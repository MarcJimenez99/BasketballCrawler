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
        index = 0
        while (pagesToCrawl > 0):
            time.sleep(5)
            print(f'Pages Crawled: {pagesCrawled}')
            url = PriorityQueue.pop(0)
            print(f'Current URL: {url}')
            TraveledLinks.append(url)
            robot_txt = url + "robots.txt"
            allowedToCrawl = False
            try:
                robot_page = urllib.request.urlopen(robot_txt)
                robot_soup = BeautifulSoup(robot_page, "html.parser")
                string = "User-agent: *"
                for line in robot_soup:
                    if string in line:
                        allowedToCrawl = True
                        print("Allowed to crawl this page...")
            except:
                print(f'No Robots.txt for this URL.')
                allowedToCrawl = True
    
            if allowedToCrawl: 
                try:
                    html_page = urllib.request.urlopen(url)
                except:
                    print(f'Bad URL do not crawl.')
                    pagesCrawled += 1
                    continue
                soup = BeautifulSoup(html_page, "html.parser")
                html_page_body = str(soup.body.text).strip('/n').replace('\n', ' ').replace('(', "").replace(')', "").replace("`", "").replace("'", "").replace("u'", "'")
                html_page_body_encode = html_page_body.encode("ascii", "ignore")
                html_page_body_decode = html_page_body_encode.decode()
                dict = {
                    "index":  {}
                }
                htmldict = {
                    "html": html_page_body_decode
                }
                with open('data.json', 'a') as f:
                    json.dump(dict, f)
                    f.write('\n')
                    json.dump(htmldict, f)
                    f.write('\n')
                    print("Updated JSON")
                    index += 1
                for link in soup.findAll('a'):
                    currentLink = urljoin(url, link.get('href')) 
                    if currentLink not in TraveledLinks and currentLink not in PriorityQueue:
                        if 'basketball' in currentLink:
                            PriorityQueue.insert(0, currentLink)
                        else:
                            PriorityQueue.append(currentLink)
                pagesToCrawl -= 1
            else:
                print("Couldn't crawl page")
            pagesCrawled += 1
            allowedToCrawl = False
            

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