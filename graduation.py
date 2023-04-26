sum_grades = 0
failed = 0
excluded = False

name = input()
grade = float(input())
grade_count = 1

while grade_count <= 12:
    if grade >= 4.00:
        sum_grades += grade
        grade_count += 1
        if grade_count > 12:
            break
    else:
        failed += 1
        if failed > 1:
            excluded = True
            print(f"{name} has been excluded at {grade_count} grade")
            break

    grade = float(input())

if not excluded:
    avg_grade = sum_grades / 12
    print(f"{name} graduated. Average grade: {avg_grade:.2f}")
