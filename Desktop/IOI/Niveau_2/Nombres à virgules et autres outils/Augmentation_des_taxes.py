tax1 = float(input())/100
tax2 = float(input())/100
price = float(input())

result = (price/(1+tax1)) * (1+tax2)
print(round(result * 100) / 100)