#!/usr/bin/env python
import urllib
import datetime
import getopt
import sys
import os

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:p:")
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    myfile = ''
    mypath = ''
    for o, a in opts:
        if o == "-f":
            myfile = a
        elif o == "-p":
            mypath = a
    start = datetime.datetime.now()
    urllib.urlretrieve(mypath+"/"+myfile, myfile)
    end = datetime.datetime.now()
    if os.path.getsize(myfile):
        td = end - start
        print int(td.seconds*1000 + td.microseconds/1000)
        os.system("rm "+myfile)
    else
        print "Urllib unsuccessful"

if __name__ == "__main__":
    main()
