#-*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for line in sys.stdin:
	line=line.strip()
	word=line.split()
	for word in word:
		print('%s\t%s' % (word, 1))