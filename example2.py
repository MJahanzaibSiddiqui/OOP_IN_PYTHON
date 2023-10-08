
# TWO WAYS TO DEFINE ATTRIBUTE
# FIRST METHOD:

class myclass:
    def mymethod1(self, attr1):
        self.myattr1=attr1 
    def mymethod2(self, attr2):
        self.myattr2=attr2     
obj =myclass()
firstvalue=15
secondvalue=20
obj.mymethod1(firstvalue)#direct to attr1
obj.mymethod2(secondvalue)#direct to attr2

# SECOND METHOD:
class myclass:
    def __init__(self,attr1,attr2):
        self.myattr1=attr1
        self.myattr2=attr2
        
obj=myclass("jazzy",804)
print(obj.myattr1)
print(obj.myattr2)

