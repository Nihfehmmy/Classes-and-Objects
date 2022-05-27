class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name ,age, track,score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def _repr_(self):
        return f"Studeny(name={self.name}, age={self.age}, track={self.track}, score={self.score}"

    def change_name(self, name):
        return self.name
        
    def change_age(self, age):
        return self.age 
    def add_track(self, track):
        return self.track 
    def get_score(self):
        return self.score 

    def display(self):
        print("name:", self.name)
        print("age:",self.age)
        print("tracks:",self.track)
        print("score:",self.score)
        return self



Bob = Student(name="Bob", age=26, score=24, track=20.90);
Bob.display();

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
