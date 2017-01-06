
# For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word
# sequence. Then, "ay" (some people just add "a") is added to the specific word


pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = word[1:len(new_word)] + first + pyg

    print("User input: ")
    print (original)

    print("In pig-Latin: ")
    print(new_word)
else:
    print ('empty')

