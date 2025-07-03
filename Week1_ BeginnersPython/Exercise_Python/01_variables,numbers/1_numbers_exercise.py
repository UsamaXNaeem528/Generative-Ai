#1. You have a football field that is 92 meter long and 48.8 meter wide.
#   Find out total area using python and print it.
length = 92
width = 48.8
totalArea = length * width
print(f'The total area of the football field is {float(totalArea)} square meters.')

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
per_packet_cost = 1.49
no_of_buying_packets = 9
given_money = 20.0
money_back = given_money - (per_packet_cost * no_of_buying_packets)
print(f'Theshopkeeper is going to give you back {money_back}$' )

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
length = 5.5
area = length**2
replace_cost_per_sqft = 500
total_cost = area *replace_cost_per_sqft
print(f'The total cost to replace all tiles in the bathroom is {total_cost} rs.')

# 4. Print binary representation of number 177
number = 17
print(f'Binary Representation of number {number} is {bin(number)}')




