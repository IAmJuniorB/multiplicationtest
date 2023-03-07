import random

all_questions = []
score = 0
first_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# populate all possible questions in a list for random selection
for i in first_numbers:
    for j in second_numbers:
        all_questions.append([i, j])

num_questions = int(input("How many questions do you want to answer? "))
while num_questions <= 0 or num_questions > len(all_questions):
    num_questions = int(input("Please enter a positive integer less than or equal to {}: ".format(len(all_questions))))

# select random questions from all available options
questions = random.sample(all_questions, num_questions)

print("\nAnswer the following:\n")
for i, question in enumerate(questions):
    first_number, second_number = question
    answer = input(f"{i+1}) {first_number} x {second_number} = ")
    try:
        if int(answer) == first_number * second_number:
            score += 1
    except ValueError:
        pass  # ignore invalid answers

print("\nScore = {}/{}".format(score, num_questions))
input()
