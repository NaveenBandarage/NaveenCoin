
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
    
      def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

#example of what the block will look like. 
# block = {
#     'index': 1,
#     'timestamp': 1506057125.900785,
#     'transactions': [
#         {
#             'sender': "8527147fe1f5426f9dd545de4b27ee00",
#             'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
#             'amount': 5,
#         }
#     ],
#     'proof': 324984774000,
#     'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
# }