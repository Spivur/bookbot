def get_num_words(text):
    return len(text.split())

def sort_on(dict):
    return dict["value"]

def get_num_characters(text):
    characterDict = {}
    for char in text.lower():
        if char not in characterDict:
            characterDict[char] = 1
        else:
            characterDict[char] += 1

    return characterDict

def print_report(dict):
    sorted_list = []
    for row in dict:
        if row.isalpha():
            sorted_list.append({"key":row, "value":dict[row]})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list