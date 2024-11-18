import json

with open("questions/question.json") as file:
    content = file.read()

data = json.loads(content)

SCORE = 0

for questions in data:
    print(questions["Qtext"])
    for answers in questions["Options"]:
        print(answers)
    user_answer = input("Enter your answer : ")
    questions["user_answer"]  = user_answer


for ii,question in enumerate(data):
    message = f"{ii+1} - Your answer : {question['user_answer']} \nCorrect answer : {question['Answer']}"
    if question['user_answer'] == question['Answer']:
        SCORE += 1
        print("Correct",end=" ")
    else:
        print("Incorrect", end=" ")
    print(message)
print(f"Score is : {SCORE}/{len(data)}")