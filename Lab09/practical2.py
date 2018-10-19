#! /user/local/bin/python3.4

import re

def getNumberPattern():
    expr = r"\b([0]?[0]?[0-9]|[0]?[1-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\b"
    return expr

def getLinkPattern():
    expr = r'(<a)[ ]+(href=")(?P<url>(http://|https://|ftp://|ftps://)(.*?))">(?P<text>(.*?))</a>'
    return expr

def parseFile(fileName):
    pass

'''
if __name__ == "__main__":
    # getNumberPattern()
    pattern = getNumberPattern()
    m = re.search(pattern, "We can get less than 300 pieces, but more than 005.")
    print(m.group(0))
    #m = re.search(pattern, "The point is located at (512, 189, 290).")
    #print(m.group(0))
    # getLinkPattern()
    pattern = getLinkPattern()
    htmlSnippet = 'You can download the file from <a href="ftps://local.files.io">The Repository</a> or you can search for it <a href="https://www.google.com">here.</a>'
    m = re.search(pattern, htmlSnippet)
    print(m.group('url'))
    print(m.group('text'))
'''
