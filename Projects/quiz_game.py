# Välkommen till (Måns födelsedags quiz)
# Vem spelar?
# 
# Q1: Hur gammal är måns? (Xår): [20år]   BQ: Vilket datum fyller han år? (MM/DD)                        2P max
# Q2: Vilka instrument kan Måns spela enligt honom själv? [piano, guitarr, sång] 3P max
# Q3: Vem var Måns största barndoms idol? [rackaralex/alexander hermansson]
# Q4: Vem vinner i armbrytning mellan Måns och player_name? efter allt input(rätt_svar) poäng eller inte
# Q5: Vart ska Måns göra sin NFK praktik i vår? [saab eller saab training]
# Q6: Hur många kusiner har Måns? (Xst): [11st]  BQ: Vem är äldst och vem är yngst? (äldst/yngst) [isac/sven]
#
# Hur tror du det gick?
# Har du någon hälsning du vill skicka till Måns? (skriv till en textfil)
#
# Visa resultatet (X/X antal rätt)
# Tack för att DU ville spela!
#
#QUIZZES FOLLOWING THIS STRUCTURE: NAME : x, questionNBR : {Question : Answer}

mans_quiz = {
    "quiz_name" : "Måns födelsedags QUIZ",
    "Q1" : {"Hur gammal är måns? (Xår):" : "20år"},
    "BQ1" : {"Vilket datum fyller han år? (MM/DD)" : "12/12"},
    "Q2" : {"Vilka instrument kan Måns spela enligt honom själv?" : ["piano", "guitarr", "sång"]},
    "Q3" : {"Vem var Måns största barndoms idol?" : ["rackaralex", "alexander hermansson"]},
    "Q4" : {"Vem vinner i armbrytning mellan Måns och player_name?" : "to_be_continued"},
    "Q5" : {"Vart ska Måns göra sin NFK praktik i vår?" : ["saab", "saab training"]},
    "Q6" : {"Hur många kusiner har Måns? (Xst):" : "11st"},
    "BQ6" : {"Vem är äldst och vem är yngst? (äldst/yngst)" : "isac/sven"},
}


#------------------------------------------


import random
import time
# tic = time.perf_counter()
# something to time
# toc = time.perf_counter()
# print(f"It took {toc - tic:0.4f} seconds") four decimals



def load_quiz(quiz_data):
    # Extract quiz name
    quiz_name = quiz_data.get("quiz_name", "Unnamed Quiz")

    #Extract all questions and answers
    questions = []
    for key, value in quiz_data.items():
        if key == "quiz_name":
            continue  # Skip the quiz name, we've already captured it

        # Each question key (like "Q1") contains a dictionary with one question-answer pair
        question_text = list(value.keys())[0]   # Get the question (value is a dict in this case)
        correct_answer = value[question_text]   # Get the answer

        # Store the question and answer in a tuple for easy access
        questions.append((question_text, correct_answer))

    # Return the quiz name and list of questions
    return quiz_name, questions



def run_quiz():
    # Unpack the result of load_quiz into quiz_name and questions in a single call
    quiz_name, questions = load_quiz(mans_quiz)
    
    #Display quiz name
    print(f"Welcome to {quiz_name}.")

    # Example loop through the questions, (den börjar inte om på första frågan vid omstart? jo vid slängning)
    for question_text, correct_answer in questions:
        print(question_text)
        player_answer = input("Your answer: ")


run_quiz()



