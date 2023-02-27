bottles_int = int(input("Ok how many green bottles do you want? "))
for number in range(bottles_int):
    print("There were "+str(bottles_int-number)+" green bottles, sitting on a wall.")
    print("Yes "+str(bottles_int-number)+ " green bottles, sitting on a wall.")
    print("And if one green bottle were to accidentally fall there would be " + str(bottles_int-number-1) + " green bottles sitting on the wall")
