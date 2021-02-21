import multiprocessing
import time
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count, Process


def square(n):
    time.sleep(2)

    return n * n


def main():
    start = timer()

    print(f'starting computations on {cpu_count()} cores')

    values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16)

    with Pool() as pool:
        res = pool.map(square, values)
        print(res)

    end = timer()
    print(f'elapsed time: {end - start}')


if __name__ == '__main__':
    main()


def example_grid_search():
    from sklearn import svm, datasets

    from sklearn.model_selection import GridSearchCV
    iris = datasets.load_iris()
    parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}
    svc = svm.SVC()
    clf = GridSearchCV(svc, parameters)
    clf.fit(iris.data, iris.target)

    GridSearchCV(estimator=svc,
                 param_grid={'C': [1, 10], 'kernel': ('linear', 'rbf')},
                 n_jobs=-1)  # Tell to use all processors

start = timer()

print(f'starting computations on {cpu_count()} cores')

values = (1, 2, 3, 4, 5, 6, 7, 8)

with Pool() as pool:
    res = pool.map(square, values)
    print(res)

end = timer()
print(f'elapsed time: {end - start}')



start = timer()

print(f'starting computations on {cpu_count()} cores')

values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

with Pool() as pool:
    res = pool.map(square, values)
    print(res)

end = timer()
print(f'elapsed time: {end - start}')

