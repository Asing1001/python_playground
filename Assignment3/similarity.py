"""
File: similarity.py
Name:
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    max_similarity = 0
    best_match = ''
    long_sequence = input('Please give me a DNA sequence to search:').upper()
    short_sequence = input('What DNA sequence do you like to match').upper()
    short_sequence_length = len(short_sequence)
    for i in range(len(long_sequence) - short_sequence_length + 1):
        # print(i)
        wordA = long_sequence[i:i + short_sequence_length]
        similarity = get_similarity(wordA, short_sequence)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = wordA

    print('The best match is:' + best_match)
    pass


def get_similarity(word_a, short_sequence):
    similarity = 0
    length = len(word_a)
    for i in range(length):
        if word_a[i] == short_sequence[i]:
            similarity += 1
    # print(wordA, short_sequence, similarity)
    return similarity


if __name__ == '__main__':
    main()
