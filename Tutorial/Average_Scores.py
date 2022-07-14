scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
average = 0
for obj in scores :
	sum += obj;
average = sum / len(scores)
print(average)