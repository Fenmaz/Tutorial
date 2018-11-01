from collections import Counter	

fingers = {"c": [2,3,4,7,8,9,10], "d": [2,3,4,7,8,9], "e": [2,3,4,7,8], "f": [2,3,4,7], "g": [2,3,4],
			"a": [2,3], "b": [2], "C": [3], "D": [1,2,3,4,7,8,9], "E": [1,2,3,4,7,8], "F": [1,2,3,4,7],
			"G": [1,2,3,4], "A":[1,2,3], "B": [1,2]}
			

num_cases = int(input())

for _ in range(num_cases):
	pressed = [False] * 11
	count = [0] * 11
	notes = input()
	for note in notes:
		new_pressed = [False] * 11
		for finger in fingers[note]:
			new_pressed[finger] = True
			if not pressed[finger]:
				count[finger] += 1
		pressed = new_pressed
	
	for i in range(1, 11):
		print(count[i], end=" ")
