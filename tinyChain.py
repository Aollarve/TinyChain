import datetime as date
import hashlib

class Block:
	def __init__(self, data, previous_hash):
		self.previous_hash = previous_hash
		self.data = data
		self.timeStamp = date.datetime.now() 
		self.hash = self.calculateHash()

	def __str__(self):
		to_print = """Hash = {hash}
Previous Hash: {previous_hash}
Data = {data}
TimeStamp = {timeStamp}"""

		return to_print.format(hash=self.hash, previous_hash=self.previous_hash, data=self.data, timeStamp=self.timeStamp)

	def calculateHash(self):
		calculatedHash = hashlib.sha256((str(self.previous_hash)+str(self.data)+str(self.timeStamp)).encode()).hexdigest()
		return calculatedHash


def create_genesis_block():
	return Block("Genesis Block", 0)

print(create_genesis_block())


