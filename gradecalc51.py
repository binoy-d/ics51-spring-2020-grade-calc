quizzes = []
labs = []
questionares = []
fin = 0.0
#enter your scores in this method as arrays of tuples(score, total)
def useHardCodedInput():
    global quizzes
    global labs
    global questionares
    global fin
    quizzes = [(6.67, 7), (1,5), (2, 4), (2.8, 4), (3, 4), (2, 4), (3, 3), (4,5), (5.5, 6), (4, 6), (5, 5)]#my grades are trash i know
    labs = [(2,2), (6,6), (6, 6), (10,10)]
    questionares = [(8.0, 10.0), (7.5, 10.0), (9.0, 10.0), (8.0, 10.0)]
    fin = 0.0

def getInput():
    global quizzes
    global labs
    global questionares
    global fin
    print("input quiz grades in format <score> <total> ex. '5 7'")
    print("input 'q' to quit")
    b = input()
    while(b!="q"):
        b = b.split()
        score = float(b[0])
        total = float(b[1])
        quizzes.append((score, total))
        b = input()


    print("quiz scores: ", quizzes)

    print("input lab grades in format <score> <total> ex. '5 7'")
    print("input 'q' to quit")
    b = input()
    while(b!="q"):
        b = b.split()
        score = float(b[0])
        total = float(b[1])
        labs.append((score, total))
        b = input()
    
    print("lab scores: ", labs)

    print("input questionare grades in format <score> <total> ex. '5 7'")
    print("input 'q' to quit")
    b = input()
    while(b!="q"):
        b = b.split()
        score = float(b[0])
        total = float(b[1])
        questionares.append((score, total))
        b = input()
    
    print("questionare scores: ", questionares)



def dropLowest(lst):
    return sorted(lst, key = lambda x: x[0]/x[1])[1:]



if __name__ == '__main__':
    hard = input("would you like to use your preset input, or enter input normally?(0 = preset, 1 = normal input)")
    if(hard == "0"):
        useHardCodedInput()
    else:
        getInput()
    
    quizzes = dropLowest(quizzes)
    questionares = dropLowest(questionares)

    print("*"*50)

    

    score = sum([a[0] for a in quizzes])#add up all scores
    total = sum([a[1] for a in quizzes])#add up all totals

    quizP = score/total

    score = sum([a[0] for a in labs])#add up all scores
    total = sum([a[1] for a in labs])#add up all totals

    labP = score/total

    score = sum([a[0] for a in questionares])#add up all scores
    total = sum([a[1] for a in questionares])#add up all totals
        
    questP = score/total
    
    grade = (0.3*quizP)+(0.3*labP)+(0.2*questP)+(0.2*fin)
    print(grade)
    

    print(f"quiz average: {quizP}")
    print(f"lab average: {labP}")
    print(f"questionare average: {questP}")
    print(f"final score: {fin}")
    print("*"*50)
    print("lets test out some different final grades!")
    print("*"*50)
    print("input a final percent, and ill give you your new grade\ninput q to quit")
    b = input()

    while(b!="q"):
        fin = float(b)
        grade = (0.3*quizP)+(0.3*labP)+(0.2*questP)+(0.2*fin)
        print(f"Your grade with a final score of {fin} would be {grade}")
        print("*"*50)
        b = input()

