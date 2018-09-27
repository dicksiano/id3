from pre_processing import *
from id3 import *

input = pre_process_ratings()

data = input[::10]

tree = id3(data)
printtree(tree)