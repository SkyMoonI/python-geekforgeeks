# sort() method = used with lists
# sort() function = used with iterables

# studentsList = ["bstudent2", "cstudent3", "astudent1", "dstudent4"]
#
# studentsList.sort()
# studentsList.sort(reverse=True)
#
# for student in studentsList:
#    print(student)

# studentsTuple = ("bstudent2", "cstudent3", "astudent1", "dstudent4")
## studentsTuple.sort() # wont work with tuple
#
# sorted_studentsTuple = sorted(studentsTuple)
# sorted_studentsTuple = sorted(studentsTuple,reverse=True)
#
# for student in sorted_studentsTuple:
#    print(student)

#students = [("1", "F", 60), ("3", "A", 30), ("2", "D", 40), ("5", "B", 20), ("4", "C", 70)]
#students.sort()
#students.sort(reverse=True)
#
#students.sort(key=lambda x: x[0])
#students.sort(key=lambda x: x[1])
#students.sort(key=lambda x: x[2])
#students.sort(key=lambda x: x[2], reverse=True)
#
#for student in students:
#   print(student)

#students = (("1", "F", 60), ("3", "A", 30), ("2", "D", 40), ("5", "B", 20), ("4", "C", 70))
#sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
#
#for student in sorted_students:
#    print(student)
