from typing import List

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_words(words: List[str]) -> List[str]:
    n = len(words)
    if n<=1:       #or we can do start < end to check if there is more than one element
        return words
    
    mid = n//2     #or (start+end)/2 if not starting from 0th index
    left = sort_words(words[:mid])  #start to mid -1
    right = sort_words(words[mid:]) # mid to end

    return merge(left,right)

def sort_numbers(numbers: List[int]) -> List[int]:
    n = len(numbers)
    if n<=1:       #or we can do start < end to check if there is more than one element
        return numbers
    
    mid = n//2     #or (start+end)/2 if not starting from 0th index
    left = sort_words(numbers[:mid]) #start to mid -1
    right = sort_words(numbers[mid:]) # mid to end

    return merge(left,right)

def sort_decimals(numbers: List[float]) -> List[float]:
    n = len(numbers)
    if n<=1:      #or we can do start < end to check if there is more than one element
        return numbers
    
    mid = n//2     #or (start+end)/2 if not starting from 0th index
    left = sort_words(numbers[:mid]) #start to mid -1
    right = sort_words(numbers[mid:]) # mid to end

    return merge(left,right)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
