product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}

print(f"pears are: {product_to_price['pear']}")

{name: str(price) + " per fruit" for name, price in product_to_price.items()}

print(product_to_price)