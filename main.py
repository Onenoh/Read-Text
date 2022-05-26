# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

fname = input('Enter File:')
if len(fname)< 1 : fname = 'story.txt.txt'
hand = open(fname)

di = dict()
for lin in hand:
        lin = lin.rstrip()
        print(lin)
        wds = lin.split()
        for w in wds:
                di[w] = di.get(w,0) + 1

print(di)
    



