def search(pattern, text):
    """
    Return true if pattern appears anywhere in text
    """
    if pattern.startswith('^'):
        return match(pattern[1:], text) # fill this line
    else:
        return match('.*' + pattern, text) # fill this line
        # match the pattern, independently of the starting of the text

def match(pattern, text):
    """
    Return True if pattern appears at the start of text
	"""

    if pattern == '':
        return True# fill in this line
    elif pattern == '$':
        return (text == '')# fill in this line
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return (match1(pattern[0], text) and
                match(pattern[1:] , text[1:])) # fill in this line

def match1(p, text):
    """
    Return  true if first character of text matches character p
    """
    if not text: return False
    return p == '.' or p == text[0] # if pattern is dot it matches everything so we
    # should return true. If it is equal to the first char of the pattern it has to 
    # return true as well

def match_star(p, pattern, text):
    """
    Return true if any number of char p, followed by pattern, matches text
    """
    return (match(pattern, text)) or
            (match1(p, text) and match_start(p, pattern, text[1:]))
            # match zero times or one time plus any times after