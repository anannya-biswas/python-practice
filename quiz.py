questions = {
    "What is the capital of India?": "Delhi",
    "What is 5 + 7?": "12",
    "Which programming language is used for AI?": "Python"
}

score = 0
for question, answer in questions.items():
    user_ans = input(question + " ")
    if user_ans.strip().lower() == answer.lower():
        print("Correct ✅")
        score += 1
    else:
        print(f"Wrong ❌ The correct answer is {answer}")

print(f"\nYour final score: {score}/{len(questions)}")
