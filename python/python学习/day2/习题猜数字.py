

secret = 666
guess = 0
tries    = 0

while guess != secret and tries < 6:
    guess = input("input num")
    if guess < secret:
        print "small"
    elif guess >secret:
        print "big"
    elif guess == secret:
        print  "you win"
    tries = tries +1
    if tries==6:
        print "4344."
        print "555",secret
        break