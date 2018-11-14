##Simple logger tool - Spellslinger
import time
import sys

class Logger(object): 
    def __init__(self, name):
        """Set the log file name. Name passed will be adorned with
            LOG_<name>.log and saved to the active module folder."""
        self.logname = "LOG_" + name + ".log"    #puts log into modules\co8
#        self.logname = ".\\LOG_" + name + ".log"   #puts log into ToEE root
        
    def logme(self, string):
        """Log the string to file, unbuffered."""
        #write to file 
        logfile = open(self.logname, "a")
        logfile.write(str(string) + "\n")
        logfile.close()

    def logmeTimed(self, string):
        """Log the string to file with time stamp, unbuffered."""
        newstring = "*" + time.asctime() + "* " + string
        self.logme(newstring)

