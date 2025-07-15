# basic quiz progam
quest1 = "What is the capital of Nigeria?"
quest2 = "What is the first month that starts with the letter 'J'?"
quest3 = "What is the most populated city in Nigeria?"
score = 0
print(quest1)
quest1Ans = input("Enter answer here: ")
if quest1Ans.lower() == "abuja":  #put the lower there and remove the caps in "Abuja"
    print("Correct")
    score += 1 #adding score
else:
    print("Wrong")
print(quest2)
quest2Ans = input("Enter answer here: ")
if quest2Ans.lower() == "june":  #put the lower there and remove the caps in "june"
    print("Correct")
    score += 1  #adding score
else:
    print("Wrong")
print(quest3)
quest3Ans = input("Enter answer here: ")
if quest3Ans.lower() == "lagos":  #put the lower there and remove the caps in "lagos"
    print("Correct")
    score += 1  #adding score
else:
    print("Wrong")
print(f"Your final score is {score} out of 3.")