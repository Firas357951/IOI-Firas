ch = str(input())
result = ''

for letter in ch:
   if letter == ' ':
      result += '_'
   else:
      result += letter 
print(result)