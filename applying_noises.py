import random
import csv
import pandas as pd
def vowel_lengthening(word):
    replacements = {
        'অ': 'ও',
        'ই': 'ঈ',
        'উ': 'ঊ'
    }
    for original, replacement in replacements.items():
        word = word.replace(original, replacement)
    return word

def consonant_omission(word):
    consonants_to_omit = ['স্ক', 'স্প', 'স্ত']
    for consonant in consonants_to_omit:
        word = word.replace(consonant, consonant[-1])
    return word

def affricate_softening(word):
    replacements = {
        'চ': 'স',
        'ছ': 'স',
        'জ': 'য'
    }
    for original, replacement in replacements.items():
        word = word.replace(original, replacement)
    return word

def vowel_reduction(word):
    replacements = {
        'ও': 'অ',
        'ঈ': 'ই',
        'ঊ': 'উ'
    }
    for original, replacement in replacements.items():
        word = word.replace(original, replacement)
    return word

def initial_consonant_change(word):
    replacements = {
        'গ': 'ঘ',
        'ক': 'খ',
        'চ': 'ছ'
    }
    if word[0] in replacements:
        word = replacements[word[0]] +  word[1 : ]
    return word

def syllable_omission(word):
    syllables = word.split('া')
    if len(syllables) > 2:
        del syllables[1]
        word = 'া'.join(syllables)
    return word

def consonant_doubling(word):
    last_char = word[-1]
    if 'অ' <= last_char <= 'ঔ': # TODO: or 'া' <= last_char <= 'ৌ':  # if the last character is a vowel, skip
        return word
    return word + last_char

def ending_variations(word):
    replacements = {
        'ছে': 'ছো',
        'লে': 'লো',
        'রে': 'রি'
    }
    for original, replacement in replacements.items():
        if word.endswith(original):
            word = word[:-len(original)] + replacement
    return word

def vowel_shifts(word):
    replacements = {
        'আ': 'ই',
        'ই': 'ঈ',
        'উ': 'ঊ'
    }
    for original, replacement in replacements.items():
        word = word.replace(original, replacement)
    return word

def consonant_hardening(word):
    replacements = {
        'ঝ': 'জ',
        'ঘ': 'গ',
        'ঢ': 'ড'
    }
    for original, replacement in replacements.items():
        word = word.replace(original, replacement)
    return word

def syllable_reversal(word): # TODO: Reverse each syllables 
    syllables = word.split('া')
    if len(syllables) == 2:
        word = 'া'.join(reversed(syllables))
    return word

def vowel_omission(word):
    if 'া' in word:
        word = word.replace('া', '', 1)
    return word

def consonant_blending(word):
    replacements = {
        'ক্ষ': 'শ',
        'ঞ্চ': 'চ',
        'ঞ্ছ': 'ছ'
    }
    for original, replacement in replacements.items():
        word = word.replace(original, replacement)
    return word

# Define a function to apply all distortions and return a dictionary
def apply_all_distortions(word):
    functions = [
        ("Original", lambda x: x),
        ("Vowel Lengthening", vowel_lengthening),
        ("Consonant Omission", consonant_omission),
        ("Affricate Softening", affricate_softening),
        ("Vowel Reduction", vowel_reduction),
        ("Initial Consonant Change", initial_consonant_change),
        ("Syllable Omission", syllable_omission),
        ("Consonant Doubling", consonant_doubling),
        ("Ending Variations", ending_variations),
        ("Vowel Shifts", vowel_shifts),
        ("Consonant Hardening", consonant_hardening),
        ("Syllable Reversal", syllable_reversal),
        ("Vowel Omission", vowel_omission),
        ("Consonant Blending", consonant_blending)
    ]
    
    distorted_dict = {}
    for name, func in functions:
        distorted_word = func(word)
        if distorted_word not in distorted_dict.values():  # Check for duplicates
            distorted_dict[name] = distorted_word
        else:
            distorted_dict[name] = ""
    return distorted_dict

# Load the words from filtered_unique_words.txt
with open('filtered_unique_words.txt', 'r', encoding='utf-8') as f:
    words = f.read().splitlines()

# Filter words based on their length in the range 3 to 15
filtered_words = [word for word in words if 7 <= len(word) <= 15]

# Apply the distortions to each word and store in a list of dictionaries
all_distorted_dicts = [apply_all_distortions(word) for word in filtered_words]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_distorted_dicts)

# Save the DataFrame to a .csv file
df.to_csv('distorted_words.tsv', sep='\t', index=False, encoding='utf-8')



# # Define a function to apply all distortions
# def apply_all_distortions(word):
#     functions = [
#         vowel_lengthening, consonant_omission, affricate_softening, vowel_reduction,
#         initial_consonant_change, syllable_omission, consonant_doubling, ending_variations,
#         vowel_shifts, consonant_hardening, syllable_reversal, vowel_omission, consonant_blending
#     ]
#     distorted_words = [word]  # Start with the original word
#     for func in functions:
#         distorted_word = func(word)
#         distorted_words.append(distorted_word)
#     return distorted_words

# # Load the words from filtered_unique_words.txt
# with open('filtered_unique_words.txt', 'r', encoding='utf-8') as f:
#     words = f.read().splitlines()

# # Apply the distortions to each word and store in a list
# all_distorted_words = []
# for word in words:
#     distortions = apply_all_distortions(word)
#     all_distorted_words.extend(distortions)

# # Convert the list of distorted words to a DataFrame
# df = pd.DataFrame(all_distorted_words, columns=['word'])

# # Save the DataFrame to a .csv file
# df.to_csv('distorted_words.csv', index=False, encoding='utf-8')
# # Create a CSV file
# output_csv = 'distorted_words.csv'
# with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Word',
#     'vowel_lengthening',
#     'consonant_omission',
#     'affricate_softening',
#     'vowel_reduction',
#     'initial_consonant_change',
#     'syllable_omission',
#     'consonant_doubling',
#     'ending_variations',
#     'vowel_shifts',
#     'consonant_hardening',
#     'syllable_reversal',
#     'vowel_omission',
#     'consonant_blending']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for word in filtered_words:
#         writer.writerow({
#             'Word': word,
#             'Typographical Errors': typographical_error(word),
#             'Character Swap': character_swap(word),
#             'Character Deletion': character_deletion(word),
#             'Character Insertion': character_insertion(word),
#             'Character Substitution': character_substitution(word)
#         })

# output_csv