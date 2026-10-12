class Node:
    def __init__(self,url : str):
        self.data = url
        self.prev = None
        self.next = None 

class BrowserHistory:


    def __init__(self, homepage: str):
        self.currPage = Node(homepage)
        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.currPage
        self.currPage.next = newNode
        self.currPage = newNode
        

    def back(self, steps: int) -> str:

        while steps > 0:
            if self.currPage.prev:
                self.currPage = self.currPage.prev
            else:
                break

            steps -= 1

        return self.currPage.data

        

    def forward(self, steps: int) -> str:

        while steps > 0:
            if self.currPage.next:
                self.currPage = self.currPage.next
            else:
                break
            steps -= 1

        return self.currPage.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)