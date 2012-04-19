# -* - coding: UTF-8 -* -
#on python 2.7.1
#on windows
#by laoyang945 inspired by tikiet

import time
import sys
import re
import codecs
import string
import random
QUESTION_FONT= 'Palatino-Bold'
QUESTION_SIZE= '8'
PHONETIC_SYMBOL_FONT= 'Palatino-Bold'
PHONETIC_SYMBOL_SIZE= '4'
PHONETIC_SYMBOL_COLOR= 'Grey'
ANSWER_FONT= 'Palatino-Bold'
ANSWER_SIZE= '5'
def generate_question(questionText):
	return 'Q: <font face="'+ QUESTION_FONT +'" size="'+ QUESTION_SIZE +'">'+ questionText+'</font><br/>'

def generate_phonetic_symbol(phoneticText):
	oldstring=['7','9','5','A','B','C','E','F','I','J','N','Q','R','T','U','V','W','\\\\','^']
	newstring=['&#716;','&#716;','&#712;','&#230;', '&#593;','&#596;','&#601;','&#643;', '&#618;','&#650;','&#331;','&#652;','&#596;','&#240;','u','&#658;','&#952;','&#604;','&#609;']
	for k in range(0,len(oldstring)-1):
		phoneticText=phoneticText.replace(oldstring[k],newstring[k])
	return '<font face="'+PHONETIC_SYMBOL_FONT+'" size="' + PHONETIC_SYMBOL_SIZE+ '" color="'+PHONETIC_SYMBOL_COLOR + '">' +phoneticText+'</font>'+'\n'

def generate_answer(answerText):
	oldstring=['7','9','5','A','B','C','E','F','I','J','N','Q','R','T','U','V','W','\\\\','^']
	newstring=['&#716;','&#716;','&#712;','&#230;', '&#593;','&#596;','&#601;','&#643;', '&#618;','&#650;','&#331;','&#652;','&#596;','&#240;','u','&#658;','&#952;','&#604;','&#609;']
	for k in range(0,len(oldstring)-1):
		answerText=answerText.replace(oldstring[k],newstring[k])
	return 'A: <font face="'+ ANSWER_FONT +'" size="'+ ANSWER_SIZE +'">'+answerText.strip() +'</font>'+'\n\n' 

def main():
	word_file_path=raw_input('input the path of the word list,the file should be encoded in utf-8 and delimited by Tab:')
	word_file=codecs.open(word_file_path,'r','utf-8')
	output_file=codecs.open('sm-iOS-'+word_file_path,'w','utf-8')
	questionIndex=raw_input('which column is the question:')
	phoneticIndex=raw_input('which column is the phonetic symbol:')
	answerIndex=raw_input('which column is the answer:')
	randomFlag=raw_input('randomly generate?[y/n]:')
	if randomFlag=='n':
		for line in word_file:
			if line.strip()=="": continue
			questionText=line.split('\t')[string.atoi(questionIndex)-1]
			phoneticText=line.split('\t')[string.atoi(phoneticIndex)-1]
			answerText=line.split('\t')[string.atoi(answerIndex)-1]
			out_text=generate_question(questionText.encode('utf-8'))+generate_phonetic_symbol(phoneticText.encode('utf-8'))+generate_answer(answerText.encode('utf-8'))
			output_file.write(out_text.decode('utf-8'))
	else:
		lines=[]
		rawlines=word_file.readlines()
		cnt=len(rawlines)
		while(cnt>0):
			try:
				pos=random.randrange(0,cnt-1)
			except:
				pos=0
			lines.append(rawlines[pos])
			del rawlines[pos]
			cnt=len(rawlines)
		for line in lines:
			if line.strip()=="": continue
			questionText=line.split('\t')[string.atoi(questionIndex)-1]
			phoneticText=line.split('\t')[string.atoi(phoneticIndex)-1]
			answerText=line.split('\t')[string.atoi(answerIndex)-1]
			out_text=generate_question(questionText.encode('utf-8'))+generate_phonetic_symbol(phoneticText.encode('utf-8'))+generate_answer(answerText.encode('utf-8'))
			output_file.write(out_text.decode('utf-8'))
	raw_input('Done')
	word_file.close()
	output_file.close()

if __name__ == '__main__':
    main()
