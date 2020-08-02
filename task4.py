""" write a program to take quiz and return how many questions are correctly answered """

def takeQuiz(questions):
    answers = []
    for question in questions:
            response = input(question+": ")
            answers.append(response)
    print('Quiz completed')
    return answers

def check_quiz(questions,key):
        count = 0
        answerslist = takeQuiz(questions)
        for i in range(len(key)):
                if key[i].lower() == answerslist[i].lower():
                        count += 1
        return f'You attempted {count} out of {len(key)} questions correctly'


questions = ['what is the capital of pakistan','when Pakitan established','who founder Pakistan']
key = ['Islamabad','1947','Quaid-e-Azam']
print(check_quiz(questions,key))
