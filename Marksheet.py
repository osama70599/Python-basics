marks = []
subjetcs = int(input("Enter Total number of subjects")) #this will help making markesheet flexible
for i in range(subjetcs):
    print("Enter marks of ",i+1," Subect.")
    num = int(input())
    marks.append(num)

total = subjetcs*100
sum = sum(marks)
percentage =  (sum*100)/total
grade = lambda percentage : 'A+' if percentage >= 80 and percentage <= 100 else ('A' if percentage >= 70 and percentage < 80 else ('B' if percentage >= 60 and percentage < 70 else ('C' if percentage >= 50 and percentage < 60 else ('D' if percentage >= 40 and percentage < 50 else 'Fail'))))
print("\t***Mark Sheet***")
for i in range(subjetcs):
    print("Marks of ",i+1,"Subject :",marks[i])
print("\nTotal makrs obtained : ",sum)
print("Percentage : ",percentage)
print("Grade : ",grade(percentage))

