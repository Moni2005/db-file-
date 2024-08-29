math = int(input("Enter your marks: "))
sci = int(input("Enter your marks: "))
sst = int(input("Enter your makrs: "))
eng = int(input("Enter your marks: "))
tam = int(input("Enter your marks: "))

avg_marks = (math+sci+sst+eng+tam)/5
print(avg_marks)
if(avg_marks < 35):
    print("Extra classes needed")
else:
    print("You are good to go!")
