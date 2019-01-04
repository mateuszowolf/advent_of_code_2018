
input_path = 'input.txt'

initial_state = ""
transforms = {}

with open(input_path ,'r') as f:
    initial_state = f.readline().split(':')[1].strip()
    for line in f.readlines():
        if '=>' in line:
            env, result = line.split('=>')
            env = env.strip()
            result = result.strip()
            transforms[env] = result

pots = {i: v for i,v in enumerate(initial_state)}


def print_generation(pots):
    generation = "".join([pots[i] for i in sorted(pots.keys())])
    print(generation)



def calculate_generation(pots):
    new_generation = {}
    new_pots = []
    for i in pots.keys():
        surroundings, new_pots_for_i = get_surroundings(pots, i)
        new_generation[i] = transforms.get(surroundings, '.')
        if new_pots_for_i:
            new_pots.extend(new_pots_for_i)

    if new_pots:
        for i in set(new_pots):
            surroundings, _ = get_surroundings(pots, i)
            new_generation[i] = transforms.get(surroundings, '.')
    return new_generation




def get_surroundings(pots, i):
    surroundings = ""
    new_pots = []
    for x in [i-2, i-1, i, i+1, i+2]:
        status, new = get_pot(pots, x)
        surroundings += status
        if new:
            new_pots.append(x)
    return surroundings, new_pots

def get_pot(pots, i):
    new = False
    try:
        status = pots[i]
    except KeyError:
        status = '.'
        new = True
    # print((i, status, new))
    return status, new

print_generation(pots)
prev_sum = sum([k for k,v in pots.items() if v =='#'])
for i in range(3000):
    pots = calculate_generation(pots)
    cur_sum = sum([k for k, v in pots.items() if v == '#'])
    print(f"{i} {cur_sum} {cur_sum-prev_sum}")
    prev_sum = cur_sum

print(sum([k for k,v in pots.items() if v =='#']))