eng=float(input("Enter Your English Number\n"))
urdu=float(input("Enter Your Urdu Number\n"))
mathematics=float(input("Enter Your Math Number\n"))
islamicStudies=float(input("Enter Your Islamic Studies Number\n"))
chemistry=float(input("Enter Your Chemistry Number\n"))
cs=float(input("Enter Your Computer Science Number\n"))
phy=float(input("Enter Your Physics Number\n"))
obtained_marks=eng+urdu+mathematics+islamicStudies+chemistry+cs+phy
print("Obatined Marks",obtained_marks)
percentage=obtained_marks/700*100
print("Percentage ",percentage )



if percentage >=80:
    print("A+")
elif percentage >=70:
    print("Grade A")
elif  percentage >=60:
    print("Grade B")
elif  percentage >=50:
    print("Grade C")
elif  percentage >=40:
    print("Grade D")
else:
    print("Fail")