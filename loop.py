
head = "STUDENT'S GRANDING SYSTEM"
head1 = "COMPUTER SCIENCE"
head2 = "SEMESTER ONE"

print(head.center(100))
print(head1.center(100))
print(head2.center(100))
print("")
student_name = input("NAME: ")
reg_no = input("Reg.No: ")
print("")

num_courses = 4 # You can change this number if you want more or fewer courses
sum_credit_hours = 0
sum_grade_point = 0
for i in range(num_courses):
    course_unit = input("Course Unit: ")
    credit_hours = input("credit hours: ")
    x = float(input("mark obtained: "))
    y = (x/100)*5 # y= grade_point valñue
    grade_point = y * float(credit_hours)
   
    
    if y > 5:
        print("wrong grade point value. ")
        exit(0)
    elif y >= 4:
        print("GRADE: A")
    elif y >= 3.5:
        print("GRADE: B*")
    elif y >= 3:
        print("GRADE: B")
    elif y >= 2.5:
        print("GRADE: C*")
    elif y >= 2:
        print("GRADE: C")
    elif y >= 1.5:
        print("GRADE: D*")
    elif y >= 1:
        print("GRADE: D")
    else:
        print("GRADE: F")
        
print("")
sum_credit_hours += float(credit_hours)
sum_grade_point += grade_point
GPA = float(sum_grade_point) / float(sum_credit_hours )
print(f"GPA is{GPA}")

    