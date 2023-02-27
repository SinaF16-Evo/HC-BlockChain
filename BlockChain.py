from Block import Block , information
import hashlib

class HC :
    def __init__(self) :
        self.chain = []                                                         #init Genesis Block and second Block after creating class
        self.chain.append(Block(0 , 1))
        self.chain.append(self.chain[-1].hash() , len(self.chain) + 1)

    def adding (self) :
        data = []                                                               #this method gets new information and check if last block is full or not
        data.append(input("Enter Your Name :"))                                 #if not full it creates new block
        data.append(input("Enter Your Phone Number :"))
        data.append(input("What is yout Blood Type?"))
        data.append(input("Any Description?"))
        if self.chain[-1].add(information(data[0] , data[1] , data[2] , data[3])) :
            pass
        else :
            self.chain.append(Block(self.chain[-1].hash() , len(self.chain) + 1))
        
    def validation (self) :
        if self.chain[-1].preblockhash == self.chain[-2].hash() :
            print("Chain is Valid!")
        else :
            print("Chain is Not Valid!")