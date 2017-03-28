import time
import os
"""
#print ('hello')
with open ("lotr_subs.srt", "r") as myfile:
    #data=myfile.readlines()

    data = myfile.read().replace("\r\n', '"," ")
    #print data[5]
    stuff = str(data)
    #s = stuff.split(' ')
    print stuff
    #print "hey"
    #print data
"""
def IsInt(s):
	try:
		int(s)
		return True
	except:
		ValueError
		return False

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



with open('lotr_subs.srt') as f:
	lines = [line.rstrip('\n\r') for line in open('lotr_subs.srt')]
	#print "hello"
	#time.sleep(2)
	#os.system('clear')
	#print "hey"
	#print lines
	#print lines[0]
	#print extract('00:01:23,393 --> 00:01:26,260')
	count = 0
	s = 'dummmy'
	timing = 'dummy'
	duration = 0.0
	#print lines
	#print IsInt(lines[5])
	#print lines[5]

	#This block of code is for setting the initial offset
	"""
	i = 0
	while (IsInt(lines[i]) == False):
		i = i+1

	offset = lines[i+1]
	ls = offset.split(' --> ')
	s1 = ls[0]
	ls1 = s1.split(':')
	#print ls1
	h1 = ls1[0]
	m1 = ls1[1]
	ms1 = ls1[2]
	ls3 = ms1.split(',')
	t1 = int(h1)*3600000 + int(m1)*60000 + int(ls3[0])*1000 + int(ls3[1])
	time.sleep(t1/1000.0)
	"""

	
	tin = []
	tout = []
	subtitles = []
	while count < len(lines):
		#print "inner"
		s = lines[count]
		if(IsInt(s)):
			count = count + 1
			timing = lines[count]
			extract(timing, tin, tout)
			subtitles.append('')
		while (lines[count] != ''and count < len(lines)):
			#print "innermost"
			#print count
			#print duration
			#print len(subtitles)
			count = count+1
			if count == len(lines):
				break
			subtitles[len(subtitles)-1] = subtitles[len(subtitles)-1] + '\n' + lines[count]
			#print lines[count]
		#time.sleep(duration/1000.0)
		#os.system('clear')
		#print count
		count = count+1
		if count == len(lines):
			break

	#for x in range(len(tin)):
	#	print str(tin[x]) + "   ----   " + str(tout[x])
	#	print tout[x]-tin[x]
	#	print '-----------------------------------------------------------------------------------------------'

	#print len(subtitles)
	#print len(tin)
	#print len(tout)
	time.sleep(tin[0]/100000.0)

	for i in range(len(subtitles)):
		print subtitles[i]
		time.sleep((tout[i]-tin[i])/100000.0)
		os.system('clear')
		if i == len(subtitles)-1:
			break
		time.sleep((tin[i+1]-tout[i])/100000.0)


		
		
		






