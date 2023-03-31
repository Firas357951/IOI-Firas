for bloc in range(8):
   for lig in range(16):
      for col in range(8):
         code = 128 * bloc + 16 * col + lig
         caractere = chr(code)
         if code < 32:
            caractere = " "
         print("{:04d} {}  ".format(code, caractere), end = "")
      print()
   print()