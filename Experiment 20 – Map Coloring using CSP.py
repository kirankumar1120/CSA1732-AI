
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def solve(assignment):
    if len(assignment) == len(regions):
        return assignment

    region = next(r for r in regions if r not in assignment)

    for color in colors:
        if all(assignment.get(n) != color
               for n in neighbors[region]):
            assignment[region] = color

            result = solve(assignment)
            if result:
                return result

            del assignment[region]

    return None

result = solve({})

if result:
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution found")
