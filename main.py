from dataclasses import dataclass
import random, os, time, math, phb


@dataclass
class Character:
    Name: str
    Race: str
    Class: str
    Stats: list
    Hitpoints: int
    Abilities: list
    Skills: list
    Allignment: str
    Background: str
    Feats: list
    Level: int
    Proficient: list
    Subclass: str


def construct():
    character = Character(
        "",
        "",
        "",
        [],
        0,
        [],
        [],
        "",
        "",
        [],
        0,
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "",
    )
    set_race(character)
    set_name(character)
    set_class(character)
    race_improvement(allocate_stats(), character.Race, character)
    set_background(character)

    proficient(
        character.Class,
        number_of_skills(character.Class),
        character,
        background_data(character, character.Background),
    )
    set_alignment(character)
    if character.Level == 0:
        level(character)
    # set_modifiers(character)

    return character


def set_class(cha) -> str:
    command = "bananarama"
    while command not in phb.classes.keys():
        command = input(phb.cLass).title()
        if command.isdigit():
            command = int(command)
        os.system("clear")
    cha.Class = phb.classes[command]


# ------allows a user to chose a class from a list------#


def set_race(cha) -> str:
    command = "bananarama"
    while command not in phb.races.keys():
        command = input(phb.raCe)
        if command.isdigit():
            command = int(command)
        os.system("clear")

    cha.Race = phb.races[command]


# ------allows the user to chose a race from a list------#


def set_name(cha):
    name = input("Please choose a name: ").title()
    os.system("clear")
    cha.Name = name


# ---------function to set character's name_________#


def race_improvement(newStats, race, cha):
    stat = []
    for i in range(len(newStats)):
        stat.append(newStats[i] + phb.raceBonus[race][i])
    cha.Stats = stat


# --function to add the racial bonuses--#


def asi(cha):
    asi = 2
    while asi != 0:
        for i in range(6):
            print(phb.mod_name[i], cha.Stats[i])
        command = input(f"You have {asi} points. Where would you like to put them?\n>")
        os.system("clear")
        for i in range(6):
            if command == phb.options[i]:
                cha.Stats[i] += 1
                asi -= 1


# ------Increases the user's ability scores by a total of 2______#


def subclass(cha):
    command = "bananarama"
    while command not in phb.subclasses[cha.Class].keys():
        print("Pick a Subclass")
        for i in phb.subclasses[cha.Class].keys():
            print(f"{i}: {phb.subclasses[cha.Class][i]}")
        command = input()
        if command.isdigit():
            command = int(command)
        os.system("clear")
    cha.Subclass = phb.subclasses[cha.Class][command]


def level(cha):
    for i in phb.levelup[cha.Class][cha.Level]:
        if i == "Ability Score Improvement":
            asi(cha)
        elif i == "Subclass":
            subclass(cha)
        else:
            if type(i) == int:
                for j in phb.subclass_features[cha.Subclass][i]:
                    cha.Abilities.append(j)
            else:
                cha.Abilities.append(i)
    cha.Level += 1
    set_hit_points(cha)


def roll_dice(amount, dx):
    result = []
    for i in range(amount):
        result.append(random.randint(1, dx))
    return result


# ---function that rolls dice---#


def allocate_stats():
    stats = [0, 0, 0, 0, 0, 0]
    orderedStats = [0, 0, 0, 0, 0, 0]
    num = 0
    count = 0

    for i in range(6):
        stat = roll_dice(4, 6)
        stat.sort()
        stats[i] = stat[1] + stat[2] + stat[3]

    while len(stats) > 0:
        print(stats)
        try:
            num = int(input(f"Select a score for your {phb.options[count]} stat: "))
        except:
            print("Please chose from the available rolls")

        if num in stats:
            orderedStats[count] = num
            stats.remove(num)
            count = count + 1
            os.system("clear")
        else:
            os.system("clear")
            print("Please chose from the available rolls")
    return orderedStats


# ------function to organize the given stats in the order of the user's chosing-------#


def proficient(Class, x, cha, Chosen_skills):
    user = ""
    # skills = []
    index = 1
    for i in range(x):
        for i in phb.proficiency_options[Class]:
            if i not in Chosen_skills:
                print(f"{index}: {phb.skill_names[i]}")
                index += 1
        user = input("Select an ability: ")
        while not user.isdigit():
            print("Please try again: ")
            user = input("Select an ability: ")
        while int(user) - 1 not in range(len(phb.proficiency_options[Class])):
            print("Please try again: ")
            user = input("Select an ability: ")
        user = int(user) - 1
        cha.Proficient[user] += 1
        cha.Skills.append(phb.skill_names[phb.proficiency_options[Class][user]])
        Chosen_skills.append(phb.proficiency_options[Class][user])
        phb.proficiency_options[Class].remove(phb.proficiency_options[Class][user])
        os.system("clear")
        index = 1


# -------function to allow the user to select which skills to be proficient in------#
# def addingmodifiers2skills(cha):
#   sasquatch = ""
#   for i in range(len(phb.proficiency_options)):
#     sasquatch.append(
#       modifiers(cha)[phb.skills[i]] + cha.Proficient[i] * set_proficiency(cha))
#   return sasquatch


def saving_throw_option(Class):
    if Class in ["Barbarian", "Fighter"]:
        savingthrows = ["Strength", "Constitution"]
    if Class == "Bard":
        savingthrows = ["Dexterity", "Charisma"]
    if Class in ["Cleric", "Paladin", "Warlock"]:
        savingthrows = ["Wisdom", "Charisma"]
    if Class in ["Druid", "Wizard"]:
        savingthrows = ["Intelligence", "Wisdom"]
    if Class in ["Monk", "Ranger"]:
        savingthrows = ["Strength", "Dexterity"]
    if Class == "Rogue":
        savingthrows = ["Dexterity", "Intelligence"]
    if Class == "Sorcerer":
        savingthrows = ["Constitution", "Charisma"]
    return savingthrows


def savingthrow(cha):
    strsave = modifiers(cha)[0]
    dexsave = modifiers(cha)[1]
    consave = modifiers(cha)[2]
    intsave = modifiers(cha)[3]
    wissave = modifiers(cha)[4]
    chasave = modifiers(cha)[5]
    saves = {
        "Strength": strsave,
        "Dexterity": dexsave,
        "Constitution": consave,
        "Intelligence": intsave,
        "Wisdom": wissave,
        "Charisma": chasave,
    }

    for i in saving_throw_option(cha.Class):
        saves[i] += set_proficiency(cha)
    return saves


# -- 2 functions that select what your saving throws and apply stats--#


def modifiers(cha):
    Modifiers = []
    for i in cha.Stats:
        Modifiers.append((i - 10) // 2)
    return Modifiers


# ---function that does math for the ability modifiers---#


def set_hit_points(cha):
    if cha.Hitpoints == 0:
        cha.Hitpoints = phb.Hit_Dice[cha.Class]
    else:
        cha.Hitpoints += random.randint(1, phb.Hit_Dice[cha.Class])


# --function that calculates health--#


def set_movement_speed(cha: Character):
    if cha.Race in [
        "Hill Dwarf",
        "Mountain Dwarf",
        "Lightfoot Halfling",
        "Stout Halfling",
        "Forest Gnome",
        "Rock Gnome",
    ]:
        speed = 25
    elif cha.Race == "Wood Elf":
        speed = 35
    else:
        speed = 30
    return speed


# ----function that sets speed of the character based on race---#


def set_AC(cha: Character):
    AC = 10 + modifiers(cha)[1]
    if cha.Class == "Monk":
        AC += modifiers(cha)[4]
    elif cha.Class == "Barbarian":
        AC += modifiers(cha)[2]
    return AC


# ----function that set AC based on some paramaters----#
def passiveperception(cha: Character):
    passive_perception = (
        10 + modifiers(cha)[4] + cha.Proficient[12] * set_proficiency(cha)
    )
    return passive_perception


def number_of_skills(pclass):
    if pclass == "Ranger" or pclass == "Bard":
        return 3
    elif pclass == "Rogue":
        return 4
    else:
        return 2


def set_proficiency(cha):
    prof = (cha.Level - 1) // 4 + 2
    return prof


# ------function that does math for the prof bonus------#


def set_alignment(cha):
    chart = [["Lawful", "Neutral", "Chaotic"], [" Good", " Neutral", " Evil"]]
    gne = input("Are you...\n1: Good\n2: Neutral\n3: Evil\n")
    while not gne.isdigit():
        gne = input("Please try again: ")
    while not int(gne) in range(1, 4):
        gne = input("Please try again: ")
    lnc = input("Are you...\n1: Lawful\n2: Neutral\n3: Chaotic\n")
    while not lnc.isdigit():
        lnc = input("Please try again: ")
    while not int(lnc) in range(1, 4):
        lnc = input("Please try again: ")
    alignment = chart[0][int(lnc) - 1] + chart[1][int(gne) - 1]
    os.system("clear")
    cha.Alignment = alignment


def set_background(cha):
    user = ""
    for i in range(len(phb.backgrounds)):
        print(f"{i+1}: {phb.backgrounds[i+1][0]}")
    user = input("Select a Background: ")
    while not user.isdigit():
        print("Please try again: ")
        user = input("Select a Background: ")
    while int(user) - 1 not in range(len(phb.backgrounds)):
        print("Please try again: ")
        user = input("Select a Background: ")
    os.system("clear")
    cha.Background = phb.backgrounds[int(user)]


def background_data(cha, background):
    Chosen_skills = []
    cha.Background = background[0]
    cha.Skills.append(phb.skill_names[background[1][0]])
    cha.Skills.append(phb.skill_names[background[1][1]])
    Chosen_skills.append(background[1][0])
    Chosen_skills.append(background[1][1])
    cha.Feats.append(background[2])
    return Chosen_skills


def character_sheet(cha):
    space = " "
    print(
        f"""
  Name: {cha.Name}         Race: {cha.Race}     Class: {cha.Class}
  
  Background: {cha.Background}        Alignment: {cha.Allignment}

  **********************************************************
  
  Hit Points: {cha.Hitpoints + modifiers(cha)[2]*cha.Level}{space*8}Armor Class: {set_AC(cha)}{space*3}Initiave modifier: {modifiers(cha)[1]}        
  Speed:      {set_movement_speed(cha)}{space*7}Passive Perception: {passiveperception(cha)}
  """
    )
    print(
        f"  Ability Scores:{space*6}|{space*2}Modifiers:{space*2}|{space*3}Saving Throws: "
    )
    print(
        f'  Strength:{space*8}{cha.Stats[0]}{space*2}|{space*2}+{modifiers(cha)[0]}{space*10}|   Str: {savingthrow(cha)["Strength"]}'
    )
    print(
        f'  Dexterity:{space*7}{cha.Stats[1]}{space*2}|{space*2}+{modifiers(cha)[1]}{space*10}|   Dex: {savingthrow(cha)["Dexterity"]}'
    )
    print(
        f'  Constitution:{space*4}{cha.Stats[2]}{space*2}|{space*2}+{modifiers(cha)[2]}{space*10}|   Con: {savingthrow(cha)["Constitution"]}'
    )
    print(
        f'  Intelligence:{space*5}{cha.Stats[3]}{space*2}|{space*2}+{modifiers(cha)[3]}{space*10}|   Int: {savingthrow(cha)["Intelligence"]}'
    )
    print(
        f'  Wisdom:{space*10}{cha.Stats[4]}{space*2}|{space*2}+{modifiers(cha)[4]}{space*10}|   Wis: {savingthrow(cha)["Wisdom"]}'
    )
    print(
        f'  Charisma:{space*8}{cha.Stats[5]}{space*2}|{space*2}+{modifiers(cha)[5]}{space*10}|   Cha: {savingthrow(cha)["Charisma"]}'
    )
    print(
        """
  **********************************************************
  """
    )
    print("  Proficiencies: ")
    for i in cha.Skills:
        print(f"  {i}")
    print("\n  Abilities: ")
    for i in cha.Abilities:
        print(f"  {i}")
    print("\n  Background Features: ")
    for i in cha.Feats:
        print(f"  {i}")


def main():
    character = construct()
    character_sheet(character)


if __name__ == "__main__":
    main()
