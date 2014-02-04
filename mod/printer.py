print "module '%s' was imported" % __name__

from bender import catchphrase

def printer():
    print "Bender's catchphrase is '%s'" % catchphrase()

