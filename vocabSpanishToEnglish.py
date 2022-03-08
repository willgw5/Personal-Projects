from random import shuffle      
f = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\SpanishWords.txt",'r')#open wordlist from desktop
readList=[]
for line in f:
	readList.append(line)   #read wordlist into list format: la spanishword, englishword\n

f.close()

spanishStrings=[]       #declare the lists to put the words into
englishStrings=[]
correctIndex=[]
incorrectIndex=[]
learntWords=[]
unlearntWords=[]

shuffle(readList)       #randomise the order of the list

for i in readList:
        possibleAnswersList=[]
        endlessString=i.splitlines()                                    #cut the newline char
        splitString=endlessString[0].split(', ')                        #split the line at the comma into a 2 word list
        
        for j in range(len(splitString)-1):                             #there can be more than one possible english answer
                possibleAnswersList.append(splitString[j+1])            #append a list of them (will be list of size one for most)
               
        spanishStrings.append(splitString[0])                           #append the spanish line to a list of strings
        englishStrings.append(possibleAnswersList)                      #append the list of english answers to a list 

listLength=len(readList)
questionNumber=int(input("How many words would you like to test, up to: "+str(listLength)+'\n'))

for i in range(questionNumber):
        print('Translate','\'' + spanishStrings[i] +'\'', 'into English')       #Read out Spanish word
        ans=input('Answer:')                                                    #Take input
        for k in range(len(englishStrings[i])):                                 #looping over each possible answer
                
                if ans==englishStrings[i][k]:                                   #Check if it matches corresponding english word
                        if len(englishStrings[i])>1:
                                print('Correct, full options are:' + str(englishStrings[i]))
                        else:
                                print('Correct!')
                                        
                                                                               #end loop if it matches a correct answer
                        correctIndex.append(i)                                  #note an index for every correct answer
                        break
        else:
                
                print('Incorrect! Correct answer was:'+ str(englishStrings[i]))       #if loop ends with no correct answer, print incorrect
                incorrectIndex.append(i)                                        #note an index for every incorrect answer


indexNumber=0                                                                   #initialise a counter for indexing the original readList
for i in readList[:len(correctIndex)+len(incorrectIndex)]:                      #only count over the words that were actually tested

        for k in correctIndex:
                if indexNumber==k:                                              #loop through the original list and see if it was correctly translated (index matches correct index)
                        learntWords.append(readList[indexNumber])               #if it was, append the original list entry to a new learnt words list
                        indexNumber += 1                                        #use a manual index counter to iterate through the readList
                        break
       
        for j in incorrectIndex:                                                #do the same but checking against incorrect index
                if indexNumber==j:         
                        unlearntWords.append(readList[indexNumber])
                        indexNumber += 1
                        break


if len(unlearntWords)>0:                                                        #print a list of incorrect answers and their soluitions
        print('The ones you answered incorrectly were:')
        for i in unlearntWords:
                print(i)
for i in readList[indexNumber:]:                                                #for untested words 
         unlearntWords.append(i)                                                #put in the unlearnt pile
        

        
f = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\SpanishWords.txt",'r+')
f.truncate()
f.writelines(unlearntWords)
f.close()
f = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Vocab Tester\\LearntSpanishWords.txt",'a')
f.writelines(learntWords)
f.close()
input('Press any button to close')


