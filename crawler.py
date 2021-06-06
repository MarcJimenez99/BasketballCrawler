from bs4 import BeautifulSoup
from lxml import html
from urllib.parse import urljoin, urlparse
import urllib.request
import requests
import time
import json

class Crawler():


    def parse(self, seedURLs, pagesToCrawl):
        PriorityQueue = []
        TraveledLinks = []

        for element in seedURLs:
            PriorityQueue.append(element)
        pagesCrawled = 1
        while (pagesToCrawl > 0):
            time.sleep(5)
            print(f'Pages Crawled: {pagesCrawled}')
            url = PriorityQueue.pop(0)
            print(f'Current URL: {url}')
            TraveledLinks.append(url)
            try:
                page_to_soup = urllib.request.urlopen(url)
            except:
                print(f'Bad URL do not crawl.')
                pagesCrawled += 1
                continue
           
            soup = BeautifulSoup(page_to_soup, "html.parser")
            html_page = requests.get(url)
            with open(f'html_files/{filename}', 'wb') as f:
                f.write(html_page.content)
            for link in soup.findAll('a'):
                currentLink = urljoin(url, link.get('href')) 
                if currentLink not in TraveledLinks and currentLink not in PriorityQueue:
                    if 'basketball' in currentLink:
                        PriorityQueue.insert(0, currentLink)
                    else:
                        PriorityQueue.append(currentLink)
            pagesCrawled += 1
            pagesToCrawl -= 1

        #  try:
        #         page_to_soup = urllib.request.urlopen(element)
        #     except:
        #         print(f'Bad URL do not crawl.')
        #         PriorityQueue.remove(element)
        #         print(f'Remaining Links to crawl: {len(PriorityQueue)}')
        #         iteration += 1
        #         continue
        

        # print(len(PriorityQueue))
        # iteration = 0
        # for element in PriorityQueue: 
            
          
        #     TraveledLinks.append(element)
        #     print(f'URL: {element}')
        #     try:
        #         page_to_soup = urllib.request.urlopen(element)
        #     except:
        #         print(f'Bad URL do not crawl.')
        #         PriorityQueue.remove(element)
        #         print(f'Remaining Links to crawl: {len(PriorityQueue)}')
        #         iteration += 1
        #         continue
        #     soup = BeautifulSoup(page_to_soup, "html.parser")
        #     html_page = requests.get(element)
        #     filename = f'crawledPage{iteration}.html'
        #     with open(f'html_files/{filename}', 'wb') as f:
        #         f.write(html_page.content)
        #     for link in soup.findAll('a'):
        #         currentLink = urljoin(element, link.get('href')) 
        #         if currentLink not in TraveledLinks and currentLink not in PriorityQueue:
        #             # if 'player' in currentLink:
        #             #     PriorityQueue.insert(0, currentLink)
        #             # else:
        #                 PriorityQueue.append(currentLink)
        #     PriorityQueue.remove(element)
        #     print(f'Remaining Links to crawl: {len(PriorityQueue)}')
        #     iteration += 1

if __name__ == "__main__":
    BasketballCrawler = Crawler()
    pagesToCrawl = int(input("How many pages would you like to crawl?: "))
    with open('seedURLs.txt') as f:
        seedURLs = f.readlines()
    seedURLs = [x.strip() for x in seedURLs] 
    print(seedURLs)
    BasketballCrawler.parse(seedURLs, pagesToCrawl)