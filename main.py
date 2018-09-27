from pre_processing import *
from id3 import *

data = pre_process_ratings()
tree = id3(data)
print(tree)