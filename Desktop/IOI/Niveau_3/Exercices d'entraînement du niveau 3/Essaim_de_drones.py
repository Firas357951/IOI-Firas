## This Python code is the best optimized solution found by me and pass 70% of tests with complexity O(L*C + nbpoints²) in order to pass the rest of \\
# tests we need to translate the code to C++ which is much faster than python.
import sys

def main():
    inp = sys.stdin.readline
    L, C = map(int, inp().split())
    
    Im1=[inp().split() for _ in range(L)]
    Im2=[inp().split() for _ in range(L)]
    Pos_Im1 = [(i,j) for i in range(L) for j in range(C) if Im1[i][j]=='1']
    Pos_Im2 = [(i,j) for i in range(L) for j in range(C) if Im2[i][j]=='1']
          
    T = [[0] * (2*C-1) for _ in range(2*L-1)]
    max = 0
    for point1 in Pos_Im1:
        for point2 in Pos_Im2:
            x = point2[0] - point1[0]
            y = point2[1] - point1[1]
            T[x][y] += 1
            if T[x][y] > max:
                max = T[x][y]
                i, j = x, y

    print(max)
    image = set()
    for point in Pos_Im1:
        x = point[0] + i
        y = point[1] + j
        image.update({(x, y)})
    result = image.intersection(set(Pos_Im2))
    for element in result:
        print(element[0]+1, element[1]+1)
main()


## This is the solution in C++
"""
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX_SIDE = 500;

struct Point
{
  int lin;
  int col;

  Point(int lin, int col) : lin(lin), col(col) {}
};

vector<Point> points[2];
int nbOccurDepl[MAX_SIDE * 2][MAX_SIDE * 2];

int main()
{
   int nbLins, nbCols;
   scanf("%d%d", &nbLins, &nbCols);
   for (int img = 0; img < 2; img++)
      for (int lin = 0; lin < nbLins; lin++)
         for (int col = 0; col < nbCols; col++)
         {
            int type;
            scanf("%d", &type);
            if (type == 1)
               points[img].push_back(Point(lin, col));
         }
   int maxOccur = 0;
   int maxDLin = 0;
   int maxDCol = 0;
   for (int pt1 = 0; pt1 < points[0].size(); pt1++)
      for (int pt2 = 0; pt2 < points[1].size(); pt2++)
      {
         Point point1 = points[0][pt1];
         Point point2 = points[1][pt2];
         int dLin = point2.lin - point1.lin;
         int dCol = point2.col - point1.col;
         int & nbOccur = nbOccurDepl[dLin + MAX_SIDE][dCol + MAX_SIDE];
         nbOccur++;
         if (nbOccur > maxOccur)
         {
            maxOccur = nbOccur;
            maxDLin = dLin;
            maxDCol = dCol;
         }
      }
   printf("%d\n", maxOccur);
   for (int pt1 = 0; pt1 < points[0].size(); pt1++)
      for (int pt2 = 0; pt2 < points[1].size(); pt2++)
      {
         Point point1 = points[0][pt1];
         Point point2 = points[1][pt2];
         int dLin = point2.lin - point1.lin;
         int dCol = point2.col - point1.col;
         if ((dLin == maxDLin) && (dCol == maxDCol))
            printf("%d %d\n", point2.lin + 1, point2.col + 1);
      }
   return 0;
}
"""