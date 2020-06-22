import csv
import requests
from bs4 import BeautifulSoup
from array import *

class RcpPoller:
    def __init__(self, dataFile):
        self.__dataFile = dataFile
        self.__poll_data = []
        self.__poll_map = {}
        self.__left = []
        self.__height = []
        self.__labels = []
        self.__xlabel = ''
        self.__ylabel = ''
        self.__title = ''
        self.__current_contest = ''

    def __pointSpread(self,elem):
        avrge = elem.find('td', class_='spread')
        return avrge.text

    def __tabulate(self, text):
        point_spread = text.split('+')
        self.__labels.append(self.__current_contest)
        self.__height.append(point_spread[1])

    def __findAverages(self,res):
        avg_poll_elems = res.find_all('tr', class_='rcpAvg')
        poll_elems = res.find_all('tr', class_='isInRcpAvg')
        for poll_elem in avg_poll_elems:
            avg_point_spread_text = self.__pointSpread(poll_elem)
            print("Average: ", avg_point_spread_text )
            self.__tabulate(avg_point_spread_text)
        for poll_elem in poll_elems:
            point_spread_text = self.__pointSpread(poll_elem)
            print( point_spread_text )

    def __readPollingUrlData(self):
        with open(self.__dataFile, newline='') as csvfile:
            self.__poll_data = csv.reader(csvfile)
            for row_num,row in enumerate(self.__poll_data):
                if row_num == 0: #first row
                    self.__title = row[0]
                    self.__xlabel = row[1]
                    self.__ylabel = row[2]
                else:
                    self.__poll_map[ row[0] ] = row[1]

    def process(self):
        self.__readPollingUrlData()
        for contest,url in self.__poll_map.items():
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='polling-data-rcp')
            self.__current_contest = contest
            print(contest)
            self.__findAverages(results)
    
        
