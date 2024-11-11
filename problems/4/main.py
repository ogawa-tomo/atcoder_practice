import re

def main():
    S = input()
    all_patterns = []
    for k_length in range(1, min(4, len(S) + 1)):
        if k_length == 1:
            all_patterns.append('.')
            for letter in S:
                all_patterns.append(letter)
        if k_length == 2:
            two_letter_patterns_list = two_letter_patterns(S)
            for two_letter_pattern in two_letter_patterns_list:
                all_patterns.extend(two_letter_patterns_with_dots(two_letter_pattern))
        if k_length == 3:
            three_letter_patterns_list = three_letter_patterns(S)
            for three_letter_pattern in three_letter_patterns_list:
                all_patterns.extend(three_letter_patterns_with_dots(three_letter_pattern))
    all_patterns = list(set(all_patterns))

    result_num = 0
    for pattern in all_patterns:
        if re.search(pattern, S):
            result_num += 1
    
    print(result_num)

def two_letter_patterns(strings):
    patterns = []
    for i in range(len(strings) - 1):
        patterns.append(strings[i:i+2])
    return list(set(patterns))

def three_letter_patterns(strings):
    patterns = []
    for i in range(len(strings) - 2):
        patterns.append(strings[i:i+3])
    return list(set(patterns))

def two_letter_patterns_with_dots(pattern):
    return [
        '..',
        f'.{pattern[1]}',
        f'{pattern[0]}.',
        pattern,
    ]


def three_letter_patterns_with_dots(pattern):
    return [
        '...',
        f'..{pattern[2]}',
        f'.{pattern[1]}.',
        f'.{pattern[1]}{pattern[2]}',
        f'{pattern[0]}..',
        f'{pattern[0]}.{pattern[2]}',
        f'{pattern[0]}{pattern[1]}.',
        pattern
    ]

main()
