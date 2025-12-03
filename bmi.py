def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print ("Weight = "+ str(weight))
    bmi = weight/(height*height)
    print ("BMI=" , f"{bmi : .3f}")

    if bmi < 18.5:
        print ("The person is UnderWeight")
    elif 18.5<= bmi <= 25.0:
        print ("This person is normal weight")
    else:
        print("this person is over weight")

while True:
    user_weight = float(input ("Enter ur weight = "))
    user_height = float(input ("Enter ur height = "))
    bmi = (user_weight)/(user_height*user_height)
    print ("Your bmi is =", f"{(bmi) : .3f}" )

    if bmi < 18.5:
        print ("U R so thin, Don't U eat Anything????")
    elif 18.5<= bmi <= 25.0:
        print ("Ummm U have a healthy diet, not BAD :>")
    else:
        print("U FAT ASS!!!")



#calculate_bmi(height =1.73, weight = 57) 