from bs4 import BeautifulSoup
from lxml import html
from urllib.parse import urljoin, urlparse
import urllib.request
import requests

PriorityQueue = []

# class PriorityQueue(object):
#     def __init__(self):
#         self.queue = []
  
#     def __str__(self):
#         return ' '.join([str(i) for i in self.queue])
  
#     # for checking if the queue is empty
#     def isEmpty(self):
#         return len(self.queue) == 0
  
#     # for inserting an element in the queue
#     def insert(self, data):
#         self.queue.append(data)
  
#     # for popping an element based on Priority
#     def delete(self):
#         try:
#             max = 0
#             for i in range(len(self.queue)):
#                 if self.queue[i][1] > self.queue[max][1]:
#                     max = i
#             item = self.queue[max]
#             del self.queue[max]
#             return item
#         except IndexError:
#             print()
#             exit()

class Crawler():


    def parse(self):

        url = 'https://www.basketball-reference.com/'
        page_to_soup = urllib.request.urlopen(url)
        # soup = BeautifulSoup(page_to_soup, 'lxml')
        # section = soup.section
        # for url in section.find_all('a'):
        #     print(urljoin(url, url.get('href')))
        soup = BeautifulSoup(page_to_soup, "html.parser")
        html_page = requests.get(url)
        with open('html_files/start.html', 'wb') as f:
            f.write(html_page.content)

        for link in soup.findAll('a'):
            # print(link.get('href'))
            currentLink = urljoin(url, link.get('href')) 
            if currentLink not in PriorityQueue:
                if 'player' in currentLink:
                    PriorityQueue.insert(0, currentLink)
                else:
                    PriorityQueue.append(currentLink)
    
        # print(PriorityQueue)
        iteration = 0
        for element in PriorityQueue: 
            page_to_soup = urllib.request.urlopen(element)
            soup = BeautifulSoup(page_to_soup, "html.parser")
            html_page = requests.get(element)
            filename = f'crawledPage{iteration}.html'
            with open(f'html_files/{filename}', 'wb') as f:
                f.write(html_page.content)
            for link in soup.findAll('a'):
                currentLink = urljoin(element, link.get('href')) 
                if currentLink not in PriorityQueue:
                    if 'player' in currentLink:
                        PriorityQueue.insert(0, currentLink)
                    else:
                        PriorityQueue.append(currentLink)
            iteration += 1

if __name__ == "__main__":
    BasketballCrawler = Crawler()
    BasketballCrawler.parse()