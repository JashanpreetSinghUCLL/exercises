from movie import *

def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return {e for e in xs if e in ys}

print(common_elements([1, 2, 5], [1, 3, 5]))