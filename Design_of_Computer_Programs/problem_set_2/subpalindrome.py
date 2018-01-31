# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    
    # Your code here
    text = list(text.lower())
    
    for i in range(len(text), 0, -1):
        
        if "result" in locals():
            break
        
        for j in range(0, len(text)-i):
            
            if "result" in locals():
                break
            
            a = j; b = j + i
            
            while text[a] == text[b] and a <= b:
                
                a += 1
                b -= 1
                
                if a - b == 0:
                    result = (j, j+i+1)
                    break
                
    if "result" not in locals(): return (0,0)
    else: return result

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    #assert L('Race carr') == (0, 8)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()