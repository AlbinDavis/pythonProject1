class person:
    def __init(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        self.bmi=0
        self.bmists=""
    def calculatebmi(self):
        self.bmi=self.weight//(self.height*self.height)
