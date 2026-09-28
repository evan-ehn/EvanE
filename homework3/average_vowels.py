# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def counting_vowels_and_consonants(letters):
    consonants = 0
    vowels = 0
    is_vowel = "eouia"
    for i in letters:
        char = i
        if char.isalpha():
            if char in is_vowel:
                vowels += 1
            else:
                consonants += 1
    return(vowels, consonants)
print(counting_vowels_and_consonants("hello world"))

def average_vowels_and_consonants(paragraph):
    number_of_sentences = 0
    average_vowels_per_sentence = 0
    average_consonants_per_sentence = 0
    is_end = ".!?"
    for i in paragraph:
        sentence = i
        if sentence in is_end:
            number_of_sentences += 1

    consonants = 0
    vowels = 0
    is_vowel = "eouia"
    for i in paragraph:
        char = i
        if char.isalpha():
            if char in is_vowel:
                vowels += 1
            else:
                consonants += 1
    average_vowels_per_sentence = vowels / number_of_sentences
    average_consonants_per_sentence = consonants / number_of_sentences

    return(number_of_sentences, average_vowels_per_sentence, average_consonants_per_sentence)
print(average_vowels_and_consonants(
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
))
    