class Candidate:
    def __init__(self,name,cgpa,coding_score):
        self.name = name
        self.cgpa = cgpa
        self.coding_score = coding_score

    def is_eligible(self):
        if self.cgpa>=7 and self.coding_score>=60:
            return True
            
        else:
            return False

    def calculate_score(self):
        placement_score=self.cgpa*10+self.coding_score
        return placement_score

    def display_profile(self):
        print("Name:",self.name)
        print("CGPA:",self.cgpa)
        print("Coding Score",self.coding_score)
        print("Placement Score: ",self.calculate_score())
        print("Eligible: ",self.is_eligible())

        
        
        


candidate1 = Candidate("Shivraj",8.5,95)
candidate2= Candidate("Rahul",6.5,80)
candidate3= Candidate("Aman",8.0,55)

candidate1.display_profile()
candidate2.display_profile()
candidate3.display_profile()
 
# print(candidate1.is_eligible())
# print(candidate2.is_eligible())
# print(candidate3.is_eligible())

# print(candidate1.calculate_score())
# print(candidate2.calculate_score())
# print(candidate3.calculate_score())


# print(candidate1.name,candidate1.calculate_score())
# print(candidate2.name,candidate2.calculate_score())
# print(candidate3.name,candidate3.calculate_score())



