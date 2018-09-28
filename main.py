from pre_processing import *
from id3 import *

input = pre_process_ratings()

data = input[::1000]
test = input

tree = id3(data)
#printtree(tree)

correct = 0
fp = 0
fn = 0
tp = 0
tn = 0
for t in test:
    a = predict(t[:-1],tree)
    b = t[-1]

    neg = pos = 0
    if 0 in a:
        neg = a[0]
    if 1 in a:
        posit = a[1]

    result = 0
    if posit >= neg: result = 1

    if result == 1:
        if result == b: tp += 1
        else: fp += 1
    else:
        if result == b: tn += 1
        else: fn += 1

print(float(tp)/len(test), float(tn)/len(test), float(fp)/len(test), float(fn)/len(test))
    