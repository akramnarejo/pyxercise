""" write a program to ask users for their name and answers to the questions until they don't want to quit and then make a dictionary of the responses
    where key must be the user's name """

responses = {}
polling_active = True
questions = ['Which mountain would you like to climb someday? ', 'Which city would you like to visit someday? ']

while polling_active:
        answers = []
        name = input('Enter your name: ')
        for question in questions:
            response = input(question)
            answers.append(response)
            responses[name] = answers
            repeat = input('Would you like to answer more? (yes/no) ')
            if repeat == 'no':
                polling_active = False
                break
        print('Polling completed')
print(responses.items())
