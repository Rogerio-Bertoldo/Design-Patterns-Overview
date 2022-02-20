from concrete_publishers.job_notifier import JobNotifier
from concrete_subscribers.candidate import Candidate
from events import Event

if __name__ == '__main__':
    job_notifier = JobNotifier()
    dev = Candidate(name="Rogerio", job="Senior Software developer", email="jayimo5237@ishop2k.com")
    po = Candidate(name="Desiree", job="Product Owner", email="jafyadulmi@vusra.com")

    dev.setAlert(job_notifier, Event(dev.job))
    po.setAlert(job_notifier, Event(po.job))
    job_notifier.addNewJob("Senior Software developer")
    print('Code is not blocked :)')