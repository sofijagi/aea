# Teksta analīzes rīks

# Importējam bibliotēkas

from collections import Counter

def count_words(text):

"""

Skaita vārdus tekstā un atgriež skaitu.

"""

words = text.split()

return len(words)

def most_common_words(text, n=5):

"""

Atgriež n biežākos vārdus un to biežumu.

"""

words = text.split()

word_counts = Counter(words)

return word_counts.most_common(n)

def count_characters(text):

"""

Skaita kopējo rakstzīmju skaitu, burtus, ciparus un simbolus.

"""

total_chars = len(text)

letters = sum(c.isalpha() for c in text)

digits = sum(c.isdigit() for c in text)

symbols = total_chars - letters - digits

return {

"total": total_chars,

"letters": letters,

"digits": digits,

"symbols": symbols,

}

def find_longest_and_shortest_words(text):

"""

Atrod garāko un īsāko vārdu tekstā.

"""

words = text.split()

if not words:

return None, None

longest = max(words, key=len)

shortest = min(words, key=len)

return longest, shortest

def analyze_text(text):

"""

Galvenā funkcija teksta analīzei.

"""

word_count = count_words(text)

common_words = most_common_words(text)

char_counts = count_characters(text)

longest, shortest = find_longest_and_shortest_words(text)

result = {

"word_count": word_count,

"most_common_words": common_words,

"character_counts": char_counts,

"longest_word": longest,

"shortest_word": shortest,

}

return result

def main():

"""

Galvenā programma, kas pieņem lietotāja ievadi un veic analīzi.

"""

print("Laipni lūdzam teksta analīzes rīkā!")

text = input("Ievadiet tekstu analīzei: ")


analysis = analyze_text(text)

print("\nTeksta analīzes rezultāti:")

print(f"- Vārdu skaits: {analysis['word_count']}")

print("- Biežākie vārdi:")

for word, freq in analysis['most_common_words']:

print(f" {word}: {freq}")

print("- Rakstzīmju skaits:")

for key, value in analysis['character_counts'].items():

print(f" {key}: {value}")

print(f"- Garākais vārds: {analysis['longest_word']}")

print(f"- Īsākais vārds: {analysis['shortest_word']}")

if name == "__main__":

main()

# Teksta Analīzes Rīks

## Apraksts

Šis rīks analizē tekstu un sniedz šādu informāciju:

- Vārdu skaits.

- Biežāk sastopamie vārdi un to biežums.

- Rakstzīmju, burtu, ciparu un simbolu skaits.

- Garākais un īsākais vārds.

## Uzstādīšana un palaišana

Klonējiet repozitoriju:

```bash

git clone https://github.com/LIETOTAJVARDS/TextAnalysisTool.git

Ievadiet tekstu analīzei: Teksta piemērs analīzei.

Analīzes rezultāti:

- Vārdu skaits: 3

- Biežāk sastopamie vārdi:

Teksta: 1

piemērs: 1

analīzei: 1

- Rakstzīmju skaits:

Kopā: 24

Burti: 20

Cipari: 0

Simboli: 4

- Garākais vārds: analīzei

- Īsākais vārds: Teksta

