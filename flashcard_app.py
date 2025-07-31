flashcards = {
    "Python": "A programming language",
    "HTML": "Markup language for web",
    "AI": "Artificial Intelligence",
}

for term, definition in flashcards.items():
    ans = input(f"What is {term}? ")
    if ans.lower() == definition.lower():
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect. Answer: {definition}")
