from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=word_len, reverse=True) # in-place!
    return words

def word_len(word) -> int:
    return len(word)

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=ab_num)
    return numbers

def ab_num(numbers) -> int:
    return abs(numbers)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
