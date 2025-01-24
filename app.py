"""
1.存储学生的姓名和成绩。
2.计算学生的平均成绩。
3.找出成绩最高和最低的学生。
4.使用字典存储学生信息，使用集合去重成绩。
students_scores = {'zhangsan': 95, 'lisi': 80, 'wangwu': 75,'zhaoliu': 60, 'chenli': 80}
sum_scores = 0
score_list = []
num_students = len(students_scores)
for score in students_scores.values():
    score_list.append(score)
    sum_scores += score
print(set(score_list))
highest_score = max(score_list)
lowest_score = min(score_list)
name_higest_score = None
name_lowest_score = None
for name, score2 in students_scores.items():
    if score2 == highest_score:
            name_higest_score = name

    if score2 == lowest_score:
            name_lowest_score = name
print("The average score of the class is:", sum_scores/num_students)
print("The highest score is:", highest_score, "by", name_higest_score)
print("The lowest score is:", lowest_score, "by", name_lowest_score)
"""

"""
try:
  with open("students_scores.txt",'r') as file:
    lines = [line.strip().split(",") for line in file]
    number_of_students = []
    for row in lines:
        for i , i_value in enumerate(row):
            sum_scores = 0
            scores = []
            scores.append(str(row[0]))
            for x in range(1,len(row)):
                sum_scores += int(row[x])
            average_score = round((sum_scores/(len(row)-1)),2)
            scores.append(average_score)
        number_of_students.append(scores)
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error reading file")
with open("student_average_scores.txt","w") as file:
    for row in number_of_students:
        file.write(",".join(map(str,row)))
        file.write("\n")
        """

from Student import Student
caozuo = True
student1 = Student("John", 18, 85, 90, 80)
student2 = Student("Jane", 17, 75, 80, 70)
student3 = Student("Bob", 16, 65, 70, 60)
class_list = [student1, student2, student3]
while caozuo:
    print("1. show student information")
    print("2. sort student by score")
    print("3. delete student")
    print("4. add student")
    print("5. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print(class_list)
    if choice == "2":
        for student in class_list:
            
        print("1. sort by average score")
        print("2. sort by chinese score")
        print("3. sort by math score")
        print("4. sort by english score")
        sort_choice = input("Enter your choice: ")
        if sort_choice == "1":
            b = []
            for student in class_list:
               a = []
               a.append[student.name]
               average_score = (student.chinese + student.math +
                                student.english) / 3
               a.append(average_score)
               b.append(a)
            b.sort(key=lambda x: x[1],reverse=False)
            print(b)
        if sort_choice == "2":
            b = []
            for student in class_list:
               a = []


from openai import OpenAI