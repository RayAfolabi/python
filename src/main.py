class Shopping:
    cart = [ ]
    def add_to_cart(self, item):
        self.cart.append(item)
        
customer1 = Shopping()
customer1.add_to_cart('T-shirt')
print(customer1.cart)

        
      
