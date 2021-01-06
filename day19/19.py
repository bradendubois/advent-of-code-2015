from sys import stdin
from random import shuffle

l = stdin.read().split("\n\n")
molecule = l[1]

l = [x.split(" => ") for x in l[0].split("\n")]
reactions = {left: [] for left, right in l}

for left, right in l:
    reactions[left].append(right)

def all_reactions(m):

    molecules = set()

    for i, c in enumerate(molecule):

        pre = m[:i]
        post = m[i:]

        for r in reactions:
            if post.startswith(r):
                reacts = [pre + x + post[len(r):] for x in reactions[r]]
                molecules.update(reacts)

    return molecules


# Part One
print(len(all_reactions(molecule)))


individual_reactions = []
for fromm, to in reactions.items():
    individual_reactions.extend([(fromm, x) for x in to])

count = 0
m = molecule

while True:

    before = m

    if m == "e":
        print(count)
        break

    for reaction, result in individual_reactions:
        count += m.count(result)
        m = m.replace(result, reaction)

    if m == before:
        m = molecule
        count = 0

        shuffle(individual_reactions)
