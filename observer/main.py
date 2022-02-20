from concrete_publishers.job_notifier import JobNotifier
from concrete_subscribers.candidate import Candidate
from events import Event

if __name__ == '__main__':
    job_notifier = JobNotifier()
    
    dev = Candidate(name="Rogerio", job="Software developer", email="emailexample@domainexample.com")
    po = Candidate(name="Bob", job="Manager", email="emailexample@domainexample.com")

    dev.setAlert(job_notifier, Event(dev.job))
    po.setAlert(job_notifier, Event(po.job))

    job_notifier.addNewJob("Software developer")
    print('Code is not blocked :)')