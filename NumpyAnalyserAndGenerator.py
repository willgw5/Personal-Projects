#code to analyse books for their relative letter usage and use a markov chain to generate some text from that data

import string
import numpy as np
import random as rm
f = open("C:\\Users\\Will\\Desktop\\Python Scripts\\Text analyser\\frank.txt",'r',encoding="utf8")  #story from file

def matrixGen(file):
    fileString=file.read()

    #print(fileString) #can print if you want do not advise for novels

    displayrow=[]
    for c in string.ascii_lowercase:        #string.ascii_lowercase is the alphabet in lowercase
        displayrow.append(c)                #creating a row of the alphabet for later
        
      
    letterMatrix = np.array([["a"]*27]*27, dtype="object")
    letterMatrix[:]='a'
    letterRow = [string.ascii_lowercase[_] for _ in range(26)]      #create two lists of the lower case alphabet and combine them to form our letter matrix
    letterRow.append(' ')                                           #manually add a blank character for spaces
    letterColumn=letterRow

         
    for i in range(len(letterRow)):                                 #add together every combination of two letters to make a 27*27 matrix of aa, ab, ac etc
        for j in range(len(letterColumn)):
            letterMatrix[i][j]=letterRow[i]+letterColumn[j]

        
    frequencyMatrix = np.array([["a"]*27]*27, dtype="object")           #create a 27 long list of 27 as each which will be filled with the amount of times aa,ab,ac etc occur


    i=0                                                         #need seperate indices to count through the frequency matrix 
    j=0
    for row in letterMatrix:                                    #iterate over every 2 letter combo  
        for column in row:
            frequencyMatrix[i][j]= fileString.translate(str.maketrans('','',string.punctuation)).lower().count(column)  #and use .count to count them and add the count into a 27*27 frequency matrix. we convert all text to lowercase 
            j+=1                                                                                                #we also strip punctuation with .translate to get a more accurate comparison
                                                                
        i+=1
        j=0

    k=0
    relativePercentage=np.zeros((27,27))
    rel=0
    i=0
    j=0
    letterSums=[]
    for row in frequencyMatrix:        #find the relative percentages of the letters that follow each letter i.e. how often does h follow t, quite often, zy not so much
        a = sum(row)                    #find the sum of the row
        letterSums.append(a)
        for column in row:
            relativePercentage[i][j]=((column/a)*100)
            j+=1

        i+=1
        j=0
        
    letterPercs=[ ((letterSums[_]/sum(letterSums))*100) for _ in range(len(letterSums))]            #this calculates the relative 'popularity' of each letter (hint: e wins every time if you don't count space)
    letterPercs2=np.array(letterPercs) 
    np.set_printoptions(precision=0, suppress=True,linewidth=250)                           #attempt to get a square readable matrix by extending linewidth and reducing sig figs


    #print(frequencyMatrix) #raw undreable matrix can be printed if you want

    print("The relative percentages for letter pairings. Format is 1st letter row, second letter column, i.e. frequency of ab's is found at [2,1] 1st row, 2nd column.\nThe relative percentage of letter pairings beginning with that ",end='')
    print('letter is shown at the end of the row. q is being weird and i do not know why')
    print('    ',end='')                                                                                                #attempt to print slightly readably
    for c in string.ascii_lowercase:                                                                                    #top line above matrix labelling of a-z with best attempt at spacing
        print(c,'  ',end='')
    print(' _    %')
    i=0

    for row in relativePercentage:                                                                                      #print each row with a-z in front from ascii
        if k==26:        
            print('_',row,"%.2f" % letterPercs2[i])                                                                     #have to manually add a blank space label again
            i+=1        
        else:         
            print(string.ascii_lowercase[k],row,"%.2f" % letterPercs2[i])
            i+=1
            k+=1

    return(relativePercentage)
    input('any button to close')
    

frankenstein=matrixGen(f)
f.close()

def markovStory(matrix,startLetter,length):
    choiceList=[]
    story=[]        
    for c in string.ascii_lowercase:                                        #make an indexed list of the possible starting options including a blank space
        choiceList.append(c)
    choiceList.append(' ')

    startIndex=choiceList.index(startLetter)                                #change the starting letter to it's corresponding index, i.e a=0, b=1
    story.append(startLetter)                                               #start a list of the generated letter sequence
    nextLetter=rm.choices(choiceList,weights=matrix[startIndex])            #generate the next letter(as a LIST beware) from the choice list(a-z plus space) with weights depending on the row of the input matrix        
    story.append(nextLetter[0])                                             #and add it to the "story"
    
    for _ in range(length):                                                 #then create a loop where we do the same thing over and over again as many times as specified in the argument 'length'
        nextIndex=choiceList.index(nextLetter[0])                           #within the loop we need to de-listify the next letter each time because rm.choices returns a list
        nextLetter=rm.choices(choiceList,weights=matrix[nextIndex]) 
        story.append(nextLetter[0])
    collated="".join(story)
    return collated                                                         #return a markov chain of specified length based on the input probability matrix
    

story=markovStory(frankenstein,'t',200)
print(story)

















