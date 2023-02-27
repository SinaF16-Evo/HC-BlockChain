import hashlib

class information :
    def __init__ (self,name , number , bloodtype , other) :       #this information Box gets 4 emergency datas
        self.name = name
        self.num = number
        self.bt = bloodtype
        self.describtion = other

class Block :
    def __init__ (self , preblockhash , blocknumber) :
        self.datablock = []
        self.datablockdict = []
        self.preblockhash = preblockhash
        self.blocknumber = blocknumber

    def add (self , inf) :                                         #add data in block and check if that block contains 5 information Box or not
        if len(self.datablock) <= 5 :                                
            self.datablock.append(inf)
            self.datablockdict.append(inf.__dict__())
            print(f"The {inf.name}\'s Information has successfully stored in Block Number {self.blocknumber}")
            
            return True
        else:
            return False

    
    def hash (self) :
        return (hashlib.sha256(str(self.datablockdict) + str(self.preblockhash) + str(self.blocknumber)))
    
