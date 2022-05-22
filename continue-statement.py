# We can stop the current iteration of the loop and using CONTINUE statement the loop continue to the next items.

# We've a list of colors, when the iteration find "GREEN", won´t display it and continue with the next.

# Set a variable with a list of colors.
colors = ["red", "blue", "green", "yellow", "pink"]
for x in colors: 
    if x == "green": # If iteration find "green",
        continue # Don't show and continue to the next
    print(x)
 
