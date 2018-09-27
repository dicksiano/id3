import math

def split_data(data, column, value):
    inclusion = [row for row in data if row[column] == value]
    exclusion = [row for row in data if not row[column] == value]

    return (inclusion, exclusion)

def class_counter(input):
    classes = {}
    for row in input:
        current = row[-1]
        if current not in classes: classes[current] = 0
        classes[current] += 1
    return classes

def entropy(input):
    classes, s = class_counter(input), 0.0
    for key in classes.keys():
        freq = float( classes[key] ) / len(input)
        s  = s - freq * math.log(freq, 2)
    return s

class node:
    def __init__(self, col=-1, value=None, results=None, trueBranch=None, falseBranch=None):
        self.col = col
        self.value = value
        self.results = results
        self.trueBranch = trueBranch
        self.falseBranch = falseBranch

def possible_values(input, col):
    column_values = {}
    for row in input:
        column_values[ row[col] ] = 1
    return column_values.keys()

def id3(data):
    if len(data) == 0: 
        return node()

    current_s = entropy(data)
    best_gain, best_criteria, best_set = 0.0, None, None

    for col in range(0, len(data[0][:-1])):
        column_values = possible_values(data, col)
        for val in column_values:
            incl, excl = split_data(data, col, val)

            if len(incl) > 0 and len(excl) > 0:
                freq = float(len(incl)) / len(data)
                gain = current_s - freq * entropy(incl) - (1-freq) * entropy(excl)

                if gain > best_gain:
                    best_gain, best_criteria, best_set = gain, (col, val), (incl, excl)
    if best_gain > 0:
        trueBranch, falseBranch = id3(best_set[0]), id3(best_set[1])            
        return node(col=best_criteria[0], value=best_criteria[1], trueBranch=trueBranch, falseBranch=falseBranch)
    return node(results = class_counter(data))

def predict(input, tree):
    if tree.results != None: return tree.results
            
    if input[tree.col] == tree.value: 
        return predict(input, tree.trueBranch)
    return predict(input, tree.falseBranch)

def printtree(tree,indent=' '):
    questions = ["Genero", "Idade", "Ocupação", "Categoria"]
    if tree.results != None:
        print( str(tree.results) )
    else:
        print( questions[tree.col] + ': '+str(tree.value)+'?')
 
        print( indent + 'T: ', end='')
        printtree(tree.trueBranch, indent + ' '),
        print( indent+'F: ', end='')
        printtree(tree.falseBranch,indent + ' ')

