# CS172 Final Project
## Collaboration Details: Description of contribution of each team member.

## Part 1 - Crawler
### Overview of system, including (but not limited to)
#### (a) Architecture
![Crawler Architecture](CrawlerArchitecture.jpg)
#### (b) The Crawling or data collection strategy (do you handle duplicate URLs, is your crawler parallel, etc.)
Our crawler makes use of two lists one called ***PriorityQueue[]*** and another called ***TraveledLinks[]***. Every
URL popped from our **PriorityQueue** will be added to our **TraveledLinks** list and after parsing through the URL's 
HTML, we will iterate through all existing links and check to see if they exist in both of our **PriorityQueue** and **TraveledLinks** lists. If they do not then we will add it to our **PriorityQueue**.
#### (c) Data Structures employed
We make use of the Python Data Structure List
### (d) Limitations (if any) of the system.
UNSURE
### (e) Instruction on how to deploy the crawler. 
To run the crawler run the following command:
```
python3 crawler.py <seedURLs.txt> <number of pages to crawl> <outputFile>**
```
## Part 2 - Indexer
Instructions on how to deploy the system. Ideally, you should include an indexer.bat (Windows) or indexer.sh (Unix/Linux) executable file that takes as input all necessary parameters .  Example: [user@server] ./indexer.sh < output − dir >
## Part 3 - Extension
Detailed description of your ‘extension’ and motivation or benefit of the implemented feature or extension. Include screen shots of your system in action.
