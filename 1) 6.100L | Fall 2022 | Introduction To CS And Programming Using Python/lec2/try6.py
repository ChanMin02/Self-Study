"""

 What does this code print with
 y = 2
 y = 20
 y = 11
 What if if x <= y: becomes elif x <= y: ?

answer = ''
x = 11
if x == y:
answer = answer + 'M'
if x >= y:
answer = answer + 'i'
else:
answer = answer + 'T'
print(answer)

"""

def func(y):
	
	answer = ""
	
	x = 11
	
	if x == y:
		answer = answer + "M"
	
	if x >= y :
		answer = answer + 'i'
	
	else :
		answer = answer + 'T'
		
	print(answer)
	
def func2(y):
	
	answer = ""
	
	x = 11
	
	if x == y:
		answer = answer + "M"
	
	elif x >= y :
		answer = answer + 'i'
	
	else :
		answer = answer + 'T'
		
	print(answer)

print(func(2))
print(func(20))
print(func(11))

print("seperate")

print(func2(2))
print(func2(20))
print(func2(11))