def bubblesort(list):

# Swap the elements to arrange in order

     for iter_num in range(len(list)-1,0,-1):
          for idx in range(iter_num):
               if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp

   list = [1,3,42,6,3,8,5,6]
bubblesort(list)
print(list)                     