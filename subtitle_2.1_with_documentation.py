"""
PROBLEM
--------

To write a program that reads out subtitles from a .srt file and print them on the terminal window at the correct time for the specific duration

GENEAL COMMENTS
---------------

Language used: Python
Reason: I've been wanting to learn python, so I've used python to implement this project. 
	    Another reason is that python has many useful and easy to use functions for string manipulations in python

Library functions: Library functions os (to clear the screen) and time (for timing the display and erasing of the subtitles) have been used
Functions: Detailed definitions of the functions I have written are given just above the functions in the code

Timing the display: To time the display, I thought up of two methods, 
one is to constantly use the system clock as a reference (after recording it in the beggining)
another is to use the previous display time and the difference as reference
although the first one may give a slightly more accurate result (if we consider the time taken up by the computer to run the code) but the secong method seemed more natural so I have used the second method

Tip: if you want the subtitles to be displayed faster, replace the 1000.0 in the last block of the code with another bigger double

LIMITATIONS
-----------

The code is not designed to deal with more than two subtitles overlapping. i.e. it will not work if three different subtitles have a clash in their timings. However that can be dealt with adding a few more lines of code somilar to the block that currently deals with overlapping
When two subtitles are overlapping, the first one shout 'exit' before the second one. This too can be fixed by adding more conditonal statements

EXECUTION
---------

To execute this code, go to the last bock of code "with open('lotr_subs.srt') as f:  ....." and replace lotr_subs.srt with any .srt file of your choice in both the places and then run the code on terminal

VERSION - 2.1
-------------

Version 1.x used a different logic and had a logical flaw in the program
Version 2.0 is pretty similar, but is inacurate when two subtitles overlap (in ttime)
Version 2.1 This is the current version which has been thoroughly tested. It can also show overlapping phrases similtaneously
"""

import time
import os

"""
This is function that returns boolean based on whether the parameter (of unknown datatype) is an integer
It uses a try - catch block to implement this 
"""
def IsInt(s):
	try:
		int(s)
		return True
	except:
		ValueError
		return False

"""
This function basically takes a string of this form "00:01:28,665 --> 00:01:31,156" and puts the data (time) into the two arrays (tin and tout) in milliseconds
It mainly uses string manipulation to get this data
"""

def extract(s,tin, tout):
	ls = s.split(' --> ')
	s1 = ls[0]
	s2 = ls[1]
	ls1 = s1.split(':')
	ls2 = s2.split(':')
	h1 = ls1[0]
	h2 = ls2[0]
	m1 = ls1[1]
	m2 = ls2[1]
	ms1 = ls1[2]
	ms2 = ls2[2]
	ls3 = ms1.split(',')
	ls4 = ms2.split(',')
	t1 = int(h1)*3600000 + int(m1)*60000 + int(ls3[0])*1000 + int(ls3[1])
	t2 = int(h2)*3600000 + int(m2)*60000 + int(ls4[0])*1000 + int(ls4[1])
	tin.append(t1)
	tout.append(t2)


"""
I'm not too clear about how the first two lines work, but it basically directly converts the .srt file into a list!(saving many lines of code) 
This block contains code for displaying the .srt file as required in the problem statement
"""
with open('lotr_subs.srt') as f:
	lines = [line.rstrip('\n\r') for line in open('lotr_subs.srt')]
	
	count = 0
	s = 'dummmy'
	timing = 'dummy'
	duration = 0.0
	
	tin = []
	tout = []
	subtitles = []

	"""
	This block extracts all the necessary data from the list into three arrays tin, tout, subtitles (the names are self explanatory)
	"""
	while count < len(lines):
		
		s = lines[count]
		if(IsInt(s)):
			count = count + 1
			timing = lines[count]
			extract(timing, tin, tout)
			subtitles.append('')

		while (lines[count] != ''and count < len(lines)):
			
			count = count+1
			if count == len(lines):
				break
			subtitles[len(subtitles)-1] = subtitles[len(subtitles)-1] + '\n' + lines[count]
			
		count = count+1
		if count == len(lines):
			break

	#The initial time delay before the first subtitle
	time.sleep(tin[0]/1000.0)

	for i in range(len(subtitles)):
		print subtitles[i]
		#Code for dealing with overlapping
		if i<len(subtitles)-1 and tin[i+1] < tout[i]:
			time.sleep((tin[i+1]-tin[i])/1000.0)
			print subtitles[i+1]
			time.sleep((tout[i] - tin[i+1])/1000.0)
			os.system('clear')
			print subtitles[i+1]
			time.sleep((tout[i+1]-tout[1])/1000.0)
			os.system('clear')
			i = i+1

		#Code in case there are no overlaping subtitles
		else:
			time.sleep((tout[i]-tin[i])/1000.0)
			os.system('clear')
		if i == len(subtitles)-1:
			break
		time.sleep((tin[i+1]-tout[i])/1000.0)


		
		
		






