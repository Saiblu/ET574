"""
Write one line of code for each step a - e. Save your code as PE1_4.py.
Discounted Price – The following steps calculates the price of an item after 25% reduction.
a) Create a variable price and assign it the value 99.99.
b) Create a variable discountPercent and assign it the value 25.
c) Create the variable markdown and assign it the value of discountPercent divided by 100 times the value of price.
d) Decrease the value of price by markdown.
e) Display the value of price (round to two decimal places).
      Example Output:
      Price = 74.99
"""

price= 99.99
Discountprice= 25
markdown= (Discountprice/ 100) * price 
print (markdown)
print (price - markdown)
print (round(price, 2))