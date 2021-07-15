#-*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


current_word=None
current_count=0
word=None
print("reducer\n\n")
for line in sys.stdin:
    line=line.strip()

    word, count=line.split('\t', 1)

    try:
        count=int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count+=count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count=count
        current_word=word

if current_word==word:
    print('%s\t%s' % (current_word, current_count))