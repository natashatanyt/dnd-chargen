classes = {
    'Barbarian': {
        'Stat': 'Strength',
        'Weapons': ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsowrd'],
        'Armour': ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale mail', 'Breastplate', 'Half plate'],
        'Hit Dice': '1d12',
        'HP': '12',
        'Saving Throws': 'Strength, Constituion',
    },

    'Bard': {
        'Stat': 'Charisma',
        'Weapons': ['Club', 'Longsword', 'Rapier', 'Shortbow', 'Dagger', 'Mace', 'Sickle', 'Quarterstaff', 'Spear', 'Crossbow, light', 'Dart', 'Sling'],
        'Armour': ['Padded', 'Leather', 'Studded Leather'],
        'Hit Dice': '1d8',
        'HP': '8',  
        'Saving Throws': 'Charisma, Dexterity',
    },

    'Cleric': {
        'Stat': 'Wisdom',
        'Weapons': ['Club', 'Longsword', 'Rapier', 'Shortbow', 'Dagger', 'Mace', 'Sickle', 'Quarterstaff', 'Spear', 'Crossbow, light', 'Dart', 'Sling'],
        'Armour': ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale mail', 'Breastplate', 'Half plate'],
        'Hit Dice': '1d8',
        'HP': '8',
        'Saving Throws': 'Wisdom, Charisma',
    },

    'Druid': {
        'Stat': 'Wisdom',
        'Weapons': ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear'],
        'Armour': ['Padded', 'Leather', 'Studded Leather'],
        'Hit Dice': '1d8',
        'HP': '8',
        'Saving Throws': 'Wisdom, Intelligence',
    },

    'Fighter': {
        'Stat': 'Strength, Dexterity',
        'Weapons': ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsowrd'],
        'Armour': ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale mail', 'Breastplate', 'Half plate', 'Ring mail', 'Chain mail', 'Splint', 'Plate'],
        'Hit Dice': '1d10',
        'HP': '10',
        'Saving Throws': 'Strength, Constitution',
    },

    'Monk': {
        'Stat': 'Wisdom, Dexterity',
        'Weapons': ['Club', 'Shortsword', 'Dagger', 'Handaxe', 'Javelin', 'Nunchaku', 'Quarterstaff', 'Sling'],
        'Armour': ['None'],
        'Hit Dice': '1d8',
        'HP': '8',
        'Saving Throws': 'Dexterity, Strength',
    },

    'Paladin': {
        'Stat': 'Strength, Charisma',
        'Weapons': ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsowrd'],
        'Armour': ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale mail', 'Breastplate', 'Half plate', 'Ring mail', 'Chain mail', 'Splint', 'Plate'],
        'Hit Dice': '1d10',
        'HP': '10',
        'Saving Throws': 'Charisma, Wisdom',
    },

    'Ranger': {
        'Stat': 'Wisdom, Dexterity',
        'Weapons': ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsowrd'],
        'Armour': ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scale mail', 'Breastplate', 'Half plate'],
        'Hit Dice': '1d10',
        'HP': '10',
        'Saving Throws': 'Dexterity, Strength',
    },

    'Rogue': {
        'Stat': 'Dexterity',
        'Weapons': ['Crossbow, hand', 'Sap', 'Shortbow', 'Rapier', 'Sword, short', 'Club', 'Dagger', 'Javelin', 'Mace, light', 'Mace, heavy', 'Shortspear', 'Sickle', 'Spear', 'Gauntlet, spiked', 'Greatclub', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Crossbow, repeating light', 'Crossbow, repeating heavy'],
        'Armour': ['Padded', 'Leather', 'Studded Leather'],
        'Hit Dice': '1d8',
        'HP': '8',
        'Saving Throws': 'Dexterity, Intelligence',
    },

    'Sorcerer': {
        'Stat': 'Constitution, Charisma',
        'Weapons': ['Dagger', 'Dart', 'Sling', 'Quarterstaff'],
        'Armour': ['None'],
        'Hit Dice': '1d6',
        'HP': '6',
        'Saving Throws': 'Constitution, Charisma',
    },

    'Warlock': {
        'Stat': 'Charisma, Wisdom',
        'Weapons': ['Club', 'Longsword', 'Rapier', 'Shortbow', 'Dagger', 'Mace', 'Sickle', 'Quarterstaff', 'Spear', 'Crossbow, light', 'Dart', 'Sling'],
        'Armour': ['Padded', 'Leather', 'Studded Leather'],
        'Hit Dice': '1d8',
        'HP': '8',
        'Saving Throws': 'Charisma, Wisdom',
    },

    'Wizard': {
        'Stat': 'Intelligence',
        'Weapons': ['Dagger', 'Dart', 'Sling', 'Quarterstaff', 'Crossbow, light'],
        'Armour': ['None'],
        'Hit Dice': '1d6',
        'HP': '6',
        'Saving Throws': 'Intelligence, Wisdom',
    }
}