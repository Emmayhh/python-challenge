import os
import csv

TotalVotesCast = 0
candidates_list = []
candidates_dic = {}
PercentageVotes = [0,0,0]
candidatesW = []

winners = ""
winnerNum = 0


#Create path to csv file
election_csv = os.path.join("/Users/hany/Desktop/Bootcamp/03-Python/Ass3/python-challenge/PyPoll/Resources/election_data.csv")

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
    # The total number of votes cast
        TotalVotesCast += 1

        candidates = (row[2])
#option = list, votes = dic
    # if not in in the current candidates
        if candidates not in candidates_list:
            #add it to list
            candidates_list.append(candidates)
            #start to count
            candidates_dic[candidates] = 0
        
        candidates_dic[candidates] += 1

    #A complete list of candidates who received votes

print("------------------------------------------------")
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total votes: {TotalVotesCast}")

#dic opinion =list 
#dic votes = dic

for candidatesW in candidates_dic:

    VotesCast = candidates_dic.get(candidatesW)

        #The total number of votes each candidate won
    PercentageVotes = VotesCast / TotalVotesCast * 100
    
    #The winner of the election based on popular vote
    
    if (winnerNum < VotesCast):
        winnersName = candidatesW
    
    # calculate the percentage of votes per candicate (3 decimal points)

#print(candidatesW)

#printing the results

for item in candidates_dic:
    print(f"{item}: {PercentageVotes:.3f}% ({candidates_dic[item]})")

print("------------------------------------------------")
print(f"Winner:{winnersName}")
print("------------------------------------------------")   

text_file = ("/Users/hany/Desktop/Bootcamp/03-Python/Ass3/python-challenge/PyPoll/analysis/PyPoll_text_file.txt")

with open(text_file, "w") as textfile:
    textfile.write("------------------------------------------------\n")
    textfile.write("Financial Analysis" + "\n")
    textfile.write("------------------------------------------------\n")  
    textfile.write(f"Total votes: {TotalVotesCast}\n")

    for item in candidates_dic:
        textfile.write(f"{item}: {PercentageVotes:.3f}% ({candidates_dic[item]})\n")

    textfile.write("------------------------------------------------\n")
    textfile.write(f"Winner:{winnersName}\n")
    textfile.write("------------------------------------------------\n")  