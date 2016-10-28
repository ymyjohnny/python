from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import *
from forms import *

# Create your views here.

import re
import sys
import gzip
import datetime
import pandas
from StringIO import StringIO

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            logfile = request.FILES['logfile']
            if not logfile.name.endswith('.gz'):
                buf = StringIO()
                with gzip.GzipFile('', fileobj=buf) as fz:
                    fz.write(logfile)
                logfile = buf.getvalue()
            rec = Logfiles()
            rec.logfile = ''.join(logfile.chunks())
            rec.save()
            return HttpResponseRedirect(reverse('record', args=(rec.id,)))
    form = UploadFileForm()
    return render(request, 'logs/index.html', {'form': form})

headers = ['ipaddr', 'date', 'method', 'path', 'version', 'headline',
           'status', 'time', 'reference', 'agent']
re_log = re.compile('(?P<ipaddr>\S*) - (?P<user>\S*) \[(?P<date>.*) \+0800\]\s+"((?P<method>\S*) (?P<path>\S*) (?P<version>\S*)|(?P<headline>.*))" (?P<status>\d*) (?P<size>\d*) (?P<time>[0-9\.]*) "(?P<reference>.*)" "(?P<agent>.*)"')
dt_fmt = '%d/%b/%Y:%H:%M:%S'


def parser(line):
    line = line.strip()
    m = re_log.match(line)
    assert m, Exception(line)
    d = m.groupdict()
    d['date'] = datetime.datetime.strptime(d['date'], dt_fmt)
    return d

def log_source(datafile):
    for line in datafile:
        yield parser(line)

def get_dateframe(recid):
    rec = Logfiles.objects.get(id=int(recid))
    logdata = gzip.GzipFile('', fileobj=StringIO(rec.logfile))
    return pandas.DataFrame(log_source(logdata))

def record(request, recid):
    daytime_url = reverse('daytime', args=(recid))
    dt = get_dateframe(recid)
    ipaddr_head = dt.ipaddr.value_counts().head(10)
    return render(request, 'logs/record.html', {
        'daytime_url': daytime_url,
        'ipaddr_head': ipaddr_head,})

def img_daytime(request, recid):
    dt = get_dateframe(recid)
    vc = dt.date.map(lambda x: x.hour).value_counts(sort=False).sort_index()
    buf = StringIO()
    vc.plot().get_figure().savefig(buf)
    return HttpResponse(buf.getvalue(), content_type='image/jpeg')

