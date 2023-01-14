import pyinputplus as py
import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    question = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        
        py.inputStr(question, allowRegexes=['^%s$' % (num1 * num2)],blockRegexes=[('.*', 'Incorrect!')],timeout=8, limit=3)

    except py.TimeoutException:
        print('Out of time!')
    except py.RetryLimitException:
        print('Out of tries!')
    
    else:
        print('Correct!')
        correctAnswers += 1

    time.sleep(1)

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))