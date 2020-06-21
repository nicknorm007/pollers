from rcppoller import RcpPoller

poller = RcpPoller('data/polldata.csv')
poller.readPollingDataUrls()
poller.iterateStates()

