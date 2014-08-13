#! /usr/bin/env/ python

import datetime
import getopt
import sys

reqs = ['universe = vanilla',
        'executable = get.sh',
        '+ProjectName = "scicomp-analytics"',
        'should_transfer_files = YES',
        'when_to_transfer_output = ON_EXIT',
        'periodic_remove = (((CurrentTime-QDate)>=2700)&&(JobStatus==1))||((CurrentTime-QDate)>=3600)'
        ]
methods = ['curl','urllib','wget']
objPath = 'http://stash.osgconnect.net/+olsona/'
objName = '3Doyle.txt'

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:o:")
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    resourceFileName = ''
    outFileName = ''
    for opt, arg in opts:
        if opt == "-r":
            resourceFileName = arg
        elif opt == "-o":
            outFileName = arg
    resources = [l.rstrip() for l in open(resourceFileName,'r').readlines()]
    outF = open(outFileName,'w')
    now = datetime.datetime.now()
    stringDay = datetime.datetime.strftime(now,"%Y.%m.%d")
    stringHour = datetime.datetime.strftime(now,"%Y.%m.%d.%H")
    for p in reqs:
        outF.write("{0}\n".format(p))
    outF.write("\n")
    for r in resources:
        outF.write('requirements = GLIDEIN_ResourceName == "{0}"\n'.format(r))
        for m in methods:
            if m == "urllib":
                outF.write("transfer_input_files = get.py\n")
            outF.write("arguments = -r {0} -m {1} -p {2} -f {3}\n".format(r,m,objPath,objName))
            outF.write("error = err/err.{0}\n".format(stringHour))
            outF.write("output = out/IO.{0}/IO.{1}.$(Process)\n".format(stringDay,stringHour))
            outF.write("log = log/words.log.{0}\n".format(stringHour))
            outF.write("queue 10\n\n")
    outF.close()
                

if __name__ == "__main__":
    main()
