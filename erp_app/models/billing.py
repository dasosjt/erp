class Billing:
	def __init__(self, products, costs, amount):
		self.desc_str = ""
		self.__description(products,costs,amount)
	def description(self, products,costs,amount):
		for i in range(len(products)):
        	self.desc_str += "Product: %s cost: %s amount: %s \n" % (self.products[i], self.costs[i], self.amount[i])
        return self.desc_str

    __description = description