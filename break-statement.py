# We can stop the loop using the statement BREAK.
# For example 

# Set a variable with list of colors.
colors = ["red", "blue", "green", "yellow"]
for x in colors: # Create a loop to display each element. 
    print(x) 
    if x == "blue": # When the element to display is BLUE
        break # The loop is stopped
        
# Futhermore, we can stop the loop before to display a item BLUE.

# Set a variable with list of colors.
colors = ["red", "blue", "green", "yellow"]
for x in colors: # Create a loop to display each element. 
    if x == "blue": # When the element to display is BLUE
      break # The loop is stopped
  print(x)
      
