#code to add a word to both tranlsation banks as well as both backup banks at once

f = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\SpanishWords.txt",'a')                       #open wordlist 
f2 = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\EnglishWords.txt",'a')
f3 = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\originalSpanishWords.txt",'a')
f4 = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\originalEnglishWords.txt",'a')

word=input("Input word in format 'la spanishword, english word, other translations'\n")
word= ('\n'+word) 

f.writelines(word)
f2.writelines(word)
f3.writelines(word)
f4.writelines(word)
f.close()
f2.close()
f3.close()
f4.close()
input('Press any button to close')


