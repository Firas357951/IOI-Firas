matrix = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', 'O', '#', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '#', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '#', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', 'x', '.', '.', '.', '.', '.', '#', '#', '#'], ['#', '#', 'x', '.', '.', '.', '.', '.', '.', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '#', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '.', '#'], ['#', 'x', '.', '.', '.', '.', '.', '.', '#', '#'], ['#', 'O', '#', '#', '#', '#', '#', 'O', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
for line in range(13):
    for col in range(10):
        print(matrix[line][col], end='')
    print()

direction = ['E', 'S', 'N', 'O', 'S', 'E', 'S', 'N']

def main():   
   def Next_pos(pos, dir):
       return (pos[0] + dir[0], pos[1] + dir[1])
   def stop(Wall):
       for element in Wall:
           if not(element):
               return False
       return True
   def find_ball(pos):
       try:
           return Ball_Pos.index(pos)
       except:
           return None
       
   L, C = map(int, input().split())
   #matrix = []
   #for _ in range(L):
    #   line = list(input())
    #   matrix.append(line)
   N = int(input())
   if N < 40:
    #  direction = list(input())
      dict = {
          'N' : (-1, 0),
          'E' : (0, 1),
          'S' : (1, 0),
          'O' : (0, -1)
      }
      
      Ball_Pos = []
      for line in range(L):
          for col in range(C):
              if matrix[line][col] == 'x':
                  Ball_Pos.append((line, col))
                  
      for dir in direction:
          dir = dict[dir]
          Wall = [False] * len(Ball_Pos)
          if Ball_Pos == [None] * len(Ball_Pos):
              return 0
          while not(stop(Wall)): 
              for idx, ball in enumerate(Ball_Pos):
                  if ball != None:
                      x, y = Next_pos(ball, dir)
                      if matrix[x][y] == '#':
                          Wall[idx] = True
                      elif matrix[x][y] == 'O':
                          Wall[idx] = True
                          Ball_Pos[idx] = None
      
              for idx, ball in enumerate(Ball_Pos):
                  if ball != None:
                      x, y = Next_pos(ball, dir)
                      if not(Wall[idx]):
                          i = find_ball((x,y))
                          if (i == None) or (i != None and not(Wall[i])):
                              Ball_Pos[idx] = Next_pos(ball, dir)
                          else:
                              Wall[idx] = True
              print(Ball_Pos, Wall, dir)
                                      
      n = 0            
      for element in Ball_Pos:
         if element != None:
            n += 1
      return n
   else:
      print(L,C, matrix)
   
print(main())