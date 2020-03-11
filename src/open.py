#!/usr/bin/python

import os
import sys

from Alfred import Tools

f_path = Tools.getEnv('path')

if os.path.isdir(f_path):
    sys.stdout.write("DIR")
if f_path.endswith(".code-workspace") and os.path.isfile(f_path):
    sys.stdout.write("FILE")
else:
    pass
