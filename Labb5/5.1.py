def file_analyzer1():
    with open('text.txt' , 'r') as file:
        number_of_paragraphs = 1
        number_of_sentances = 0
        number_of_words = 0

        for line in file:
            #New line equals add a paragraph
            if line.isalpha == True:
                number_of_paragraphs += 1

            for char in line:
                
            


        #number of words (hitta space och sedan nästa space)


        #number of sentences (uppercase efter ett space, till punkt och sedan space.)


        #number of paragraphs


        #which letter is most used?

                return 
    




with open('text.txt' , 'r') as file:
    number_of_paragraphs = 0
    number_of_sentances = 0
    number_of_words = 0
    for line in file:
        #New line equals add a paragraph
        if line.isalpha == True:
            number_of_paragraphs += 1
        
print(number_of_paragraphs)
