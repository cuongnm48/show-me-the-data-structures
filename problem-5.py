import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.block_list = []

    def add_block(self, data):
        if self.block_list:
            previous_hash = self.block_list[-1].hash
        else:
            previous_hash = None
        timestamp = datetime.datetime.now(datetime.timezone.utc)
        new_block = Block(timestamp, data, previous_hash)
        self.block_list.append(new_block)    

    def print_blocks(self):
        for current_block in self.block_list:
            print("Timestamp:", current_block.timestamp)
            print("Data:", current_block.data)
            print("Previous Hash:", current_block.previous_hash)
            print("Hash:", current_block.hash)
            print()

blockchain = Blockchain()

# Test Case 1: Add blocks to the blockchain
blockchain.add_block("Block 0")
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
print("Blockchain with 3 blocks:")
blockchain.print_blocks()

# Test Case 2: Empty blockchain
empty_blockchain = Blockchain()
print("\nEmpty Blockchain:")
empty_blockchain.print_blocks()

# Test Case 3: Large data value
large_data_blockchain = Blockchain()
large_data = "a" * 100
large_data_blockchain.add_block(large_data)
print("\nBlockchain with large data:")
large_data_blockchain.print_blocks()

