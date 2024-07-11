def get_word_count(fileContents):
    return len(fileContents.split())


def sort_on(d):
    return d["num"]

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def main():
    with open("books/frankenstein.txt") as f:
        fileContents = f.read()
    print(fileContents)
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(fileContents)} words found in the document")
    print()

    for item in chars_dict_to_sorted_list(get_chars_dict(fileContents)):
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
