#Import dependencies

import os
import csv

#Import CSV

csvpath = os.path.join("Resources/budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#Establish Variables

    counter = 0
    counter_2 = 0
    largest = 0
    smallest = 0
    average = []
    newav = []
    months = []

#Assign values to variables

    for row in csvreader:
        counter = counter + 1
        counter_2 = counter_2+float(row[1])
        average.append(int(row[1]))
        months.append(row[0])

    cur=0
    nxt=0
    l = 0
    s=0

    for i in range(len(average)-1):
        cur=average[i]
        nxt=average[i+1]
        newav.append(nxt-cur)

        if largest < float(nxt-cur):
            largest = float(nxt-cur)
            l=i+1

        if smallest > float(nxt-cur):
            smallest = float(nxt-cur)
            s=i+1

    finav=sum(newav)/len(newav)

#Formatting

    counter_2="${:,.2f}".format(counter_2)
    finav="${:,.2f}".format(finav)
    largest="${:,.2f}".format(largest)
    smallest="${:,.2f}".format(smallest)

#Print results

    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(counter))
    print("Total: " + str(counter_2))
    print("Average Change: " + str(finav))
    print("Greatest Increase in Profits: " + months[l] + " " + str(largest))
    print("Greatest Decrease in Profits: " + months[s] + " " + str(smallest))

#Write to .Txt file

    f = open("Financial_Analysis.txt", "w")
    f.write("Financial Analysis\n")
    f.write("------------------------\n")
    f.write("Total Months: " + str(counter) + "\n")
    f.write("Total: " + str(counter_2) + "\n")
    f.write("Average Change: " + str(finav) + "\n")
    f.write("Greatest Increase in Profits: " + months[l] + " " + str(largest) + "\n")
    f.write("Greatest Decrease in Profits: " + months[s] + " " + str(smallest))