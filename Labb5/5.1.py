with open('Labb5/text.txt' , 'r') as file:
    alphabet = [0] * 26

    text = file.read()


    number_of_words = len(text.split())
    number_of_sentances = len(text.split(". "))
    number_of_paragraphs = len(text.split("\n\n"))
    
    text = text.lower()
    for char in text:
        if char.isalpha():
            alphabet[ord(char) - ord("a")] += 1
    
    index_of_max = alphabet.index(max(alphabet))

    print(number_of_paragraphs)
    print(number_of_sentances)
    print(number_of_words)
    print(chr(index_of_max + ord("a")))
    