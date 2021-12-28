answer = int(input("сколько вишен вы хотите съесть?"))
if answer>=11 and answer<=14 or answer%10==0 or answer%10>=5 and answer%10<=9:
    print(answer, "вишен")
elif answer%10==1:
    print(answer,"вишню")
else:
    print(answer, "вишни")



