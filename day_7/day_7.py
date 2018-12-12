from collections import defaultdict
import re
from datetime import datetime
import string
startTime = datetime.now()
steps = defaultdict(set)
step_lengths = {letter: 60+i for i, letter in enumerate(string.ascii_uppercase, start=1)}


with open('input.txt') as f:
    for line in f.readlines():
        dep, step = [l.strip() for l in re.findall('\W[A-Z]', line.strip())]
        if dep not in steps:
            _ = steps[dep]
        steps[step].add(dep)
    print(steps)

def remove_from_deps(item):
    for k, v in steps.items():
        try:
            v.remove(item)
        except KeyError:
            pass


class Worker(object):
    def __init__(self, name):
        self.name = name
        self.time_remaining = 0
        self.task = None
        self.idle = True

    @property
    def is_idle(self):
        return self.idle

    def assign_task(self, task):
        if self.task:
            raise Exception('Already have a task')
        else:
            self.task = task
            self.time_remaining = step_lengths[task]
            self.idle = False
            return True

    def tick(self):
        if self.time_remaining:
            self.time_remaining -= 1
        if self.time_remaining == 0:
            v = self.task
            self.task = None
            self.idle = True
            return v

# order = []
# while True:
#     to_process = sorted([k for k,v in steps.items() if len(v) == 0])
#     try:
#         k = to_process.pop(0)
#         del steps[k]
#         order.append(k)
#         remove_from_deps(k)
#     except:
#         break
#
# print("".join(order))
# #Python 3:
no_workers = 5
workers = [Worker(i) for i in range(1, no_workers+1)]
print(len(workers))




seconds = -1 # account for incrementing seconds before anything is assigned
completion_order = []
working_tasks = set()
while steps:
    completed = []
    seconds += 1
    # print(workers[0].task)
    for worker in workers:
        t = worker.tick()
        if t:
            completed.append(t)
            remove_from_deps(t)
            del steps[t]
    if completed:
        _ = [remove_from_deps(t) for t in completed]
        completion_order.extend(completed)
    to_process = sorted([k for k, v in steps.items() if len(v) == 0 and k not in working_tasks])
    idle_workers = [w for w in workers if w.is_idle]
    [(w.assign_task(tp), working_tasks.add(tp)) for tp, w in zip(to_process, idle_workers)]
    assigned_tasks = [w.task for w in workers if w.task in steps]


print("".join(completion_order))
print(seconds)
print(datetime.now() - startTime)