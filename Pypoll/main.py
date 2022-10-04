#Import os module
import os
# Import csv module
import csv
# Import collections module
from collections import Counter
# Create a file path to the data
file_path = os.path.join('..','Resources','election_data.csv')
#initialize variables
total_votes = 0
candidate_list_seen =[]
candidate_list_uniq =[]
winner = ()
candidatesvotegain ={}
totalvotes = 0
#open csv and read it
with open(file_path) as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #total votes number
        total_votes += 1
        #candidate list 
        candidate_list_seen = row[2]
        if candidate_list_seen not in candidate_list_uniq:
            candidate_list_uniq.append(candidate_list_seen)
        #find out the winner
        totalvotes +=1
        if row[2] not in candidatesvotegain:
            candidatesvotegain[row[2]] = 1
        else:
            candidatesvotegain[row[2]] += 1
        winner = max(candidatesvotegain, key = candidatesvotegain.get)
#count for totel number of votes each candidates won
with open(file_path) as content_file:
    countent = content_file.read()
    votes_Charles = (countent.count('Charles Casper Stockham'))
    votes_Diana = (countent.count('Diana DeGette'))
    votes_Raymon = (countent.count('Raymon Anthony Doane'))      
#calculate the percentage of each candidates won
per_Charles = (int(votes_Charles)/int(total_votes)*100)
per_Diana =  (int(votes_Diana)/int(total_votes)*100)   
per_Raymon =  (int(votes_Raymon)/int(total_votes)*100)  
#print analysis result
print('Election Results')
print('------------------------')
print('Total Votes: ' + str(total_votes))
print('------------------------')
print('Charles Casper Stockham:' + str(round(per_Charles)) + '%' + '(' + str(votes_Charles) + ')')
print('Diana DeGette:' + str(round(per_Diana)) + '%' + '(' + str(votes_Diana) + ')')
print('Raymon Anthony Doane:' + str(round(per_Raymon)) + '%' + '(' + str(votes_Raymon) + ')')
print('------------------------')
print('Winner: ' + str(winner))
#write this to an output file
f = open("election_results.txt", "w")
f.write('Election Results')
f.write('------------------------')
f.write('Total Votes: ' + str(total_votes))
f.write('------------------------')
f.write('Charles Casper Stockham:' + str(round(per_Charles)) + '%' + '(' + str(votes_Charles) + ')')
f.write('Diana DeGette:' + str(round(per_Diana)) + '%' + '(' + str(votes_Diana) + ')')
f.write('Raymon Anthony Doane:' + str(round(per_Raymon)) + '%' + '(' + str(votes_Raymon) + ')')
f.write('------------------------')
f.write('Winner: ' + str(winner))