def hisobla_yigindi(*args):
    print(f"Kelgan ma'lumotlar: {args}")
    return sum(args)

print(hisobla_yigindi(2, 5))          # 7
print(hisobla_yigindi(10, 20, 30, 40)) # 100
