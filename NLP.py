''' program to take input from user and print the phrase after calculating
    the frequency of words and their grammer related information'''



# -----------------------import area-------------------------

#natural language toolkit package provided by mit 
import nltk
from nltk.book import *

#package used for numerical computations in python
#(numpy- numerical python )
import numpy

#------------------------import area ends---------------------


#function to tokenize the entered phrase

def tokenizing():
    check =False
    while(check == False):
        print("****************")
        print(" Enter Your  Choice:")
        print("****************")
        print("1.Enter Text For Analysis")
        print("2.Find Frequency Of Words")
        print("3.Lexical Distribution")
        print("4.Exit")
        print("****************")
        x = int(input())
        if  (x ==1):
            enterText()
        elif (x==2):
            frequency()
        elif(x==3):
            lexicalDistribution()
        else:
            check = True


#function to get user input in text
#and write it on a file named a.txt

def enterText():
    s = input("enter your text:"+"\n")
    f = open("a.txt","r+")
    f.write(s)
    f.close()


#function to create the distribution table regarding
#frequency of letters in a phrase

def frequency():
    f = open("a.txt","r+")
    x = f.read()
    token = nltk.word_tokenize(x)
    freq= FreqDist(token)
    freq.tabulate()



#function that prints the lexical distribution
#table of the tokenized words

def lexicalDistribution():
    f = open ("a.txt","r+")
    x = f.read()
    text = nltk.word_tokenize(x)
    x = nltk.pos_tag(text)
    print(x)

