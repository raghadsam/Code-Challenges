#Building Dictionaries 
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
dictionary1 = {}
dictionary2 = {}

#Using for loop
for word in book_title:
    if word not in dictionary1:
        dictionary1[word] = 1
    else:
        dictionary1[word] += 1
print(dictionary1)

#Using get method
for word in book_title:
    dictionary2[word] = dictionary2.get(word, 0) + 1
print(dictionary2)

