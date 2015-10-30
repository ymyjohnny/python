import psutil,datetime
print ("hello,world")

mem = psutil.virtual_memory()
print mem
print "mem:",mem.total,mem.used

swap = psutil.swap_memory()
print swap
print "swap-used:",swap.used

cputime = psutil.cpu_times()
print cputime
print "cputime-user:",cputime.user


diskinfo = psutil.disk_partitions(all)
print diskinfo

diskused = psutil.disk_usage('/')
print diskused.percent

#disk io fenqu
diskio = psutil.disk_io_counters(perdisk=True)
print diskio

# network
network =  psutil.net_io_counters(pernic=False)
print network.bytes_sent
print network

# boot time
boottime = psutil.BOOT_TIME
print boottime
print datetime.datetime.fromtimestamp(boottime).strftime("%Y-%m-%d %H:%M:%S")





