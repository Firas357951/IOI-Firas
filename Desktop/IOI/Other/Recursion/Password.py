Pass = '123456'

def Verify():
    Try = input()
    while Try != Pass:
        Try = Verify()
        #print(Try, Pass)
    return Try

print(Verify())