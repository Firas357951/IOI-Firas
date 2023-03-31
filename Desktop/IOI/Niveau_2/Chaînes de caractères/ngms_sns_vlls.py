Voyelle = ["A", "E", "I", "O", "U", "Y"]

title = str(input())
author = str(input())
List = [title, author]
for element in List:
   for letter in element:
      if (letter == " ") or  (letter in Voyelle):
         pass
      else:
         print(letter, end='')
   print()