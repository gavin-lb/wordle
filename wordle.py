from collections import Counter
from functools import partial


def sort_words(words: list) -> list:
    counts = [Counter(letter) for letter in zip(*words)]
    scores = {}
    for word in words:
        score = {}
        for letter, count in zip(word, counts):
            score.setdefault(letter, []).append(count[letter])
        scores[word] = sum(max(v) for v in score.values())
    return sorted(words, key=scores.get, reverse=True)

def filter_word(word: str, correct: dict, partially: dict, incorrect: set) -> bool:
    if any(word[i] != c for i, c in correct.items()):
        return False
    unknown = {c for i, c in enumerate(word) if i not in correct}
    if unknown & incorrect:
        return False
    if not set(partially.values()) <= unknown:
        return False
    if any(word[i] == c for i, c in partially.items()):
        return False
    return True


def main():
    with open('wordle.txt') as file:
        words = [word.strip() for word in file]
    incorrect = set()
    while True:
        words = sort_words(words)
        print('\nPlease input one of these words:',
              *[f'{i: >2}) {w}' for i, w in enumerate(words[:5], 1)],
              sep='\n', end='\n\n')
        while True:
            num = input('Which number word did you input: ')
            try:
                if not 0 <= int(num) <= 5:
                    raise IndexError
                word = words[int(num)-1]
                break
            except:
                print('Invalid selection!')
        while True:
            colours = input('\nWhat were the colours? Use "g" for green, "y" for yellow and "b" for black, ie. "bygbb": ')
            if set(colours) <= set('gyb') and len(colours) == 5:
                break
            print('Invalid colours!')
        correct, partially = {}, {}
        for index, (colour, letter) in enumerate(zip(colours, word)):
            if colour == 'b':
                incorrect.add(letter)
            elif colour == 'g':
                correct[index] = letter
            elif colour == 'y':
                partially[index] = letter
        filter_func = partial(filter_word, correct=correct, partially=partially, incorrect=incorrect)
        words = list(filter(filter_func, words))
        if len(words) == 1:
            print('\nThe correct word is:', *words)
            break
        
if __name__ == '__main__':
    main()
