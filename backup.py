#!/usr/bin/python3

import sys
import math
from backupcfg import jobs

def main():
    
    try:
        argCount = len(sys.argv)
        
        if argCount != 2:
            print("ERROR: job not specified")
        else:
            jobName = sys.argv[1]
            if not jobName in jobs:
                print(f"ERROR: job {jobName} is not in job list")
            else:
                pass
            
    except:
        print("ERROR: An error has occurred.")

if __name__ == '__main__':
    main()