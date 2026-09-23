# initializing variables for this program
# eggs act as an input within this program
# the output needs to be number of full boxes that can be made from them
# (there are 6 eggs in each box), additionally the number of left over eggs should also be displayed

# taking users input for number of eggs 
n_eggs = int(input("\nHow many eggs do you have? "))

# calculating the total number of boxes using the number of eggs variable
n_total_boxes = n_eggs // 6


# calculating the remainder of eggs left over after they have been sorted into boxes
remainer_from_total_boxes = n_eggs % 6

# basic print statement to let users know the number of eggs they have
print(f"\nYou have {n_eggs} eggs.")

# we save the message we want to show to users as a variable.. then we print that variable to the terminal
message_to_user = f"\nYou can make {n_total_boxes} with {remainer_from_total_boxes} eggs left over."
print(message_to_user)