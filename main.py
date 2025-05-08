
import ray
from train import train_model

ray.init()

configs = ['cfg1', 'cfg2', 'cfg3']

# Launch multiple training tasks
futures = [train_model.remote(cfg) for cfg in configs]

# Gather results
results = ray.get(futures)

print(results)
