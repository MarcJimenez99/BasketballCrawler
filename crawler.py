from bs4 import BeautifulSoup
from lxml import html
from urllib.parse import urljoin, urlparse
import urllib.request
import requests
import time

PriorityQueue = []
TraveledLinks = []
class Crawler():


    def parse(self):

        url = 'https://www.basketball-reference.com/'
        TraveledLinks.append(url)
        page_to_soup = urllib.request.urlopen(url)
        soup = BeautifulSoup(page_to_soup, "html.parser")
        html_page = requests.get(url)
        with open('html_files/start.html', 'wb') as f:
            f.write(html_page.content)
        for link in soup.findAll('a'):
            # print(link.get('href'))
            currentLink = urljoin(url, link.get('href')) 
            if currentLink not in TraveledLinks and currentLink not in PriorityQueue:
                # if 'player' in currentLink:
                #     PriorityQueue.insert(0, currentLink)
                #     TraveledLinks.append(currentLink)
                # else:
                    PriorityQueue.append(currentLink)
                    TraveledLinks.append(currentLink)

        # print(len(PriorityQueue))
        iteration = 0
        for element in PriorityQueue: 
            time.sleep(5)
            print(f'Iteration: {iteration}')
            TraveledLinks.append(element)
            print(f'URL: {element}')
            try:
                page_to_soup = urllib.request.urlopen(element)
            except:
                print(f'Bad URL do not crawl.')
                PriorityQueue.remove(element)
                print(f'Remaining Links to crawl: {len(PriorityQueue)}')
                iteration += 1
                continue
            soup = BeautifulSoup(page_to_soup, "html.parser")
            html_page = requests.get(element)
            filename = f'crawledPage{iteration}.html'
            with open(f'html_files/{filename}', 'wb') as f:
                f.write(html_page.content)
            for link in soup.findAll('a'):
                currentLink = urljoin(element, link.get('href')) 
                if currentLink not in TraveledLinks and currentLink not in PriorityQueue:
                    # if 'player' in currentLink:
                    #     PriorityQueue.insert(0, currentLink)
                    # else:
                        PriorityQueue.append(currentLink)
            PriorityQueue.remove(element)
            print(f'Remaining Links to crawl: {len(PriorityQueue)}')
            iteration += 1

if __name__ == "__main__":
    BasketballCrawler = Crawler()
    BasketballCrawler.parse()