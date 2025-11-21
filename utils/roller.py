import random, re

def rollDice(expression: str):
    match = re.match(r"(\d+)d(\d+)(.*)", expression)
    if not match:
        return None
    
    count = int(match.group(1))
    sides = int(match.group(2))
    modifier = match.group(3)

    rolls = [random.randint(1, sides) for c in range(count)]
    total = sum(rolls)

    if modifier:
        if "+" in modifier:
            mod = int(modifier.replace("+", ""))
            total += mod
        elif "-" in modifier:
            mod = int(modifier.replace("-", ""))
            total -= mod

    return rolls, total