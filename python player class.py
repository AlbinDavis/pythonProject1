class Player:
    def __init__(self,playerName,playerCountry,playerScore,Wicket):
        self.playerName=playerName
        self.playerCountry=playerCountry
        self.playerScore=playerScore
        self.Wicket=Wicket

class Team:
    def getMinRuns(p):
        min_score_index = 0
        for i in range(1, len(p)):
            if p[i].playerScore < p[min_score_index].playerScore:
                min_score_index = i
        print(p[min_score_index].playerName, p[min_score_index].playerCountry,p[min_score_index].playerScore)
    def getMaxWickets(p):
        max_wicket_index=0
        for i in range(1,len(p)):
            if p[i].Wicket>p[max_wicket_index].Wicket:
                max_wicket_index=i
        print(p[max_wicket_index].playerName, p[max_wicket_index].playerCountry, p[max_wicket_index].playerScore,
              p[max_wicket_index].Wicket)

n=int(input())
p=[]
for i in range(n):
    name=input()
    country=input()
    score=int(input())
    wicket=int(input())
    p.append(Player(name,country,score,wicket))

Team.getMinRuns(p)
Team.getMaxWickets(p)
