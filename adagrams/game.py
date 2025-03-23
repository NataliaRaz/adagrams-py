from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():

    pool = []
    for letter, count in LETTER_POOL.items():
        for _ in range(count):
            pool.append(letter)
    
    letter_bank = []
    while len(letter_bank) < 10:
        index = randint(0, len(pool) - 1)
        letter = pool[index]
        letter_bank.append(letter)
        pool.pop(index) 

    return letter_bank

def uses_available_letters(word, letter_bank):
    
    word = word.upper()
    letter_bank_counts = {}

    for letter in letter_bank:
        letter = letter.upper()
        if letter in letter_bank_counts:
            letter_bank_counts[letter] += 1
        else:
            letter_bank_counts[letter] = 1
    
    for letter in word:
        if letter not in letter_bank_counts or letter_bank_counts[letter] == 0:
            return False 
        letter_bank_counts[letter] -= 1
    
    return True

def score_word(word):
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    word = word.upper()
    score = 0

    for letter in word:
        score += letter_scores[letter]

    if 7 <= len(word) <= 10:
        score += 8

    return score

def get_highest_word_score(word_list):
    best_word = None
    best_score = 0

    for word in word_list:
        current_score = score_word(word)

        if best_word is None or current_score > best_score:
            best_word = word
            best_score = current_score
        elif current_score == best_score:
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
            elif len(best_word) != 10 and len(word) < len(best_word):
                best_word = word

    return (best_word, best_score)