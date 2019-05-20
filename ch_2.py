height = 70
temperature = 98.6

sum = 3 + 2
difference = 88 - 2
product = 4 * 2
quotient = 16 / 4
power = 3 ** 5
remainder = 7 % 3
print('Sum: {}'.format(sum))
print('Difference: {}'.format(difference))
print('Product: {}'.format(product))
print('Quotient: {}'.format(quotient))
print('Power: {}'.format(power))
print('Remainder: {}'.format(remainder))

sum = 3 + 4
difference = 200 - 2
new_number = sum + difference
print(new_number)
print(sum / sum)
print(sum + 1)

#int() function
quantity = 4
quantity_string = '4'
total = int(quantity_string) + 1
print(total)

#float() function
quantity_string = '4'
quantity_float = float(quantity_string)
print(quantity_float)

""" The comment starts here.
This is another line in the comment.
Here is the last line of the comment. """


"""
This starts a comment down here!
Python will not attempt to interpret these lines as they are comments.
"""

# The cost of one server per hour.
Cost_per_hour = 1.02

# Compute the costs for one server.
Cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day

# Display the results.
Print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(cost_per_month))