#Import dependencies

import os
import csv

#Import CSV

csvpath = os.path.join("Resources/election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#Establish variables

    counter = 0
    KhanCounter = 0
    CorreyCounter = 0
    LiCounter = 0
    OTooleyCounter = 0

#Assign values to variables

    for row in csvreader:
        counter = counter + 1

        if row[2] == "Khan":
            KhanCounter = KhanCounter + 1
        elif row[2] == "Correy":
            CorreyCounter = CorreyCounter + 1
        elif row[2] == "Li":
            LiCounter = LiCounter + 1
        else:
            OTooleyCounter = OTooleyCounter + 1


#Formatting
   
    Khanpct = "{:.3%}".format(KhanCounter/counter)
    Correypct = "{:.3%}".format(CorreyCounter/counter)
    Lipct = "{:.3%}".format(LiCounter/counter)
    OTooleypct = "{:.3%}".format(OTooleyCounter/counter)

#Determine the winner

    if Khanpct>Correypct and Khanpct>Lipct and Khanpct>OTooleypct:
        winner = "Khan"
    elif Correypct>Khanpct and Correypct>Lipct and Correypct>OTooleypct:
        winner = "Correy"
    elif Lipct>Correypct and Lipct>Khanpct and Lipct>OTooleypct:
        winner = "Li"
    else:
        winner = "O'Tooley"
    
#Print results

    print(str("Election Results"))
    print(str("-----------------------------"))
    print(str("Total Votes = ") + str(counter))
    print(str("-----------------------------"))
    print(str("Khan ") + str(Khanpct) + " " + str(KhanCounter))
    print(str("Correy ") + str(Correypct) + " " + str(CorreyCounter))
    print(str("Li ") + str(Lipct) + " " + str(LiCounter))
    print(str("O'Tooley ") + str(OTooleypct) + " " + str(OTooleyCounter))
    print(str("-----------------------------"))
    print(str("Winner: " + str(winner)))
    print(str("-----------------------------"))

#Write to .Txt file

    f = open("Election_Results.txt", "w")
    f.write("Election Results\n")
    f.write("-----------------------------\n")
    f.write("Total Votes = " + str(counter) + "\n")
    f.write("-----------------------------\n")
    f.write("Khan " + str(Khanpct) + " " + str(KhanCounter) + "\n")
    f.write("Correy " + str(Correypct) + " " + str(CorreyCounter) + "\n")
    f.write("Li " + str(Lipct) + " " + str(LiCounter) + "\n")
    f.write("O'Tooley " + str(OTooleypct) + " " + str(OTooleyCounter) + "\n")
    f.write("-----------------------------\n")
    f.write("Winner: " + str(winner) + "\n")
    f.write("-----------------------------")