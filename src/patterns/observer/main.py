import os
import sys

#TODO This hack isn't a good way to allow the importing of sibling modules...
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from concrete_publishers.job_notifier import JobNotifier
from concrete_subscribers.candidate import Candidate
from events import Event

if __name__ == '__main__':
    job_notifier = JobNotifier()
    
    dev = Candidate(name="Rogerio", job="Software developer", email="pogeyef279@reimondo.com")
    manager = Candidate(name="Bob", job="Manager", email="jafyadulmi@vusra.com")

    dev.setAlert(job_notifier, Event(dev.job))
    manager.setAlert(job_notifier, Event(manager.job))

    job_notifier.addNewJob("Software developer")
    job_notifier.addNewJob("Manager")
    print('Code is not blocked :)')
