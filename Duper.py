# Ethan Busbee
# 17 October 2014 (Initial)
# 19 October 2014 (Update)
# 28 December 2014 (Update)

# Duper.py contains a class, Duper, that can replicate output across multiple output streams using the usual print statement.
# This code is based on work by Thrustmaster on Stackoverflow: http://stackoverflow.com/questions/11325019/output-on-the-console-and-file-using-python

import sys

class Duper(object):
    """Duper duplicates output across multiple output streams. (These might not synchronize in real-time due to buffering.)"""

    def __init__(self, *files):
        """Input = any number of output streams.
        Usage = \"sys.stdout = Duper([output files])\"
        NOTE: Console output will be automatically included.
        You can turn this off by calling Duper.useConsole(False).
        This can be reenabled in the same way later."""

        self._files = set(files)
        self.addOuts(sys.stdout)

    def __del__(self):
        """This is a delete function, why are you even reading its documentation?"""
        self.closeOuts()

    def write(self, obj):
        """Input = something to write. (Don't call this yourself, use print statements.)"""
        for f in self._files:
            f.write(obj)
            f.write('test')

    def getOuts(self):
        """Returns the list of output stream files that are being written to."""
        return self._files

    def setOuts(self, *files):
        """Input = a list of 0 or more output files to replace the current list."""
        self._files = files

    def addOuts(self, *outfiles):
        """Input = a list of 0 or more output streams to add to the current list."""
        for outfile in outfiles:
            self._files.add(outfile)    

    def removeOuts(self, *outfiles):
        """Input = a list of 0 or more output streams to remove from the current list."""
        for outfile in outfiles:
            self._files.remove(outfile)

    def closeOuts(self):
        """Closes all attached output streams, if applicable."""
        for f in self._files:
            try: f.close()
            except: continue
