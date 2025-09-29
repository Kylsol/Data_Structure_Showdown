# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 11. Reverse the Sequence
# Reverse a sequence using only pointer-based operations.
# Input: [a, b, c, d]
# Output: [d, c, b, a]

class Letters:
    def __init__(self, values):
        self.values = values
    
    def reverse(self):
        for slist in range(len(self.values)):
            self.values.insert(slist, self.values.pop())
        return self.values
    
list = [1, 2, 3, 4, 5, 6]

reverse = Letters(list)
result = reverse.reverse()
print(result)


# Reflection

# For some reason, adding the timer to this assignment made me stress more than it normally would have.
# I made many silly mistakes because I knew that there is a timer that I am racing against. I was able
# to finish within the limit but I think I should have been able to do this quicker. 
# I first tried pop(0) + append, but that just rotated the list and rebuilt the original order. 
# I switched to removing from the end with pop() and inserting at the current index as I scan from 
# left to right (insert(i, popped)). Repeating this for every index constructs the reversed list.
