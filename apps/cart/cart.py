from ..store.models import Product
from django.shortcuts import render
class Cart():
    def __init__(self, request):
        self.session = request.session
        # get current key session
        cart = self.session.get('session_key')
        # create new key session
        if 'session_key' not in self.session:
            cart = self.session['session_key']={}

        self.cart = cart

    def get_total(self):
        products_id=self.cart.keys()
        products=Product.objects.filter(id__in=products_id)
        total=0
        for key,value in self.cart.items():
            for pro in products:
                if pro.id == int(key):
                    if pro.is_sale:
                        total=total+value*(pro.sale_price)
                    else:
                        total=total+value*(pro.price)
                    break
        return total        

    def delete(self, product):
        product_id=str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified=True

    def update(self, product, quantities):
        product_id=str(product)
        product_qty=int(quantities)

        ourcart=self.cart

        ourcart[product_id]=product_qty

        self.session.modified=True

        return self.cart
        

    def add(self, product, quantities):
        product_id=str(product.id)
        product_qty=str(quantities)

        if product_id in self.cart:
            pass 
        else:
            self.cart[product_id]=int(product_qty)

        self.session.modified=True

    def get_products(self):
        products_id=self.cart.keys()

        product=Product.objects.filter(id__in=products_id)
        return product
    
    def get_quantities(self):
        quantities = self.cart
        return quantities

    def __len__(self):
        return len(self.cart)