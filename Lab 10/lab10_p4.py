# Problem 4

word_synonyms = {
    'travel': ['journey', 'go', 'jaunt', 'move_around', 'move', 'locomote', 'change_of_location', 'traveling', 'locomotion', 'trip'],
    'computer': ['data_processor', 'computing_machine', 'information_processing_system', 'calculator', 'electronic_computer', 'estimator', 'figurer', 'computing_device', 'reckoner'],
    'learn': ['hear', 'acquire', 'pick_up', 'teach', 'take', 'check', 'instruct', 'discover', 'read', 'get_a_line', 'study', 'find_out', 'determine', 'ascertain', 'memorize', 'watch', 'see'],
    'excited': ['shake_up', 'emotional', 'activated', 'frantic', 'energize', 'mad', 'charge_up', 'stimulate', 'worked_up', 'stir', 'charge', 'delirious', 'shake', 'agitate', 'wind_up', 'unrestrained']
}

# Add your code below
word = input(str("Please enter a word. "))

if word in word_synonyms:
    print(word_synonyms.get(word))
else:
    print("Your word is not in the dictionary.")
    