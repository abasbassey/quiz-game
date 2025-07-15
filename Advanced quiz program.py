#function to ask question and get input
def ask_question(question, correct_answer): #takes input (the question and it's correct answer)
    user_answer = input(question + "\nEnter answer here: ")  # Prints question, and gets answer on new line and stores in a var called user_answer
    if user_answer.lower() == correct_answer.lower(): #check if the answer is correct or not and lower makes both of them equal
        print("Correct")  # we printed and not returned because This would give an error because you're adding a string to an integer
        # score += 1  #changing the score value
        return 1
    else:
        print("Wrong")
        return 0
    
#list of (question, answer) pairs
quiz = [  #this is a list of tuples
      ("What is the capital of Nigeria?", "abuja"),
      ("What is the first month that starts with the letter 'J'?", "january"),
      ("What is the most populated city in Nigeria?", "lagos")
]

score = 0  # setting the score variable

for q, a in quiz: 
    score += ask_question(q, a)

print(f"Your final score is {score} out of {len(quiz)}")  # printing the score out. Len can be put in a variable called "Number of questions" and printed at the end also