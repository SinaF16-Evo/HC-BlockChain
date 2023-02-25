from Block import Block
import hashlib

class HC :
    def __init__(self) :
        self.chain = []
        self.chain.append(Block("Genesis Block" , 1))
        
