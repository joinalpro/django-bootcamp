class Studymart:
    def free_course(self):
        print('Python')
        #it's method now
    def free_course2(self):
        print('Django')

class AiQuest(Studymart):
    def course(self):
        print("ML")
    def course2 (self):
        print('DL')

a = Studymart()
a.free_course()

b = AiQuest()
b.course2()
b.course()