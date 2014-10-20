# Ethan Busbee
# 17 October 2014 (Initial)
# 19 October 2014 (Update)

# Duper.py contains a class, Duper, that can replicate output across multiple output streams using the usual print statement.
# This code is based on work by Thrustmaster on Stackoverflow: http://stackoverflow.com/questions/11325019/output-on-the-console-and-file-using-python

import sys

class Duper(object):
    """Duper duplicates output across multiple output streams. (These might not synchronize in real-time due to buffering.)"""

    files = sys.stdout  # giving a default value so things don't explode because of a KeyboardInterrupt or anything like that

    def __init__(self, *files):
        """Input = any number of output streams. (Default output stream is sys.stdout)
        Usage = \"sys.stdout = Duper(sys.stdout, *other files*\"
        NOTE: If you don't use the above format, it's possible to cut console output completely!"""
        self.files = files

    def __del__(self):
        """This is a delete function, why are you even reading its documentation?"""
        self.closeOuts()

    def write(self, obj):
        """Input = something to write. (Don't call this yourself, use print statements.)"""
        for f in self.files:
            f.write(obj)

    def getOuts(self):
        """Returns the list of output stream files that are being written to."""
        return self.files

    def setOuts(self, *files):
        """Input = a list of 0 or more output files to replace the current list."""
        self.files = files

    def addOut(self, *outfiles):
        """Input = a list of 0 or more output streams to add to the current list."""
        for outfile in outfiles:
            if outfile not in self.files: self.files += outfile

    def removeOut(self, *outfiles):
        """Input = a list of 0 or more output streams to remove from the current list."""
        for outfile in outfiles:
            if outfile in self.files: self.files -= outfile

    def closeOuts(self):
        """Closes all attached output streams, if applicable."""
        for f in self.files:
            try: f.close()
            except: continue
