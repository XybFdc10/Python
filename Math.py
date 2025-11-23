import random

def Is_math():
    l = [5, 6, 7, 8, 9]
    used_question = set()
    def random_nums():
        a = random.choice(l)
        b = random.choice(l)
        c = tuple(sorted([a, b]))
        return c

    for x in range(5):
        g = random_nums()
        while g in used_question:
            g = random_nums()
        used_question.add(g)
    new_list = [list(item) for item in used_question]
    a, b = new_list[0]
    c, d = new_list[1]
    e, f = new_list[2]
    g, h = new_list[3]
    i, j = new_list[4]
    while True:
        ans1 = a*b
        ans2 = c*d
        ans3 = e*f
        ans4 = g*h
        ans5 = i*j
        answer = []
        print("-----------------")
        print("| MATH QUESTION |")
        print("-----------------")
        print(f"What Is The Result Of {a} × {b}?")
        user_ans1 = int(input("Answer: "))
        print(f"What Is The Result Of {c} × {d}?")
        user_ans2 = int(input("Answer: "))
        print(f"What Is The Result Of {e} × {f}?")
        user_ans3 = int(input("Answer: "))
        print(f"What Is The Result Of {g} × {h}?")
        user_ans4 = int(input("Answer: "))
        print(f"What Is The Result Of {i} × {j}?")
        user_ans5 = int(input("Answer: "))
        if user_ans1 == ans1:
            answer.append(user_ans1)
        if user_ans2 == ans2:
            answer.append(user_ans2)
        if user_ans3 == ans3:
            answer.append(user_ans3)
        if user_ans4 == ans4:
            answer.append(user_ans4)
        if user_ans5 == ans5:
            answer.append(user_ans5)
        right_ans = len(answer)
        print("----------------")
        print("| YOUR ANSWER  |")
        print("----------------")
        print(f"Your Right Answer is {right_ans}/5")
        break

Is_math()    
