import re

text = open('C:\DHfun\dq9.txt', 'r').read()

ourDQnums = []
enteredPhrases = []

while True:
    val = input("\nEnter your phrase:  ")

    if val == 'game over':
        break

    if val not in enteredPhrases:
        count = 0
        length = 0

        val1 = r'\b' + val + r'\s'
        val2 = r'\b' + val + r'[^\w\s]'
        val3 = r'[^\w\s]' + val

        for match in re.finditer(val1, text, re.IGNORECASE):
            count += 1
            word = text[match.start():match.start()+len(val)]
            ourDQnums.append((match.start(), word))
        for match in re.finditer(val2, text, re.IGNORECASE):
            count += 1
            word = text[match.start():match.start()+len(val) + 3].rsplit(' ', 1)
            ourDQnums.append((match.start(), word[0]))
        for match in re.finditer(val3, text, re.IGNORECASE):
            count += 1
            word = text[match.start():match.start()+len(val) + 3].rsplit(' ', 1)
            ourDQnums.append((match.start(), word[0]))
        
        enteredPhrases.append(val)
        print("\n'" + val + "' appears " + str(count) + " time(s)\n")
    
    else:
        print("\nYou already entered that phrase\n")
        enteredPhrases.append(val)

    ourDQnums.sort()
    words = [lis[1] for lis in ourDQnums]
    print(*words)


