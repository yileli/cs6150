import numpy as np


timesteps = [4 * 10**4, 9 * 10**4, 16 * 10**4]
runs = 50  

def simulate_random_walk(t, runs):

    crossings = []
    for _ in range(runs):

        steps = np.random.choice([-1, 1], size=t)

        positions = np.cumsum(steps)

        zero_crossings = np.sum(np.diff(np.sign(positions)) != 0)
        crossings.append(zero_crossings)
    return np.mean(crossings)

results = {t: simulate_random_walk(t, runs) for t in timesteps}
print(results)