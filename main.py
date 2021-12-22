answer = int(input("сколько вишен вы хотите съесть?"))
if answer == 1 or answer == 21:
    print(answer,"вишню")
elif answer > 1 and answer < 5:
    print(answer, "вишни")
elif answer > 4 and answer < 21:
    print(answer, "вишен")
else:
    print("эй! это годовой запас вишни")