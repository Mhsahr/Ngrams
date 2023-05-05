def grams (text, ngrams):
    output = []
    a = list (text)
    for i in range (len (a) - ngrams + 1):
        output.append (a[i: i + ngrams])
    return output

print (grams (text = 'hello world', ngrams = 3))