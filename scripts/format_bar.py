"""
Given a capacity and a current value, return a string representing a bar to be printed to the console.

Usage:
    format_bar.py <current> <capacity> <length>

Args:
    current (int): The current value.
    capacity (int): The maximum value.
    length (?int): The length of the bar to be printed. Defaults to the capacity.

Returns:
    bar (str): The bar to be printed to the console. Like so:
    [60/100] ######---- 60%
    
"""
if args == []:
    raise Exception("No arguments provided")
elif len(args) < 2:
    raise Exception("Not enough arguments provided")

# Args
current = int(args[0])
capacity = int(args[1])
length = capacity if len(args) < 3 else int(args[2])
# Values
# [current/capacity] full_blocksempty_blocks percentage%
# handle divisin by zero
percentage = (current / capacity) * 100 if capacity != 0 else 0
full_blocks = int((percentage / 100) * length)
empty_blocks = length - full_blocks
# Format the bar
bar = "[{0}/{1}] {2}{3} {4}%".format(
    current,
    capacity,
    "#" * full_blocks,
    "-" * empty_blocks,
    int(percentage))

# Return the result
result = bar
