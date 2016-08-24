"""
Alex Ring
Alri7215
alri7215@colorado.edu
Week 1
"""

"""
Create a function that prints out 10 lines, 100 letters per line, with given probabilities, first letter always "I"
Probabilities
--------------
 * P(_ | I) = 1
 * P(a | _) = 0.5
 * P(l | _) = 0.5
 * P(m | a) = 0.4
 * P(_ | m) = 0.8
 * P(! | m) = 0.2
 * P(l | a) = 0.6
 * P(i | l) = 1
 * P(v | i) = 0.95
 * P(e | v) = 1
 * P(n | i) = 0.05
 * P(e | n) = 1
 * P(! | e) = 1
 * P(_ | !) = 0.7
 * P(I | !) = 0.2
 * P(! | !) = 0.1
"""
import random

for i in range(10): #10 Lines
	x = "I"
	for j in range(99): #100 Letters already have first
		
		rand = random.randint(1,100) #Rand
		
		#Probabilities
		if x[j] == "I":
			x = x + "_"
		elif x[j] == "_":
			if rand > 50:
				x = x + "a"
			else:
				x = x + "l"
		elif x[j] == "a":
			if rand > 40:
				x = x + "l"
			else:
				x = x + "m"
		elif x[j] == "m":
			if rand > 20:
				x = x + "!"
			else:
				x = x + "_"
		elif x[j] == "l":
			x = x + "i"
		elif x[j] == "v":
			x = x + "e"
		elif x[j] == "i":
			if rand > 5:
				x = x + "v"
			else:
				x = x + "n"
		elif x[j] == "n":
			x = x + "e"
		elif x[j] == "e":
			x = x + "!"
		else:
			if rand < 11:
				x = x + "!"
			elif rand > 30:
				x = x + "_"
			else:
				x = x + "I"
	print(x)
