def calculate_pyramid_height(number_of_blocks : int) -> int: 
     a=True
     b,c,d=0,0,0
   
     while a:
      b += 1
      if (b + c > number_of_blocks):
         a = False
      else:
         c += b  
         d += 1

     return d
n = int(input("Please enter a integer number : "))
a =calculate_pyramid_height(n)      
print(a)
