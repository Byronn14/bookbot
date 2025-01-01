path_to_file = "books/frankenstein.txt"

def count_words(content):
    nb_words = 0
    lines = content.split('\n')
    for line in lines:
        words = line.split(' ')
        for s in words:
            if len(s) > 0:
                nb_words+= 1

    return nb_words

def count_characters(content):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    final_dict = {}
    content = content.lower()
    lines = content.split('\n')
    for line in lines:
        words = line.split(' ')
        for word in words:
            for letter in word:
                if letter in letters:
                    if (letter in final_dict):
                        final_dict[letter] += 1
                    else:
                        final_dict[letter] = 1
    
    return final_dict

def print_report(count_words,dict_char):
    dict_char_sorted = {k: v for k, v in sorted(dict_char.items(), key=lambda item: item[1], reverse=True)}

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words} words found in the document")
    print("")
    for keys in dict_char_sorted:
        print(f"The '{keys}' character was found {dict_char[keys]} times")
    print("--- End report ---")


with open(path_to_file) as f:
    file_contents = f.read()
    words = count_words(file_contents)
    dict_char = count_characters(file_contents)
    print_report(words,dict_char)