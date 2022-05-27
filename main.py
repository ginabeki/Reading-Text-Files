# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename
from re import X


def read_file_content(filename):
    # [assignment] Add your code here 
    with open ('story.txt', 'r') as f:
        lines = f.read()
        print(lines)
    
    return lines
    
read_file_content('story.txt')

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text_words = text.split()
    count = dict()
    for word in text_words:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1

    
    return count
x = count_words()
print(x)