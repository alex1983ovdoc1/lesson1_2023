answers = {
    'hello'         : 'Hello!',
    'how are you'   : 'Fine, and you?',
    'bye'           : 'See you later.'
    }

def get_answer(question, answers):
    return answers.ger(question)

def ask_user(answers):
    while True:
        user_input = input('Say anything:')
        answer = get_answer(user_input, answers)
        print(answer)

        if user_input == 'bye':
            break

if __name__=='__main__':
    ask_user(answers)