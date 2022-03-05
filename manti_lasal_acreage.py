import csv

def sum_acreage(acreages):
    totsum = 0
    for i in range(0,len(acreages)):
        totsum = totsum + acreages[i]
    return totsum

def average_acreage(acreages):
    average = sum_acreage(acreages)/len(acreages)
    return average

def acreage_vals(acreages, area):
    for i in range (0, len(acreages)):
        if area == dict(acreages[i])["Name"]:
            return dict(acreages[i])["Acreage"]

lafile = open(r"C:\Users\abhii\Desktop\Github\Manti-La-Sal-Acreage\lasal_acreage.csv")
drdr = csv.DictReader(lafile)
acreages_and_names = [line2 for line2 in drdr]
acreages = [float((dict(line)["Acreage"])) for line in acreages_and_names]
ival = 0

while ival != '4':
    print('Lasal Acreage Information Center')
    print('1 - Average Acreage of All Areas')
    print('2 - Sum of Acreage of all Areas')
    print('3 - Specific Acreage Values')
    print('4 - Exit Program')

    ival = input("Enter an option: ")
    if ival == '1':
        print(average_acreage(acreages))
    elif ival == "2":
       print(sum_acreage(acreages))
    elif ival == "3":
       area_name = input("Enter an area: ")
       print(acreage_vals(acreages_and_names, area_name))
    elif ival == "4":
        x = 1

