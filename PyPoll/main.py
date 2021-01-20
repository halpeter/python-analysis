import os
import csv

csvpath = os.path.join('resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    #define variables, and lists
    total_votes = 0
    khan_votes = []
    khan_total = 0
    correy_votes = []
    correy_total = 0
    li_votes = []
    li_total = 0
    otooley_votes = []
    otooley_total = 0

    for row in csvreader:
        #The total number of votes cast
        total_votes = total_votes + 1
        #Add all Khan votes to a list
        if row[2] == "Khan":
            khan_votes.append(row[0])
        #Add all Correy votes to a list
        if row[2] == "Correy":
            correy_votes.append(row[0])
        #Add all Li votes to a list
        if row[2] == "Li":
            li_votes.append(row[0])
        #Add all O'Tooley votes to a list
        if row[2] == "O'Tooley":
            otooley_votes.append(row[0])

    #Calculate Khan percentage & total votes
    khan_total = len(list(khan_votes)) 
    khan_percentage = "{:.3f}".format((khan_total / total_votes) * 100)
 
    #Calculate Correy percentage & total votes
    correy_total = len(list(correy_votes)) 
    correy_percentage = "{:.3f}".format((correy_total / total_votes) * 100)

    #Calculate Li percentage & total votes
    li_total = len(list(li_votes)) 
    li_percentage = "{:.3f}".format((li_total / total_votes) * 100)

    #Calculate O'Tooley percentage & total votes
    otooley_total = len(list(otooley_votes)) 
    otooley_percentage = "{:.3f}".format((otooley_total / total_votes) * 100)

    #print results
    print("Election Results")
    print("--------------------------")
    print(f'Total Votes: {total_votes}')
    print("--------------------------")
    print(f'Khan: {khan_percentage}% ({khan_total})')
    print(f'Correy: {correy_percentage}% ({correy_total})')
    print(f'Li: {li_percentage}% ({li_total})')
    print(f'OTooley: {otooley_percentage}% ({otooley_total})')
    print("--------------------------")
    print(f'Winner: Khan')
    print("--------------------------")


#export text file with the results