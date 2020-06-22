from rcppoller import RcpPoller

DATA_FILE = 'data/polldata.csv'

poller = RcpPoller(DATA_FILE)
poller.process()