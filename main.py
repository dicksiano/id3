from pre_processing import *
from id3 import *

input = pre_process_ratings()

data = input[::100]
test = input

tree = id3(data)
#printtree(tree)

correct = 0
for t in test:
    a = predict(t[:-1],tree)
    b = t[-1]
    correct += int(max(a, key=a.get) == b)

print(float(correct)/len(test))
    