'''
python program for getting the word count from the contents of a file using command line arguments.
Develpoed By: SREEVALSAN V
RegisterNumber: 23012962
'''
import sys
fp=open(sys.argv[1])
data=fp.read()
words=data.split(',')
print("no of words",len(words))