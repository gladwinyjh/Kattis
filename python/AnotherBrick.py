def main():
   h, w, n = map(int, input().split())
   bricks = list(map(int, input().split()))
   
   for i in range(h):
       # Start of new layer, current layer width = w
       width = w
       for j in range(n):
           # Take current brick and lay it
           # Remove that brick from bricks
           width -= bricks.pop(0)
           # If laying current brick completes layer
           if width == 0:
               # If already at top height
               if i == h-1:
                   print('YES')
               # Move to next height
               break
           # If current brick is too long for remaining width
           elif width < 0:
               print('NO')
               return
           # There is still some width after laying current break
           # Move to next brick in bricks
           else:
               continue



if __name__ == '__main__':
    main()