#!/usr/bin/python3

import os
import sys

from Alfred3 import Tools

f_path = Tools.getEnv('path')

if os.path.isdir(f_path):
    sys.stdout.write("DIR")
if f_path.endswith(".code-workspace") and os.path.isfile(f_path):
    sys.stdout.write("FILE")
else:
    pass
