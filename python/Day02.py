#Given the meal price (base cost of a meal), tip percent (the percentage of the
#meal price being added as tip), and tax percent (the percentage of the meal
#price being added as tax) for a meal, find and print the meal's total cost.


meal = float(raw_input())
tip = float(raw_input())
tax = float(raw_input())

tip = meal*(tip/100)
tax = meal*(tax/100)
cost = meal+tip+tax
if cost>(int(cost)+0.5) :
    cost = str(int(cost)+1)
else :
    cost = str(int(cost))

print "The total meal cost is "+cost+" dollars."
