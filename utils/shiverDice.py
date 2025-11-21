import random, re

skillDice = [
    ("GRIT",    "assets/SHIVER/GRIT.png"),
    ("WIT",     "assets/SHIVER/WIT.png"),
    ("SMARTS",  "assets/SHIVER/SMARTS.png"),
    ("HEART",   "assets/SHIVER/HEART.png"),
    ("STRANGE", "assets/SHIVER/STRANGE.png"),
    ("LUCK",    "assets/SHIVER/LUCK.png")
]

talentDice = [
    ("STRANGE x2", "assets/SHIVER/STRANGE x2.png"),
    ("STRANGE",    "assets/SHIVER/STRANGE.png"),
    ("STRANGE",    "assets/SHIVER/STRANGE.png"),
    ("TALENT",     "assets/SHIVER/TALENT.png"),
    ("TALENT",     "assets/SHIVER/TALENT.png"),
    ("TALENT",     "assets/SHIVER/TALENT.png"),
    ("TALENT x2",  "assets/SHIVER/TALENT x2.png"),
    ("TALENT x2",  "assets/SHIVER/TALENT x2.png")
]

def rollSkill():
    return random.choice(skillDice)

def rollTalent():
    return random.choice(talentDice)

def rollShiver (expression: str):
    skillDiceCount = 0
    talentDiceCount = 0
    modifierTier = None
    modifierType = None

    parts = expression.lower().split()

    for part in parts:
        match = re.match(r"(\d+)?(sd|td)", part)
        if match:        
            count = int(match.group(1)) if match.group(1) else 1
            diceType = match.group(2)

            if diceType == "sd":
                skillDiceCount += count
            elif diceType == "td":
                talentDiceCount += count
            continue

        if part in ["min", "maj"]:
            modifierTier = part
            continue

        if part in ["dis", "adv"]:
            modifierType = part
            continue

        return None
    
    if modifierTier and modifierType:
        if modifierTier == "min":
            if modifierType == "adv":
                skillDiceCount += 1
            elif modifierType == "dis" and skillDiceCount > 0:
                skillDiceCount -= 1
        elif modifierTier == "maj":
            if modifierType == "adv":
                talentDiceCount += 1
            elif modifierType == "dis" and talentDiceCount > 0:
                talentDiceCount -= 1

    skillResults = [rollSkill() for die in range(skillDiceCount)]
    talentResults = [rollTalent() for die in range(talentDiceCount)]

    return skillResults + talentResults