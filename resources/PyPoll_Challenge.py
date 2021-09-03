#PyPoll Challenge - Nabil Ramirez

# Load modules and packages.
import csv
import os

# Initialize INPUTS: votes integer, candidate + county lists, votes per candidate library.
all_votes = 0
cddt_list = [] 
cnty_list = []
per_cddt_votes = {}
per_cnty_votes = {}

# Initialize OUPUTS: string + integer + float vars for TXT output reporting
elect_results = ""
winning_candidate = ""
winning_count = 0
winning_percentage = 0 
largest_county = ""
county_v_turnout = 0

#Read CSV file using file path + with open + variable; read header; assign to data fram
with open("resources/election_results.csv") as elect_r:
    file1 = csv.reader(elect_r, delimiter = ",")
    header = next(file1)
    election_df = [row for row in file1]

    #Loop through to pull data
    for each_vote in election_df:

        # Summation of total votes
        all_votes = all_votes + 1

        # Pull candidate, append to list if needed, track votes per candidate
        cddt_name = each_vote[2]

        if cddt_name not in cddt_list:
            cddt_list.append(cddt_name)
            per_cddt_votes[cddt_name] = 0
        else:
            per_cddt_votes[cddt_name] = per_cddt_votes[cddt_name] + 1

        # Pull county, append to list if needed, track votes per county
        cnty_name = each_vote[1]

        if cnty_name not in cnty_list:
            cnty_list.append(cnty_name)
            per_cnty_votes[cnty_name] = 0
        else:
            per_cnty_votes[cnty_name] = per_cnty_votes[cnty_name] + 1

print(f"{per_cddt_votes}")
print(f"{per_cnty_votes}")

# Create output TXT file using f and open + file path
with open("resources/analysis/election_analysis.txt","w") as output_txt:

# Print the final vote count + per candidate + per county metrics
    elect_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"TOTAL VOTES: {all_votes}\n"
        f"-------------------------\n\n"
        f"COUNTY VOTERS -- \n"
        f"-------------------------\n"
        f"{per_cnty_votes} \n"
        f"-------------------------\n\n"
        f"CANDIDATE VOTES -- \n"
        f"-------------------------\n"
        f"{per_cddt_votes} \n"
        f"-------------------------\n\n")
    print(elect_results, end = "")
    output_txt.write(elect_results)

# Calculate and print additional election metrics

#     # 6a: Write a for loop to get the county from the county dictionary.

#         # 6b: Retrieve the county vote count.

#         # 6c: Calculate the percentage of votes for the county.


#          # 6d: Print the county results to the terminal.

#          # 6e: Save the county votes to a text file.

#          # 6f: Write an if statement to determine the winning county and get its vote count.


#     # 7: Print the county with the largest turnout to the terminal.


#     # 8: Save the county with the largest turnout to a text file.


#     # Save the final candidate vote count to the text file.
#     for candidate_name in candidate_votes:

#         # Retrieve vote count and percentage
#         votes = candidate_votes.get(candidate_name)
#         vote_percentage = float(votes) / float(total_votes) * 100
#         candidate_results = (
#             f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#         # Print each candidate's voter count and percentage to the
#         # terminal.
#         print(candidate_results)
#         #  Save the candidate results to our text file.
#         txt_file.write(candidate_results)

#         # Determine winning vote count, winning percentage, and candidate.
#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             winning_count = votes
#             winning_candidate = candidate_name
#             winning_percentage = vote_percentage

#     # Print the winning candidate (to terminal)
#     winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")
#     print(winning_candidate_summary)

#     # Save the winning candidate's name to the text file
#     txt_file.write(winning_candidate_summary)
