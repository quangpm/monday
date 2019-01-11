import time
from gpioMonitor import gitCommands
from ate_settings import *
from utilities.utils import *
import os


class updateController():
    def execute(self):
        tag = self.gitComm.gitGetLatestTag()
        print("The Current Tag: " + str(tag))
        #Fetch all latest tag
        (response, message) = self.gitComm.gitFetchTag()
        if response == 0:
            tag_latest = self.gitComm.gitGetTagsOnThisCommit()
            print("Fetch Tags: " + '\n' + str(tag_latest))
            latest_tag = self.gitComm.gitGetLatestTag()
            print("The Latest Tag: " + str(tag))
            #If the latest tag is different the current tag, pull the latest SW
            if latest_tag != tag:
                # git hard reset to be able to pull and fetch.  If there is an uncommitted file, a git pull is not permitted.
                self.gitComm.gitHardReset()
                
                # git pull to get latest branch update
                branch = self.gitComm.gitGetCurrentBranchName()
                print("The current branch: " +branch)
                (response, message) = self.gitComm.gitPull(branch)
                time.sleep(2)
                if response == 0:
                    commit = self.gitComm.gitGetCommitNumber()
                    print("Commit number is: " + commit)
                    return True
                else:
                    print("Check network settings or connection")
                    return False
        else:
            return False
