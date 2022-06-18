newWord = input("Digite una palabra: ")
oldWord = input("Digite una palabra: ")

if newWord.lower() < oldWord.lower():
    oldWord = newWord
print(oldWord)
for x in range(0 , 4):
    newWord = input("Digite una palabra: ")
    if newWord.lower() < oldWord.lower():
        oldWord = newWord
    print(oldWord)