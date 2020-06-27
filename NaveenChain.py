
#This is a blockchain constructor which makes an initial empty list to store our block chain as well another list to store transactionss.
class NaveenChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self):
        # This creates a new block and adds it to the list
        pass
    
    def new_transaction(self):
        # This adds a new transaction to the list of transactions
        pass
    
    @staticmethod
    def hash(block):
        # Creates a hash/hashes the block
        pass

    @property
    def last_block(self):
        # Gets the last block
        pass
