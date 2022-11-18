#!/usr/bin/env python3
print("Welcome To 'How Well Do You Know Rap Artist J.Cole???'\n")

class Question:
    def __init__(self, prompt, answer): 
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What does the J in J. Cole's rap name stand for?\n(a) Jason\n(b) Jamie\n(c) Jermaine\n(d) Jackie\n\n", 
    "Where is J. Cole from?\n(a) New York, New York\n(b) Fayetteville, North Carolina\n(c) Chicago, Illinois\n(d) Memphis, Tennessee\n\n",
    "How tall is J. Cole?\n(a) 6'2\n(b) 6'3\n(c) 5'11\n(d) 6'7\n\n",
    "What was the name of J. Cole's first album?\n(a) The Come Up\n(b) From The Bottom\n(c) Thank Me Later\n(d) Born Sinner\n\n",
    "Which job title did J. Cole NOT work as before rapping?\n(a) A skating rink Kangaroo mascot\n(b) an ad salesman\n(c) a bill collector\n(d) a car salesman\n\n",
    "Which rapper shunned J. Cole before his rise to fame?\n(a) 50 cent\n(b) Nas\n(c) Jay Z\n(d) Kanye West\n\n",
    "How many grammys does J. Cole have?\n(a) 16\n(b) 2\n(c) 1\n(d) 5\n\n",
    "When was J. Cole born?\n(a) January 28, 1985\n(b) January 1, 1985\n(c) February 28, 1987\n(d) January 28, 1987\n\n",
    "How many kids does J. Cole have?\n(a) 3\n(b) 1\n(c) 2\n(d)He doesn't have any! Ha, you tried to trick me!\n\n",
    "Which song does J. Cole mention 'that Jada and Will love'?\n(a) No Role Models\n(b) Born Sinner\n(c) 4 Your Eyez Only\n(d) KOD\n\n",
    "Which comedian did J. Cole feature in one of his music videos?\n(a) Mike Epps\n(b) Desi Banks\n(c) Katt Williams\n(d) Kevin Hart\n\n"

]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "d"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "a"),
    Question(question_prompts[8], "c"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "d")

]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
            print("Correct! 'If you ain’t aim too high, then you aim too low!' +1 point\n")
        elif answer != question.answer:
            print("Sorry, wrong answer! 'It’s beauty in the struggle, ugliness in the success.' No points added\n")
    print("You scored", score, "out of", len(questions),"!")

run_quiz(questions)
