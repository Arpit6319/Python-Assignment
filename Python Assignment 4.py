#Break:-
#numbers = [1, 2, 3, 4, 5]
#for num in numbers:
#    if num == 3:
#        break
#   print(num)
    
#Pass:-
#for i in range(5):
 #   pass
  #  print("This line is still executed.")

#Continue
#numbers = [1, 2, 3, 4, 5]
#for num in numbers:
 #   if num == 3:
  #      continue
   # print(num)

#For with else
#numbers = [1, 2, 3, 4, 5]
#for num in numbers:
 #   if num == 6:
  #      break
    #print(num)
#else:
 #   print("All numbers were printed successfully.")

#While with else
count = 0

while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("Loop completed successfully.")
