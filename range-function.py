# In Python we can loop through a specified number of times with RANGE() function.

# The secuence of numbers. start from position 0 (zero) and increments by 1 (one) by default.

for x in range(6):
    print(x) # Display secuence of numbers starting from 0 to 5, because the loop ends in the position before (5) the specified number (6)
    
    
# We can specified where we want start the iterarion.

for x in range(1, 6):
    print(x) # Display secuence of numbers starting from 1 to 5, because we've specified start from 1
    
    
# And is possible to specify the increment value by adding a third parameter:

for x in range(1, 6, 2):
    print(x)
