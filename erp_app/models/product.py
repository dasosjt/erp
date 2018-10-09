from peewee import CharField
from erp_app.models.base import BaseModel
from erp_app.models.billing import Billing

#http://docs.peewee-orm.com/en/latest/peewee/models.html
class Product(BaseModel):
    username = CharField(unique=True)

class SendProduct:
	products = ['sandwich', 'juice', 'brownie'];
	costs = [10, 5, 4]
	amount = [2, 3, 2]
	Billing(products,costs, amount)