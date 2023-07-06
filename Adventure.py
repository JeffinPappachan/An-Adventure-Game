name = input(" Type ypur name: ")
print("welcome", name ,"to this adventure!")
answer =input("Your are o a dirt road, it has come to an end and you can go left or right. which way would do you like to go? ").lower()
if answer == "left":
    answer=input("you came to  a river, you can walk around it or swim accross? type walk to walk and swim to swim accross: ").lower()
if answer =="swim":
    print("You swim across and were eaten by an alligator")
elif answer =="walk":
    print("you walked for many mile and ran out of water and you lost the game")
elif answer == "right":
    answer=input("The right turn have lead to a to a narrow road and further moving in to narrow leads to an valley. do you want to go down/top\n").lower()
if answer=="down":
   answer==input("you have reached the down of the valley.Their is a tent near by and would you like to visit their or sit down the valley. Sit/visit tent \n").lower()
elif answer =="sit":
    print("Your are sitting down the valley")
elif answer =="visit tent":
    print("you are visiting the tent near by and the people of that valley are very gratefull. they are giving you food to eat . you are eating their food and relaxing.  ")
elif answer=="top":
    answer =input("You have reached the top of the valley and their is beautiful apple tree.would you like you sit here and enjoy this beautiful nature. Yes/No").lower()
if answer=='yes':
    print("Your are sitting and enjoying the nice moment\n")
elif answer=="no":
    print("Your returing to your home ")    
else:
    print("The end")