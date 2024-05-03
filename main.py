def capture_book():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
        
def capture_words(text_dump):
    words_in_text = []
    words_in_text = text_dump.split()

    words = len(words_in_text)
    return words

def capture_letters(text_dump):
    each_letter = [
        {'letter': 'a', 'num': 0}, {'letter': 'b', 'num': 0}, {'letter': 'c', 'num': 0}, {'letter': 'd', 'num': 0}, {'letter': 'e', 'num': 0}, {'letter': 'f', 'num': 0},
        {'letter': 'g', 'num': 0}, {'letter': 'h', 'num': 0}, {'letter': 'i', 'num': 0}, {'letter': 'j', 'num': 0}, {'letter': 'k', 'num': 0}, {'letter': 'l', 'num': 0},
        {'letter': 'm', 'num': 0}, {'letter': 'n', 'num': 0}, {'letter': 'o', 'num': 0}, {'letter': 'p', 'num': 0}, {'letter': 'q', 'num': 0}, {'letter': 'r', 'num': 0},
        {'letter': 's', 'num': 0}, {'letter': 't', 'num': 0}, {'letter': 'u', 'num': 0}, {'letter': 'v', 'num': 0}, {'letter': 'w', 'num': 0}, {'letter': 'x', 'num': 0},
        {'letter': 'y', 'num': 0}, {'letter': 'z', 'num': 0}
    ]
    other = 0
    lower_text = text_dump.lower()
    for i in lower_text:
        for x in each_letter:
            if x['letter'] == i:
                x['num'] += 1
    each_letter.sort(key=lambda x: x['num'], reverse=True)        

    return each_letter, other


    
    

def main():
    book = capture_book()
    num_words = capture_words(book)
    num_letters, num_others = capture_letters(book)

    print(f'This file contains {num_words} words!')
    for i in num_letters:
        print(f'There are {i['num']} {i['letter']} in this file!')

main()



