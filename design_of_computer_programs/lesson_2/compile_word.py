# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word(word):
    
    if word.isupper():
        
        terms = [("%s*%s" % (10**i, char)) for (i, char) in enumerate(reversed(word))]
        
        return '(' + '+'.join(terms) + ')'
        
    else:
        return word

"""
# not fully working -> trying to solve a different problem than the proposed one
import re

def compile_word(word):

    word = right_order(word)
 
    num_generator = (10**i for i in range(0,100))

    char_generator = (char for char in list(word)[::-1])
    
    chars_generated = 0
    
    output = '('
    
    for char in char_generator:

        chars_generated += 1

        output += '+'
    
        if char.isupper():
            output += str(next(num_generator)) + '*' + char
        else:
            # The current one is added to the string
            output += char
            
            # While the next ones are lower keep adding them
            while char.islower():
                
                if chars_generated < len(word):
                    char = next(char_generator)
                else:
                    break
                
                chars_generated += 1
                
                if char.islower():
                    output += char
                    
            # When the last one is not lower treat as normal
            if char.isupper():
                output += '+' + str(next(num_generator)) + '*' + char
        
        #print("last char is %s", char)
    output = output[0]+output[2:]
    
    output += ')'
            
    return output

def right_order(word):
    #Change the order of upper words. Keep the lower ones the same
    upper_indexes = []
    
    for number, char in enumerate(word):
        if char.isupper():
            upper_indexes.append(number)
    
    upper_list = re.findall(r"[A-Z]", word)

    assert len(upper_indexes) == len(upper_list)

    word_list = list(word)

    upper_indexes_reduced = upper_indexes[0:len(upper_indexes)/2]

    for i in upper_indexes_reduced:
        
        word_list[upper_indexes[i]] = upper_list[-i-1]
        word_list[upper_indexes[i-1]] = upper_list[i]

    
    final_word = ''.join(word_list)
    
    return final_word
        
# Tests
assert compile_word('YOU') == '(1*U+10*O+100*Y)'
assert compile_word('YOUa') == '(1*U+10*O+100*Y+a)'
assert compile_word('aYOU') == '(a+1*U+10*O+100*Y)'
assert compile_word('aYOUa') == '(a+1*U+10*O+100*Y+a)'
assert compile_word('aYaOaUa') == '(a+1*U+a+10*O+a+100*Y+a)'
assert compile_word('YObzaUa') == '(1*U+10*O+bza+100*Y+a)'
assert compile_word('asas') == '(asas)'"""