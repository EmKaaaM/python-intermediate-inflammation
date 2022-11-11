from functools import reduce
from multiprocessing import Pool

def sum_of_squares(sequence):
    integers = [int(x) for x in sequence if x[0] != '#']
    squares = [x * x for x in integers]
    return reduce(lambda a, b: a + b, squares)

if __name__ == '__main__':
    with Pool(8) as p:
        print(p.map(sum_of_squares, ['1','2','3'])),
        #print(p.map(sum_of_squares, ['-1', '-2', '-3'])),
        print(p.map(sum_of_squares, ['1', '2', '#100', '3']))