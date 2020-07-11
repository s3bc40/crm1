# Init : python manage.py shell
from accounts.models import *
customer = Customer.objects.all()
print(customer)
<QuerySet [<Customer: Joe>, <Customer: John Doe>]>

# Get first or last customer
print(customer.first())
Joe
print(customer.last())
John Doe

# Get from attributes
customer1 = Customer.objects.get(name='John Doe')
print(customer1)
John Doe
print(customer1.email)
john.doe@noemail.com
print(customer1.id)
2
customer1 = Customer.objects.get(id=2)
print(customer1)
John Doe

# One to Many relationship : Parent to child
orders = customer1.order_set.all()
print(orders)
<QuerySet [<Order: Order object (1)>, <Order: Order object (3)>]>

# One to Many relationship : Child to Parent
order = Order.objects.first()
print(order.customer.name)
John Doe
print(order.customer.phone)
56658887
print(order.customer.email)
john.doe@noemail.com

# Filter out products
products = Product.objects.filter()
print(products)
<QuerySet [<Product: BBQ Grill>, <Product: Baking Soda>, <Product: Running Shoes>]>
products = Product.objects.filter(category='Indoor')
print(products)
<QuerySet [<Product: Baking Soda>]>
products = Product.objects.filter(category='Out door')
print(products)

# Order the query : ascendant or descendant
<QuerySet [<Product: BBQ Grill>, <Product: Running Shoes>]>
products = Product.objects.all().order_by('id')
print(products)
<QuerySet [<Product: BBQ Grill>, <Product: Baking Soda>, <Product: Running Shoes>]>
products = Product.objects.all().order_by('-id')
print(products)
<QuerySet [<Product: Running Shoes>, <Product: Baking Soda>, <Product: BBQ Grill>]>

# Manu to Many relationship : table__attribute
products = Product.objects.filter(tags__name='ZeroWaste')
print(products)
