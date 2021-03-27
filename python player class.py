class Player:
    def __init__(self,playerName,playerCountry,playerScore):
        self.playerName=playerName
        self.playerCountry=playerCountry
        self.playerScore=playerScore

class Team:
    def getMinRuns(p):
        j=1
        for i in p:
            if j is 1:
                s=i.playerScore
                j+=1
            if i.playerScore <s:
                s=i.playerScore
        for i in p:
            if i.playerScore ==s:
                print(i.playerScore,i.playerName,i.playerCountry)
n=int(input())
p=[]
for i in range(n):
    name=input()
    country=input()
    score=int(input())
    p.append(Player(name,country,score))

Team.getMinRuns(p)





