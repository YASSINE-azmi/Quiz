from Quiz import quiz

my_quiz = quiz()
score:int = 0

print("-"*40)
print("               Start the Quiz")
print("-"*40)
score += int(my_quiz.quiz1())
print("-"*40)
score += int(my_quiz.quiz2())
print("-"*40)
score += int(my_quiz.quiz3())
print("-"*40)
score += int(my_quiz.quiz4())
print("-"*40)
score += int(my_quiz.quiz5())
print("-"*40)
score += int(my_quiz.quiz6())

print(f"Your score is {((score*100)/6):.2f}%")

