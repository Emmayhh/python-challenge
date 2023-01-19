import os
import csv

TotalVotesCast = 0
candidates_list = []
candidates_dic = {}
winners = ""



#Create path to csv file
election_csv = os.path.join("Resources/election_data.csv")

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
    # The total number of votes cast
        TotalVotesCast += 1

        candidates = (row[2])

        # if not in the current candidates, add
        if candidates not in candidates_list:
            #add name of candidates
            candidates_list.append(candidates)
            #start to count
            candidates_dic[candidates] = 0

        candidates_dic[candidates] += 1
        
    #A complete list of candidates who received votes
    
print("------------------------------------------------")
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total votes: {TotalVotesCast}")


for candidates in candidates_dic:
    #extract each candidates votestotal
    VotesCast = candidates_dic.get(candidates)

    #percentage of each candidate
    PercentageVotes = VotesCast / TotalVotesCast * 100
    
    #splite name and votestotal from dic
    for keys, values in candidates_dic.items():
        print(f"{keys}: {PercentageVotes:3f}% ({values})")

    # find who won the election
    winners = max(candidates_dic)

    print("------------------------------------------------")
    print(f"Winner:{winners}")
    print("------------------------------------------------")   

text_file = ("/Users/hany/Desktop/Bootcamp/03-Python/Ass3/python-challenge/PyPoll/analysis/PyPoll_text_file.txt")

with open(text_file, "w") as textfile:
    textfile.write("------------------------------------------------\n")
    textfile.write("Financial Analysis" + "\n")
    textfile.write("------------------------------------------------\n")  
    textfile.write(f"Total votes: {TotalVotesCast}\n")


    for keys, values in candidates_dic.items():
        textfile.write(f"{keys}: {PercentageVotes:3f}% ({values})\n")


    textfile.write("------------------------------------------------\n")
    textfile.write(f"Winner:{winners}\n")
    textfile.write("------------------------------------------------\n")  
