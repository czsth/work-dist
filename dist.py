import random
import numpy as np
import json

# params: a 2-dim list as range, a list for members' names, a number seed for randomizing
# returns: a dictionary with key as member, and a list of task indices as value
def dist(task_range, group_members, seed):
    random.seed(seed)

    l, r = task_range
    task_indices = list(range(l, r + 1))
    random.shuffle(task_indices)

    total_tasks = len(task_indices)
    total_members = len(group_members)
    tasks_at_least = total_tasks // total_members
    bad_luck_count = total_tasks % total_members
    personal_task_count = [tasks_at_least + 1] * bad_luck_count + [tasks_at_least] * (total_members - bad_luck_count)
    random.shuffle(personal_task_count)
    personal_task_ranges = [0] + np.cumsum(personal_task_count).tolist()

    task_dist = {
        member: task_indices[personal_task_ranges[i]:personal_task_ranges[i + 1]]
        for i, member in enumerate(group_members)
    }

    return task_dist

with open('config.json') as f:
    data = json.load(f)

members = data['members']
task_range = data['task_range']
seed = data['seed']

print(dist(task_range, members, seed))
