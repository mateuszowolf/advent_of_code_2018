
puzzle_input = 51589

def main_p1():
    recipes = [3, 7]
    elf_1_ind = 0
    elf_2_ind = 1

    while len(recipes) <= puzzle_input + 10:
        combined = recipes[elf_1_ind] + recipes[elf_2_ind]
        if combined > 9:
            recipe_1 = combined // 10
            recipe_2 = combined % 10
            recipes.extend([recipe_1, recipe_2])
        else:
            recipes.append(combined)
        elf_1_ind = get_new_index(elf_1_ind, recipes)
        elf_2_ind = get_new_index(elf_2_ind, recipes)

    print("".join([str(c) for c in recipes[puzzle_input: puzzle_input+10]]))


def main_p2():
    tgt = "360781"
    recipes = [3, 7]
    elf_1_ind = 0
    elf_2_ind = 1
    recipes_str = "".join([str(c) for c in recipes])

    while not recipes_str.endswith(tgt):
        combined = recipes[elf_1_ind] + recipes[elf_2_ind]
        if combined > 9:
            recipe_1 = combined // 10
            recipe_2 = combined % 10
            recipes.extend([recipe_1, recipe_2])
        else:
            recipes.append(combined)
        elf_1_ind = get_new_index(elf_1_ind, recipes)
        elf_2_ind = get_new_index(elf_2_ind, recipes)
        recipes_str = "".join([str(c) for c in recipes[-15:]])
    print(len(recipes_str.replace(tgt, "")))



def get_new_index(current_index, recipes):
    score = recipes[current_index]
    new_index = 1 + score + current_index
    if new_index > len(recipes) - 1:
        new_index = new_index % len(recipes)
    return new_index

if __name__ == '__main__':
    # main_p1()
    main_p2()