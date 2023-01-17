#imports
import csv 
import os

#file path
Poll_CSV = os.path.join("Resources", "election_data.csv")

votecount = 0
cand1 = 0
cand2 = 0
cand3 = 0
candidatelist = []

    
with open(Poll_CSV) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
    
    for row in csv_reader:

        #count total votes
        votecount+=1
        
        #find candidate names
        try:
            candidatelist.index(row[2]) >= 0
            pass

        except ValueError:
            candidatelist.append(row[2])
            
        #count votes of candidates
        if candidatelist.index(candidatelist[0]) == candidatelist.index(row[2]):
            cand1 += 1
        elif candidatelist.index(candidatelist[1]) == candidatelist.index(row[2]):
            cand2 += 1
        elif candidatelist.index(candidatelist[2]) == candidatelist.index(row[2]):
            cand3 += 1
        else:
            pass

        
print("Election Results")
print("-----------------------")
print("Total Votes:", votecount)
print("-----------------------")
print(candidatelist[0], (cand1/votecount)*100, "%", "(", cand1, ")")
print(candidatelist[1], (cand2/votecount)*100, "%", "(", cand2, ")")
print(candidatelist[2], (cand3/votecount)*100, "%", "(", cand3, ")")
print("-----------------------")

if cand1 > cand2 and cand1 > cand3:
    print("The Winner is ", candidatelist[0])
elif cand2 > cand1 and cand2 > cand3:
    print("The Winner is ", candidatelist[1])
elif cand3 > cand1 and cand3 > cand2:
    print("The Winnier is ", candidatelist[2])
else:
    pass

with open("Analysis/PyPoll_Analysis.txt", 'w') as f:
    f.write("Election Results: Total Votes: 369711; Charles Casper Stockham 23.04% ( 85213 ); Diana DeGette 73.81% ( 272892 ); Raymon Anthony Doane 3.13% ( 11606 ); The Winner is  Diana DeGette")

