import urllib
from bs4 import BeautifulSoup
import requests

address = 'https://google.com/search?q='
# Default Google search address start
file = open( "OCR.txt", "rt" )
# Open text document that contains the question
word = file.read()
file.close()

myList = [item for item in word.split('\n')]
newString = ' '.join(myList)
# The question is on multiple lines so this joins them together with proper spacing

qstr = urllib.parse.quote_plus(newString)
# Encode the string

newWord = address + qstr
# Combine the base and the encoded query

response = requests.get(newWord)

answers = open("ocr2.txt", "rt")

ansTable = answers.read()
answers.close()

ans = ansTable.splitlines()

ans1 = str(ans[0].lower())
ans2 = str(ans[2].lower())
ans3 = str(ans[4].lower())

ans1Score = 0
ans2Score = 0
ans3Score = 0

soup = BeautifulSoup(response.text, 'lxml')
for g in soup.find_all(class_='g'):

    webBlock = str(g).lower()

    ans1Tally = webBlock.count(ans1)
    ans2Tally = webBlock.count(ans2)
    ans3Tally = webBlock.count(ans3)

    if 	webBlock.find(ans1)!=-1:

        ans1Score += ans1Tally

    if webBlock.find(ans2)!=-1:

        ans2Score += ans2Tally

    if webBlock.find(ans3)!=-1:

        ans3Score += ans3Tally

print(' ')
print("Question: " + newString)
print('-----')
print(ans1.capitalize()+": "+str(ans1Score))
print(ans2.capitalize()+": "+str(ans2Score))
print(ans3.capitalize()+": "+str(ans3Score))
print('-----')

# print(' ')
# print(ans1.capitalize()+": "+str(ans1Score))
# print(ans2.capitalize()+": "+str(ans2Score))
# print(ans3.capitalize()+": "+str(ans3Score))

# with open("Results.txt", "w") as results:
#     results.write(newString + '\n\n')
#     results.write(ans1.capitalize()+": "+str(ans1Score)+'\n')
#     results.write(ans2.capitalize()+": "+str(ans2Score)+'\n')
#     results.write(ans3.capitalize()+": "+str(ans3Score))
#
# with open("Game.txt", "a") as results:
#     results.write('\n\n'+newString + '\n\n')
#     results.write(ans1.capitalize()+": "+str(ans1Score)+'\n')
#     results.write(ans2.capitalize()+": "+str(ans2Score)+'\n')
#     results.write(ans3.capitalize()+": "+str(ans3Score))

#print(webBlock)
