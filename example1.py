
# constructor practice code or syntax
class customer:
    def __init__(self,name):
     self.myname=name #created .myname attribute and set it to name parameter 
     print("constructor")
     
cust=customer("jazzy")
print(cust.myname)  