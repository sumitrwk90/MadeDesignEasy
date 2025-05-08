
import ray

@ray.remote(num_cpus=2)  # optional: assign CPU use
def train_model(config):
    # training logic here
    return f"Trained with {config}"

"""
Each task gets 2 CPUs.

You can run 5 tasks in parallel on 10 CPUs.

You don't have to manually set the CPU count. Just check ray.cluster_resources() to see how many CPUs Ray can use, 
then write your code accordingly — by assigning the right number of CPUs per task to fully utilize your system without overload.

"""