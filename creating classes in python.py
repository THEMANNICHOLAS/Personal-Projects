
class TermPaper:
    def __init__(person, name, subject, grade):
        person.name = name
        person.subject = subject
        person.grade = grade
    
    def printTermPaper(person):
        print(person.name)
        print(person.subject)
        print(person.grade)
    
def setUser():
    name = input("What is your name?")
    return name

def setSubject():
    subject = input("What is your subject?")
    return subject

def setGrade():
    grade = input("What is your grade?")
    return grade

def main():
    p1 = TermPaper(setUser(), setSubject(), setGrade())
    print()
    p1.printTermPaper()

main()