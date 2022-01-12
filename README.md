# Wordle
A script for solving the word game [Wordle](https://www.powerlanguage.co.uk/wordle/). 

It filters the set of all possible 5 letter words until it finds the correct answer. It use a scoring system for words in order to try and converge on the correct letters a bit quicker. It counts the frequency of letters at each index amongst the entire possible word set, then gives each word a score by summing of the frequency of their letters. However, in order to encourage words with 5 unique letters (as using a repeated letter misses an opportunity for ruling out an additional letter), it only takes the maximum frequency for a repeated letter and scores the other repeat(s) a zero. 

The user is given multiple options for the entered word at each step because sometimes the script will suggest a word that the game does not recognise (due to differing dictionaries), so there are a couple backup words to use in such an event.

Here is an example of command line output: 
```
Please input one of these words:
 1) cares
 2) bares
 3) tares
 4) pares
 5) canes

Which number word did you input: 1

What were the colours? Use "g" for green, "y" for yellow and "b" for black, ie. "bygbb": bgybb

Please input one of these words:
 1) rainy
 2) ranty
 3) ratty
 4) fairy
 5) lairy

Which number word did you input: 1

What were the colours? Use "g" for green, "y" for yellow and "b" for black, ie. "bygbb": ygbbb

Please input one of these words:
 1) valor
 2) jalor
 3) labor
 4) fator
 5) gator

Which number word did you input: 1

What were the colours? Use "g" for green, "y" for yellow and "b" for black, ie. "bygbb": ygbgg

The correct word is: favor
```
