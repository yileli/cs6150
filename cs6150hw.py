import numpy as np


population_size = 1000000
proportions = {'+1': 0.35, '-1': 0.40, '0': 0.25}


sample_sizes = [10, 120, 250]


n_experiments = 200


def simulate_majority(sample_size, n_experiments):
    majority_count = 0
    for _ in range(n_experiments):

        sample = np.random.choice(
            ['+1', '-1', '0'],
            size=sample_size,
            p=[proportions['+1'], proportions['-1'], proportions['0']]
        )

        counts = {vote: np.sum(sample == vote) for vote in ['+1', '-1', '0']}

        if counts['-1'] > counts['+1'] and counts['-1'] > counts['0']:
            majority_count += 1

    return majority_count / n_experiments

def func1():
    probabilities = {size: simulate_majority(size, n_experiments) for size in sample_sizes}
    print(probabilities)

def func2():
    probabilities = 0.0
    size=250
    while (probabilities<0.9):
        probabilities = simulate_majority(size, n_experiments)
        size+=1
        print(probabilities,size)
