from io import StringIO
import sys

input1 = """7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00"""
input2 = """4
Scott 4.50
Ted 3.00
Scott 5.00
Ted 3.66"""
input3 = """5
Lee 6.00
Lee 5.50
Lee 6.00
Peter 4.40
Kenny 3.30
"""
# sys.stdin = StringIO(input1)
# sys.stdin = StringIO(input2)
sys.stdin = StringIO(input3)

number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students:
        students[student] = [float(grade)]
    else:
        students[student].append(float(grade))

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = " ".join(str(f"{x:.2f}") for x in grades)
    print(f"{student} -> {grades_str} (avg: {avg_grade:.2f})")
