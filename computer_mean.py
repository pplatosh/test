import sys
sum = 0.0
counter = 0
for line in sys.stdin:
linesrtipped = line.strip()
line_float = float(linestripped)
sum = sum +line_float
counter = counter+1
mean = sum/counter
print(mean)

