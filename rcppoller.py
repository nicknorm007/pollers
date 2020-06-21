import csv
import requests
from bs4 import BeautifulSoup

class RcpPoller:
    def __init__(self, dataFile):
        self.dataFile = dataFile
        self.poll_data = []
        self.poll_map = {}

    def readPollingDataUrls(self):
        with open(self.dataFile, newline='') as csvfile:
            self.poll_data = csv.reader(csvfile)
            for row in self.poll_data:
                self.poll_map[ row[0] ] = row[1]
        print(self.poll_map)

    def pointSpread(self,elem):
        avrge = elem.find('td', class_='spread')
        return avrge.text

    def findAverages(self,res):
        avg_poll_elems = res.find_all('tr', class_='rcpAvg')
        poll_elems = res.find_all('tr', class_='isInRcpAvg')
        for poll_elem in avg_poll_elems:
            print("Average: ", pointSpread(poll_elem))
        for poll_elem in poll_elems:
            print(pointSpread(poll_elem))

    def iterateStates(self):
        for state,url in self.poll_map.items():
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='polling-data-rcp')
            print(state)
            findAverages(results)
    
        
