class QuizBrain:
    def __init__(self,q_list):
        self.question_number_count =  0
        self.question_list = q_list 
    
    def is_correct(self,response):
        current_question = self.question_list[self.question_number_count]
        if current_question.answer == response:
            return True
        else:
            return False

    def is_question_left(self):
        return self.question_number_count<len(self.question_list)
           
        
    def next_question(self):
        current_question = self.question_list[self.question_number_count]
        self.question_number_count += 1
        return input(f"Q.{self.question_number_count}: {current_question.text}? (True/False):")