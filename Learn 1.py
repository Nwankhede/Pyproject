#for i in range (5):
#    print (i,end="")


class Computer:
    def __init__(self):
        self.ram="4gb"
        self.graphic=("2gb")
        self.ssd="1tb"


    def config(self):
        print(self.ram,self.graphic,self.ssd)


obj=Computer()
obj.config()
