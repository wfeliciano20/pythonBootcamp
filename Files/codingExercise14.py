"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
questions_file = open('questions.txt', 'r')
questions = [line.strip() for line in questions_file.readlines()]
questions_file.close()

answers = []
solutions = []
for question in questions:
    question, solution = question.split('=')
    solutions.append(solution)
    answer = input(f'{question}=')
    answers.append(answer)

score = 0
total = len(questions)

for i in range(len(solutions)):
    if solutions[i] == answers[i]:
        score = score + 1

print(f'Your final score is {score}/{total}.')
result_file = open('result.txt', 'w')
result_file.write(f'Your final score is {score}/{total}.')
result_file.close()
