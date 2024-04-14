def load_proper_nouns():
    with open("proper_nouns.txt", "r") as file:
        proper_nouns = set(word.strip().lower() for word in file)
    return proper_nouns

def pluralize(word):
    proper_nouns = load_proper_nouns()
    
    # Check for empty string
    if not word:
        return {'plural': '', 'status': 'empty_string'}
    
    # Convert word to lowercase for proper noun check
    lowercase_word = word.lower()
    
    # Check if word is a proper noun
    if lowercase_word in proper_nouns:
        return {'plural': word, 'status': 'proper_noun'}
    
    # Check if word is already in plural
    if word.endswith('s'):
        return {'plural': word, 'status': 'already_in_plural'}
    
    # Apply pluralization rules
    if word.endswith(('ay', 'ey', 'iy', 'oy', 'uy')):
        plural = word + 's'
    elif word.endswith('y') and word[-2] not in 'aeiou':
        plural = word[:-1] + 'ies'
    elif word.endswith('f'):
        plural = word[:-1] + 'ves'
    elif word.endswith(('sh', 'ch', 'z', 'x')):
        plural = word + 'es'
    else:
        plural = word + 's'
    
    return {'plural': plural, 'status': 'success'}

# Test cases
test_cases = ["failure", "food", "Zulma", "injury", "elf", "buzz", "computers", "PCs", "",
              "highway", "presentation", "pouch", "COVID-19", "adam"]

for test_word in test_cases:
    result = pluralize(test_word)
    print(f"Input: {test_word}, Output: {result}")
