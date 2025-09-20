name_student  =  (input("What is your name: "))
sbj_student =  int(input("How many subjects did you write?: "))
grades = []
for  i in range(sbj_student):
    grade = float(input(f"Enter grade for the subject{i+1}: "))
    grades.append(grade)
print("grades entered:", grades)
minimum = min(grades)
maximum = max(grades)
average = sum(grades)/len(grades)

print("minimum grade:", minimum)
print("maximum grade:", maximum)
print("average:", average)


if average > 70:
    print (f"{name_student}, you had an excellent grade, congratulations 👏🏿👏🏿")
elif average < 70 and average > 35:
    print(f"{name_student}, your grade is fair enough but please put more effort😊")
else:
    print(f"{name_student}, you failed🥺, please work harder...remember this is not the end")