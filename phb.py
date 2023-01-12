options = ["str", "dex", "con", "int", "wis", "cha"]


classes = {
    1: "Barbarian",
    2: "Bard",
    3: "Cleric",
    4: "Druid",
    5: "Fighter",
    6: "Monk",
    7: "Paladin",
    8: "Ranger",
    9: "Rogue",
    10: "Sorcerer",
    11: "Warlock",
    12: "Wizard",
}

cLass = """Pick a Class:
1:  [Barbarian]
2:  [Bard]
3:  [Cleric]
4:  [Druid]
5:  [Fighter]
6:  [Monk]
7:  [Paladin]
8:  [Ranger]
9:  [Rogue]
10: [Sorcerer]
11: [Warlock]
12: [Wizard]\n"""

races = {
    1: "Dragonborn",
    2: "Hill Dwarf",
    3: "Mountain Dwarf",
    4: "High Elf",
    5: "Dark Elf",
    6: "Wood Elf",
    7: "Forest Gnome",
    8: "Rock Gnome",
    9: "Half-Elf",
    10: "Lightfoot Halfling",
    11: "Stout Halfling",
    12: "Half-Orc",
    13: "Human",
    14: "Tiefling",
}

raCe = """Pick a Race:
1:  [Dragonborn]
2:  [Hill Dwarf]
3:  [Mountain Dwarf]
4:  [Dark Elf]
5:  [High Elf]
6:  [Wood Elf]
7:  [Forest Gnome]
8:  [Rock Gnome]
9:  [Half-Elf]
10: [Lightfoot Halfling]
11: [Stout Halfling]
12: [Half-Orc]
13: [Human]
14: [Tiefling]\n"""

raceBonus = {
    "High Elf": [0, 2, 0, 1, 0, 0],
    "Wood Elf": [0, 2, 0, 0, 1, 0],
    "Dark Elf": [0, 2, 0, 0, 0, 1],
    "Hill Dwarf": [0, 0, 2, 0, 1, 0],
    "Mountain Dwarf": [2, 0, 2, 0, 0, 0],
    "Dragonborn": [2, 0, 0, 0, 0, 1],
    "Forest Gnome": [0, 1, 0, 2, 0, 0],
    "Rock Gnome": [0, 0, 1, 2, 0, 0],
    "Half-Elf": [0, 0, 0, 0, 0, 2],
    "Lightfoot Halfling": [0, 2, 0, 0, 0, 1],
    "Stout Halfling": [0, 2, 1, 0, 0, 0],
    "Half-Orc": [2, 0, 1, 0, 0, 0],
    "Human": [1, 1, 1, 1, 1, 1],
    "Tiefling": [0, 0, 0, 1, 0, 2],
}

Hit_Dice = {
    "Wizard": 6,
    "Sorcerer": 6,
    "Cleric": 8,
    "Bard": 8,
    "Warlock": 8,
    "Druid": 8,
    "Rogue": 8,
    "Monk": 8,
    "Ranger": 10,
    "Paladin": 10,
    "Fighter": 10,
    "Barbarian": 12,
}

skill_names = [
    "Athletics",
    "Acrobatics",
    "Sleight of Hand",
    "Stealth",
    "Arcana",
    "History",
    "Investigation",
    "Nature",
    "Religion",
    "Animal Handling",
    "Insight",
    "Medicine",
    "Perception",
    "Survival",
    "Deception",
    "Intimidation",
    "Performance",
    "Persuasion",
]

skills = [0, 1, 1, 1, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5]
# proficient = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

proficiency_options = {
    "Fighter": [1, 9, 0, 5, 10, 15, 12, 13],
    "Barbarian": [9, 0, 15, 7, 13, 14],
    "Cleric": [5, 10, 11, 17, 8],
    "Druid": [4, 9, 10, 11, 7, 12, 8, 13],
    "Monk": [1, 0, 5, 10, 8, 3],
    "Paladin": [0, 10, 15, 11, 17, 8],
    "Ranger": [9, 0, 10, 6, 7, 12, 3, 13],  # choose 3
    "Rogue": [1, 0, 14, 10, 15, 6, 12, 16, 17, 2, 3],  # choose 4
    "Sorcerer": [4, 14, 10, 15, 17, 8],
    "Warlock": [4, 14, 5, 15, 6, 7, 8],
    "Wizard": [4, 5, 10, 6, 11, 8],
    "Bard": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],  # choose 3
}

levelup = {
    "Barbarian": [
        ["Rage", "Unarmored Defense"],
        ["Reckless Attack", "Danger Sense"],
        ["Subclass", 0],
        ["Ability Score Improvement"],
        ["Extra Attack", "Fast Movement"],
        [1],
        ["Feral Instinct"],
        ["Ability Score Improvement"],
        ["Brutal Critical 1"],
        [2],
        ["Relentless Rage"],
        ["Ability Score Improvement"],
        ["Brutal Critical 2"],
        [3],
        ["Persistant Rage"],
        ["Ability Score Improvement"],
        ["Brutal Critical 3"],
        ["Indomidable Might"],
        ["Ability Score Improvement"],
        ["Primal Champion"],
    ],
    "Bard": [
        ["Spellcasting", "Bardic Inspiration (d6)"],
        ["Jack of All Trades", "Song of Rest (d6)"],
        ["Subclass", "Expertise", 0],
        ["Ability Score Improvement"],
        ["Bardic Inspiration (d8)", "Font of Inspiration"],
        ["Countercharm", 1],
        [],
        ["Ability Score Improvement"],
        ["Song of Rest (d8)"],
        ["Bardic Inspiration (d10)", "Expertise", "Magical Secrets"],
        [],
        ["Ability Score Improvement"],
        ["Song of Rest (d10)"],
        ["Magical Secrets", 2],
        ["Bardic Inspiration (d12)"],
        ["Magical Secrets"],
        ["Ability Score Improvement"],
        ["Superior Inspiration"],
    ],
    "Cleric": [
        ["Spellcasting", "Subclass", 0],
        ["Channel Divinity (1/rest)", 1],
        [],
        ["Ability Score Improvement"],
        ["Destroy Undead (CR 1/2)"],
        ["Channel Divinity (2/rest)", 2],
        [],
        ["Ability Score Improvement", "Destroy Undead (CR 1)", 3],
        [],
        ["Divine Intervention"],
        ["Destroy Undead (CR 2)"],
        ["Ability Score Improvement"],
        [],
        ["Destroy Undead (CR 3)"],
        [],
        ["Ability Score Improvement"],
        ["Destroy Undead (CR 4)", 4],
        ["Channel Divinity (3/rest)"],
        ["Ability Score Improvement"],
        ["Divine Intervention Improvement"],
    ],
    "Druid": [
        ["Druidic", "Spellcasting"],
        ["Wild Shape", "Subclass", 0],
        [],
        ["Wild Shape Improvement", "Ability Score Improvement"],
        [],
        [1],
        [],
        ["Wild Shape Improvement", "Ability Score Improvement"],
        [],
        [2],
        [],
        ["Ability Score Improvement"],
        [],
        [3],
        [],
        ["Ability Score Improvement"],
        [],
        ["Timeless Body", "Beast Spells"],
        ["Ability Score Improvement"],
        ["Archdruid"],
    ],
    "Fighter": [
        ["Fighting Style", "Second Wind"],
        ["Action Surge (one use)"],
        ["Subclass", 0],
        ["Ability Score Improvement"],
        ["Extra Attack"],
        ["Ability Score Improvement"],
        [1],
        ["Ability Score Improvement"],
        ["Indomidable (one use)"],
        [2],
        ["Extra Attack (2)"],
        ["Ability Score Improvement"],
        ["Indomidable (two uses)"],
        ["Ability Score Improvement"],
        [3],
        ["Ability Score Improvement"],
        ["Action Surge (two uses)", "Indomitable (three uses)"],
        [4],
        ["Ability Score Improvement"],
        ["Extra Attack (3)"],
    ],
    "Monk": [
        ["Unarmored Defense", "Martial Arts"],
        ["Ki", "Unarmored Movement"],
        ["Subclass", "Deflect Missiles", 0],
        ["Ability Score Improvement", "Slow Fall"],
        ["Extra Attack", "Stunning Strike"],
        ["Ki-Empowered Strikes", 1],
        ["Evasion", "Stillness of Mind"],
        ["Ability Score Improvement"],
        ["Unarmored Movement Improvement"],
        ["Purity of Body"],
        [2],
        ["Ability Score Improvement"],
        ["Tongue of the Sun and Moon"],
        ["Diamond Soul"],
        ["Timeless Body"],
        ["Ability Score Improvement"],
        [3],
        ["Empty Body"],
        ["Ability Score Improvement"],
        ["Perfect Self"],
    ],
    "Paladin": [
        ["Divine Sense", "Lay on Hands"],
        ["Fighting Style", "Spellcasting", "Divine Smite"],
        ["Divine Health", "Subclass", 0],
        ["Ability Score Improvement"],
        ["Extra Attack"],
        ["Aura of Protection"],
        [1],
        ["Ability Score Improvement"],
        [],
        ["Aura of Courage"],
        ["Improved Divine Smite"],
        ["Ability Score Improvement"],
        [],
        ["Cleansing Touch"],
        [2],
        ["Ability Score Improvement"],
        [],
        ["Aura improvements"],
        ["Ability Score Improvement"],
        [3],
    ],
    "Ranger": [
        ["Favored Enemy", "Natural Explorer"],
        ["Fighting Style", "Spellcasting"],
        ["Subclass", 0, "Primeval Awareness"],
        ["Ability Score Improvement"],
        ["Extra Attack"],
        ["Favored Enemy and Natural Explorer improvements"],
        [1],
        ["Ability Score Improvement", "Land's Stride"],
        [],
        ["Natural Explorer improvement", "Hide in Plain Sight"],
        [2],
        ["Ability Score Improvement"],
        [],
        ["Favored Enemy improvement", "Vanish"],
        [3],
        ["Ability Score Improvement"],
        [],
        ["Ferel Senses"],
        ["Ability Score Improvement"],
        ["Foe Slayer"],
    ],
    "Rogue": [
        ["Expertise", "Sneak Attack", "Thieves' Cant"],
        ["Cunning Action"],
        ["Subclass", 0],
        ["Ability Score Improvement"],
        ["Uncanny Dodge"],
        ["Expertise"],
        ["Evasion"],
        ["Ability Score Improvement"],
        [1],
        ["Ability Score Improvement"],
        ["Reliable Talent"],
        ["Ability Score Improvement"],
        [2],
        ["Blindsense"],
        ["Slippery Mind"],
        ["Ability Score Improvement"],
        [3],
        ["Elusive"],
        ["Ability Score Improvement"],
        ["Stroke of Luck"],
    ],
    "Sorcerer": [
        ["Spellcasting", "Subclass", 0],
        ["Font of Magic"],
        ["Metamagic"],
        ["Ability Score Improvement"],
        [],
        [1],
        [],
        ["Ability Score Improvement"],
        [],
        ["Metamagic"],
        [],
        ["Ability Score Improvement"],
        [],
        [2],
        [],
        ["Ability Score Improvement"],
        ["Metamagic"],
        [3],
        ["Ability Score Improvement"],
        ["Sorcerous Restoration"],
    ],
    "Warlock": [
        ["Subclass", "Pact Magic", 0],
        ["Eldritch Invocations"],
        ["Pact Boon"],
        ["Ability Score Improvement"],
        [],
        [1],
        [],
        ["Ability Score Improvement"],
        [],
        [2],
        ["Mystic Arcanum(6th level)"],
        ["Ability Score Improvement"],
        ["Mystic Arcanum(7th level)"],
        [3],
        ["Mystic Arcanum(8th level)"],
        ["Ability Score Improvement"],
        ["Mystic Arcanum(9th level)"],
        [],
        ["Ability Score Improvement"],
        ["Eldritch Master"],
    ],
    "Wizard": [
        ["Spellcasting", "Arcane Recovery"],
        ["Subclass", 0],
        [],
        ["Ability Score Improvement"],
        [],
        [1],
        [],
        ["Ability Score Improvement"],
        [],
        [2],
        [],
        ["Ability Score Improvement"],
        [],
        [3],
        [],
        ["Ability Score Improvement"],
        [],
        ["Spell Mastery"],
        ["Signature Spell"],
    ],
}
subclasses = {
    "Barbarian": {1: "Path of the Berserker", 2: "Path of the Totem Warrior"},
    "Bard": {1: "College of Lore", 2: "College of Valor"},
    "Cleric": {
        1: "Knowlege Domain",
        2: "Life Domain",
        3: "Light Domain",
        4: "Nature Domain",
        5: "Tempest Domain",
        6: "Trickery Domain",
        7: "War Domain",
    },
    "Druid": {1: "Circle of the Land", 2: "Circle of the Moon"},
    "Fighter": {1: "Champion", 2: "Battle Master", 3: "Eldrich Knight"},
    "Monk": {
        1: "Way of the Open Hand",
        2: "Way of Shadow",
        3: "Way of the Four Elements",
    },
    "Paladin": {
        1: "Oath of Devotion",
        2: "Oath of the Ancients",
        3: "Oath of Vengance",
    },
    "Ranger": {1: "Hunter", 2: "Beast Master"},
    "Rogue": {1: "Thief", 2: "Assassin", 3: "Arcane Trickster"},
    "Sorcerer": {1: "Draconic Bloodline", 2: "Wild Magic"},
    "Warlock": {1: "The Archfey", 2: "The Fiend", 3: "The Great Old One"},
    "Wizard": {
        1: "School of Abjuration",
        2: "School of Conjuration",
        3: "School of Divination",
        4: "School of Enchantment",
        5: "School of Evocation",
        6: "School of Illusion",
        7: "School of Necromancy",
        8: "School of Transmutation",
    },
}
subclass_features = {
    "Path of the Berserker": [
        ["Frenzy"],
        ["Mindless Rage"],
        ["Intimidating Presence"],
        ["Retaliation"],
    ],
    "Path of the Totem Warrior": [
        ["Spirit Seeker", "Totem Spirit"],
        ["Aspect of the Beast"],
        ["Spirit Walker"],
        ["Totemic Attunement"],
    ],
    "College of Lore": [
        ["Bonus Proficiencies", "Cutting Words"],
        ["Adittional Magical Secrets"],
        ["Peerless Skill"],
    ],
    "College of Valor": [
        ["Bonus Proficiencies", "Combat Inspiration"],
        ["Extra Attack"],
        ["Battle Magic"],
    ],
    "Knowlege Domain": [
        ["Blessings of Knowlege"],
        ["Channel Divinity: Knowlege of the Ages"],
        ["Channel Divinity: Read Thoughts"],
        ["Potent Spellcasting"],
        ["Visions of the Past"],
    ],
    "Life Domain": [
        ["Bonus Proficiency", "Disciple of Life"],
        ["Channel Divinity: Preserve Life"],
        ["Blessed Healer"],
        ["Divine Strike"],
        ["Supreme Healing"],
    ],
    "Light Domain": [
        ["Bonus Cantrip", "Warding Flare"],
        ["Channel Divinity: Radiance of the Dawn"],
        ["Improved Flare"],
        ["Potent Spellcasting"],
        ["Corona of Light"],
    ],
    "Nature Domain": [
        ["Acolyte of Nature", "Bonus Proficiency"],
        ["Channel Divinity: Charm Animals and Plants"],
        ["Dampen Elements"],
        ["Divine Strike"],
        ["Master of Nature"],
    ],
    "Tempest Domain": [
        ["Bonus proficiencies", "Wrath of the Storm"],
        ["Channel Divinity: Destructive Wrath"],
        ["Thunderbolt Strike"],
        ["Divine Strike"],
        ["Stormborn"],
    ],
    "Trickery Domain": [
        ["Blessing of the Trickster"],
        ["Channel Divinity: Invoke Duplicity"],
        ["Channel Duplicity: Cloak of Shadows"],
        ["Divine Strike"],
        ["Improved Duplicity"],
    ],
    "War Domain": [
        ["Bonus Proficiencies", "War Priest"],
        ["Channel Divinity: Guided Strike"],
        ["Channel Divinity: War God's Blessing"],
        ["Divine Strike"],
        ["Avatar of Battle"],
    ],
    "Circle of the Land": [
        ["Bonus Cantrip", "Natural Recovery"],
        ["Land's Stride"],
        ["Nature's Ward"],
        ["Nature's Sanctuary"],
    ],
    "Circle of the Moon": [
        ["Combat Wild Shape", "Circle Forms"],
        ["Primal Strike"],
        ["Elemental Wild Shape"],
        ["Thousand Forms"],
    ],
    "Champion": [
        ["Improved Critical"],
        ["Remarkable Athlete"],
        ["Addtional Fighting Style"],
        ["Superior Critial"],
        ["Survivor"],
    ],
    "Battle Master": [
        ["Combat Superiority"],
        ["Student of War"],
        ["Know Your Enemey"],
        ["Improved Combat Superiority"],
        [" Relentless"],
    ],
    "Eldrich Knight": [
        ["Spellcasting"],
        ["Weapon Bond"],
        ["War Magic"],
        ["Eldritch Strike"],
        ["Arcane Charge"],
        ["Improved War Magic"],
    ],
    "Way of the Open Hand": [
        ["Open Hand Technique"],
        ["Wholeness of Body"],
        ["Tranquility"],
        ["Quivering Palm"],
    ],
    "Way of Shadow": [
        ["Shadow Arts"],
        ["Shadow Step"],
        ["Cloak of Shadows"],
        ["Opportunist"],
    ],
    "Way of the Four Elements": [
        ["Disciple of the Elements"],
        ["Elemental Disciplines"],
    ],
    "Oath of Devotion": [
        ["Channel Divinity: Sacred Weapon"],
        ["Channel Divinity: Turn the unholy"],
        ["Aura of Devotion"],
        ["Purity of Spirit"],
        ["Holy Nimbus"],
    ],
    "Oath of the Ancients": [
        ["Channel Divinity: Nature's Wrath"],
        ["Channel Divinity: Turn the Faithless"],
        ["Aura of Warding"],
        ["Undying Sentinel"],
        ["Elder Champion"],
    ],
    "Oath of Vengance": [
        ["Channel Divinity: Abjure Enemy"],
        ["Channel Divinity: Vow of Enmity"],
        ["Relentless Avenger"],
        ["Soul of Vengeance"],
        ["Avenging Angel"],
    ],
    "Hunter": [
        ["Hunter's Prey"],
        ["Defensive Attack"],
        ["Multiattack"],
        ["Superior Hunter's Defense"],
    ],
    "Beast Master": [
        ["Ranger's Companion"],
        ["Exceptional training"],
        ["Bestial Fury"],
        ["Share Spells"],
    ],
    "Thief": [
        ["Fast Hands"],
        ["Second-Story Work"],
        ["Supreme Sneak"],
        ["Use Magic Device"],
        ["Thief's Reflexes"],
    ],
    "Assassin": [
        ["Bonus Proficiencies"],
        ["Assassiante"],
        ["Infiltration"],
        ["Impostor"],
        ["Death Strike"],
    ],
    "Arcane Trickster": [
        ["Spellcasting"],
        ["Mage Hand Legerdemain"],
        ["Magical Ambush"],
        ["Versatile Tickster"],
        ["Spell thief"],
    ],
    "Draconic Bloodline": [
        ["Dragon Ancestor"],
        ["Draconic Resilience"],
        ["Elemental Affinity"],
        ["Dragon Wings"],
        ["Draconic Presence"],
    ],
    "Wild Magic": [
        ["Wild Magic Surge"],
        ["Tides of Chaos"],
        ["Bend Luck"],
        ["Controlled Chaos"],
        ["Spell Bombardment"],
    ],
    "The Archfey": [
        ["Fey Presence"],
        ["Misty Escape"],
        ["Beguiling Defences"],
        ["Dark Delirium"],
    ],
    "The Fiend": [
        ["Dark One's Blessing"],
        ["Dark One's Own Luck"],
        ["Fiendish Resilience"],
        ["Hurl Through Hell"],
    ],
    "The Great Old One": [
        ["Awakened Mind"],
        ["Entropic Ward"],
        ["Thought Shield"],
        ["Create Thrall"],
    ],
    "School of Abjuration": [
        ["Abjuration Savant"],
        ["Arcane Ward"],
        ["Projected Ward"],
        ["Improved Abjuration"],
        ["Spell Resistance"],
    ],
    "School of Conjuration": [
        ["Conjuration Savant"],
        ["Minor Conjuration"],
        ["Benign Transposition"],
        ["Focused"],
        ["Durable Summons"],
    ],
    "School of Divination": [
        ["Divination Savant"],
        ["Portent"],
        ["Expert Divination"],
        ["The Third Eye"],
        ["Greater Portent"],
    ],
    "School of Enchantment": [
        ["Enchantment Savant"],
        ["Hypnotic Gaze"],
        ["Intsinctive Charm"],
        ["Split Enchantment"],
        ["Alter Memories"],
    ],
    "School of Evocation": [
        ["Evocation Savant"],
        ["Sculpt Spells"],
        ["Potent Cantrip"],
        ["Empowered Evocation"],
        ["Overchannel"],
    ],
    "School of Illusion": [
        ["Illusion Savant"],
        ["Improved Minor Illusion"],
        ["Malleable Illusion"],
        ["Illusory Reality"],
    ],
    "School of Necromancy": [
        ["Necromancy Savant"],
        ["Grim Harvest"],
        ["Undead Thralls"],
        ["Inured to Undeath"],
        ["Command Dead"],
    ],
    "School of Transmutation": [
        ["Transmutation Savant"],
        ["Minor Alchemy"],
        ["Tranmuter's stone"],
        ["Shapechanger"],
        ["Master Transmuter"],
    ],
}

backgrounds = {
    1: ["Acolyte", [10, 8], "Shelter of the Faithful"],
    2: ["Charlatan", [2, 14], "False Identity"],
    3: ["Criminal", [14, 3], "Criminal Contact"],
    4: ["Entertainer", [1, 16], "By Popular Demand"],
    5: ["Folk Hero", [9, 13], "Rustic Hospitality"],
    6: ["Gladiator", [1, 16], "By Popular Demand"],
    7: ["Guild Artisan", [10, 17], "Guild Membership"],
    8: ["Hermit", [11, 8], "Discovery"],
    9: ["Knight", [5, 17], "Retainers"],
    10: ["Noble", [5, 17], "Position of Privilege"],
    11: ["Outlander", [0, 13], "Wanderer"],
    12: ["Pirate", [0, 12], "Bad Reputaion"],
    13: ["Sage", [4, 5], "Researcher"],
    14: ["Sailor", [0, 12], "Ships's Passage"],
    15: ["Soldier", [0, 15], "Military Rank"],
    16: ["Urchin", [2, 3], "City Secrets"],
}