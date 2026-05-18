# Проект 4

# Калькулятор систем счисления

# Решение взято из комментариев

num_set = "0123456789abcdef"
base = int(input("Enter your base (2-16)\n"))
num = input(f"Enter your number in base {base} number system\n")[::-1]
res = 0
for i in range(len(num)):
    res += num_set.find(num[i].lower()) * (base**i)
print(f"Decimal number: {res}")
