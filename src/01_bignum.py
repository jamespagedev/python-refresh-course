# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

import sys
# YOUR CODE HERE
sys.set_int_max_str_digits(0)
print(2**65536)