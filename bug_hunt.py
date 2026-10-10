
count = 1
total = 0

# BUG: Added the missing colon to the while condition.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Changed the loop condition from count < 5 to count <= 5
# so that the number 5 is included in the sum.

# BUG: Converted total to a string so it can be joined with
# the text in the print statement.
print("Sum of 1 to 5 is: " + str(total))
