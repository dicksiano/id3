from pre_processing import *
from id3 import *
import random

input = pre_process_ratings()

data = input[::1000]
test = input

tree = id3(data)
#printtree(tree)

"""
num_pos = 0
num_neg = 0
for t in test:
    b = t[-1]
    if b == 1:
        num_pos += 1
    else:
        num_neg += 1
"""
correct = 0
fp_id3, fn_id3, tp_id3, tn_id3 = 0, 0, 0, 0
fp_priori, fn_priori, tp_priori, tn_priori = 0, 0, 0, 0
fp_random, fn_random, tp_random, tn_random = 0, 0, 0, 0

for t in test:
    # Decision Tree
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
        if result == b: tp_id3 += 1
        else: fp_id3 += 1
    else:
        if result == b: tn_id3 += 1
        else: fn_id3 += 1

for t in test:
    b = t[-1]
    # Priori Classificator
    result = 0
    prob = random.uniform(0, 1)
    if prob < 0.5742: result = 1

    if result == 1:
        if result == b: tp_priori += 1
        else: fp_priori += 1
    else:
        if result == b: tn_priori += 1
        else: fn_priori += 1

for t in test:
    b = t[-1]
    # Classificator based on Decision Tree Distribution
    result = 0
    prob = random.uniform(0, 1)
    if prob < float(tp_id3+fp_id3)/len(test): result = 1

    if result == 1:
        if result == b: tp_random += 1
        else: fp_random += 1
    else:
        if result == b: tn_random += 1
        else: fn_random += 1

print(float(tp_id3)/len(test), float(tn_id3)/len(test), float(fp_id3)/len(test), float(fn_id3)/len(test), float(tp_id3+tn_id3)/len(test))
print(float(tp_priori)/len(test), float(tn_priori)/len(test), float(fp_priori)/len(test), float(fn_priori)/len(test), float(tp_priori+tn_priori)/len(test))
print(float(tp_random)/len(test), float(tn_random)/len(test), float(fp_random)/len(test), float(fn_random)/len(test), float(tp_random+tn_random)/len(test))
#print(float(num_neg)/len(test), float(num_pos)/len(test))
    