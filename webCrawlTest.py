##too do
#prevent it from repeating pages
#implement a strategy were it just goes to united states first
#make my variables not hardoced

from playwright.sync_api import sync_playwright

import heapq

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def add(self, value: str, priority: float):
        heapq.heappush(self._queue, (-priority, self._index, value))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1] if self._queue else None


class findLink:
    target="Nintendo"
    start="https://en.wikipedia.org/wiki/United_States"
    page=None
    playwright=None
    browser=None
    visited=[]

    def setValues(self):
        print("setting values")
        trans=input("Enter the start article. This is Case Sensitive: ")
        self.start="https://en.wikipedia.org/wiki/"+trans
        self.target=input("enter the Target article. This is Case Sensitive: ")
        

    

    def __init__(self):
        pass

    def startBot(self):
        # Start Playwright without 'with'
        self.playwright = sync_playwright().start()
        
        # Launch browser and context
        self.browser = self.playwright.chromium.launch(headless=False)
        context = self.browser.new_context()
        
        # Create the page
        self.page = context.new_page()
        self.page.goto(self.start)
        print("Browser is open and ready!")

    
    def killBot(self):
        pass
        ##self.browser.close()

    def turn(self):
    # Gets the href of every single <a> tag on the page
        links = self.page.locator("a").evaluate_all("elements => elements.map(e => e.href)")

        print(f"Found {len(links)} links!")

        links = [link.replace("https://en.wikipedia.org/wiki/", "") for link in links]

        filteredLinks=[]
        for link in links:
            if "https" not in link:
                filteredLinks.append(link)
        
        for link in filteredLinks:
            #print(link)
            pass
        
        #this could make a out of bounds error
        possibleLinks=self.pickNextLink(filteredLinks)
        while(True):
            test=possibleLinks.pop()
            if  test not in self.visited:
                nextLink=test
                break
        

        print(nextLink)
        ##print("the target is",self.target)
        ##navigate to the next websit
        
        self.page.goto("https://en.wikipedia.org/wiki/"+nextLink)
        self.visited.append(nextLink)
        if(nextLink==self.target):
            print("Target found!")
            return True
        return False
    
    def pickNextLink(self,links):
        targetVec = model.encode(self.target)
        linkVectors = model.encode(links)
        # best=0
        # bestValue=links[0]
        bestValue=PriorityQueue()
        for i, linkVec in enumerate(linkVectors):
            distance=util.cos_sim(linkVec,targetVec)
            #print("the distance between",link,"and",target,"is",distance)
            bestValue.add(links[i],distance)
        return bestValue



    


class botController():
    bot=findLink()
    maxIterations=15
    i=0


    def __init__ (self):
        self.bot.setValues()
        self.bot.startBot()
        
        self.loop()
        

    def loop(self):
        found=False
        while(found==False and self.i<self.maxIterations):
            found=self.bot.turn()
            self.i=self.i+1
        if(found==True):
            print("it took",self.i,"turns to find the target") #this shouldn't say it made it if it didn't
        else:
            print("could not find the correct article in ",self.i,"tries")
        self.bot.killBot()




botController()

#bot.killBot()



#takes in a list of strings and decides which one is the most similar to the target
        
#returns 






#run()