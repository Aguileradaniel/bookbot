def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
        print_report(file_contents,filepath)

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
        return_list.append({"char":char,"count":dict[char]})
    return return_list

def order_char_list(char_list:list[dict])->list[dict]:
    order_fn = lambda dict : dict["count"]
    char_list.sort(reverse=True,key=order_fn)
    return char_list

def print_report(book:str, path:str)->None:
    wordcount = count_words(book)
    charlist = order_char_list(dict_to_list_of_dicts(count_chars(book)))

    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document")

    for charcount in charlist:
        if charcount["char"].isalpha():
            print("The '" + charcount["char"] + "' character was found " + str(charcount["count"]) + " times")
    
    print("--- End report ---")

main()