def dataset(file):
    lines = open(file, encoding="ISO-8859-1").readlines()
    return [line.split("::") for line in lines]

def pre_process_movies():
    dict = {}
    for line in dataset('movies.dat'):
        dict[ int(line[0]) ] = line[2][:-1]
    return dict

def pre_process_users():
    dict = {}
    for line in dataset('users.dat'):
        dict[ int(line[0]) ] = [line[1], line[2], line[3]]
    return dict

def pre_process_ratings():
    movies, users, res = pre_process_movies(), pre_process_users(), []

    for line in dataset('ratings.dat'):
        tmp = users[ int(line[0]) ]
        rate = 1 if int( line[2] ) > 3 else 0
        res.append([tmp[0], tmp[1], tmp[2], movies[ int(line[1]) ], rate])

    return res