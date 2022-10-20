# dictionary that stores Q&A
# variable that tracks the score of player
# loop through the dictionary using the key value pairs
# display each question to the user and allow them to answer
# tell them if right/wrong
# show the final result when quiz is completed


quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of United States?",
        "answer": "Washington D.C."
    },
    "question3": {
        "question": "What is the capital of U.K.?",
        "answer": "London"
    },
    "question4": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question5": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question6": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    }
}

playerScore = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('Correct')
        playerScore = playerScore + 1
        print(f"Your score is now {playerScore}!")
    else:
        print('Wrong answer!')
        print('The answer is: ' + value['answer'])
        print(f'Your score is now {playerScore}!')
