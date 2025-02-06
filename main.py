def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        charcount = count_chars(file_contents)
        print(charcount)
        print(dict_to_list_of_dicts(charcount))

def count_words(text: str) -> int:
    return len(text.split())

def count_chars(text: str) -> dict:
    text = text.lower()
    resp_dict = {}
    for char in text:        
        if char in resp_dict:
            resp_dict[char] +=1
        else:
            resp_dict[char] = 1
    return resp_dict

def dict_to_list_of_dicts(dict:dict) -> list:
    return_list = []
    for char in list(dict):
        if char.isalpha():
            return_list.append({"letter":char,"count":dict[char]})
    return return_list

main()