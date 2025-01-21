with open("books/frankestain.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    c_words = len(words)
    low_content = file_contents.lower()
    frankestain = {}
    
    for letter in low_content:
        if letter.isalpha():
            if letter not in frankestain:
                frankestain[letter] = 1
            else:
                frankestain[letter] += 1
    
    # Ordenar e criar uma lista de tuplas em vez de dicionários individuais
    sorted_letters = sorted(frankestain.items(), key=lambda item: item[1], reverse=True)
    
    # Exibir o relatório
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{c_words} words found in the document!")
    print("")
    
    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times.")
    
    print("--- End report ---")










