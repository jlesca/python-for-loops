# We can do a loop inside another loop.

#The "inner loop" will be executed one time for each iteration of the "outer loop":

adj = ["small", "fast", "huge"]
transport = ["car", "bike", "ship"]

for x in adj:
  for y in transport:
    print (x, y)
    
# Output:

# small car
# small bike
# small ship
# fast car
# fast bike
# fast ship
# huge car
# huge bike
# huge ship
