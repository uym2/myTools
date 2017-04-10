#!/usr/bin/env python

import pylauncher
import sys

task = sys.argv[1]
np = sys.argv[2]

##
## Emulate the classic launcher, using a one liner
##

pylauncher.ClassicLauncher(task,
                           debug="job+task+host+exec+command",
                           cores=np)

