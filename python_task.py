str = input("Введите строку: ")
found = False
for i in range(len(str)):
    if str[i] not in str[:i] + str[i+1:]:
        print("Первый неповторяющийся символ:", str[i])
        found = True
        break
if not found:
    print("Все символы повторяются.")
