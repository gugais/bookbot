def count_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_char_counts(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append((char, count))
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_list