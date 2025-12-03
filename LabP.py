print("ET0735 - lab test practice")

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas(eg.5,67,32)")


def get_user_input():
    arrayList =[]
    print("get_user_input")
    itemstring = input("Enter a number")
    numList = itemstring.split(",")
    for eachnum in numList:
        arrayList.append(float(eachnum))
    print(arrayList)
    return arrayList




def calc_average(numlist):
    print("calc_average")
    total = sum(numlist)
    avg = total / len(numlist)
    print ("average =" , float(avg))
    return avg


def sort_temperature(numlist):
    print("sort_temperature")
    templist = numlist.copy()
    templist.sort()
    print ("Sorted number are ", templist)
    return templist
   

def find_min_max(numlist):
    print("find_min_max")
    array=[]
    templist = sort_temperature(numlist)
    min = templist[0]
    array.append(min)
    max = templist[-1]
    array.append(max)

    print ("Min and Max =", array )
    return array







def main():
    numlist=get_user_input()
    calc_average(numlist)
    sort_temperature(numlist)
    find_min_max(numlist)



if __name__ == "__main__":
 main()