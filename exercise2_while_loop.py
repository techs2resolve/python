name = input("Enter your name:- ")
namelength = len(name)

tmp_variable = ""
i=0

while i < namelength :
    if name[i] not in tmp_variable:
        tmp_variable += name[i]
        print(f"{name.count(name[i])} : {name[i]}")
    i += 1
