def make_test_dice(outcomes):
	#outcomes = list(outcomes)
	while True:
		for i in outcomes:
			yield i
			
dice = make_test_dice([1, 2, 3])

print(next(dice))
print(next(dice))
print(next(dice))
print(next(dice))