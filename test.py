# Ethan Busbee
# 2014-12-28 (File creation)

# This test file is intended to test the Duper class contained within Duper.py.

from Duper import Duper
from datetime import datetime

d = Duper() # Should only print to console

print "This should only be on the console!"

now = "log/log_" + str(datetime.now())
out = open(now, "w")

d.addOuts(out)

print "This should be on the console and in the log file!"