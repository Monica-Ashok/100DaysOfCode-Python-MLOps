#TODO: Create a class called QuizBrain
#TODO: Initialize the quiz brain
#TODO: Initialize the question number
#TODO: Initialize the question list
#TODO: Create a method called next_question
#TODO: Retrieve the item in the question_list based on the question_number
#TODO: Use the input() function to show the user the question text
#TODO: Create a method called still_has_questions
#TODO: Check if the question_number is less than the length of the question_list
#TODO: If it is, return True, otherwise return False
#TODO: While loop to keep the quiz running
#TODO: Create a method called check_answer
#TODO: Check if the user's answer is correct
#TODO: If it is, print "You got it right!"
#TODO: If it is, print "That's wrong."
#TODO: Print the correct answer
#TODO: Print the user's answer
#TODO: Print the user's score


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list= question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")






