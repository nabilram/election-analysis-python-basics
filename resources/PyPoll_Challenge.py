#PyPoll Challenge - Nabil Ramirez

# Load modules and packages.
import csv

# Initialize INPUTS: votes integer, candidate + county lists, votes per candidate/country libraries.
all_votes = 0
cddt_list = [] 
cnty_list = []
per_cddt_votes = {}
per_cnty_votes = {}

# Initialize OUPUTS: string + integer + float vars for TXT output reporting
elect_results = ""
win_cddt = ""
win_cnty = ""
win_cddt_raw = 0
win_cddt_px = 0
win_cnty_px = 0 

#Read CSV file using file path + with open + variable; read header; assign to data frame
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
            per_cddt_votes[cddt_name] = 1
        else:
            per_cddt_votes[cddt_name] = per_cddt_votes[cddt_name] + 1

        # Pull county, append to list if needed, track votes per county
        cnty_name = each_vote[1]

        if cnty_name not in cnty_list:
            cnty_list.append(cnty_name)
            per_cnty_votes[cnty_name] = 1
        else:
            per_cnty_votes[cnty_name] = per_cnty_votes[cnty_name] + 1

# Create output TXT file using f and open + file path and print and TXT election metrics
with open("resources/analysis/election_analysis.txt","w") as output_txt:
    elect_results = (f"\nOVERALL TOTAL VOTES: {all_votes}\n\n")
    print(elect_results, end = "")
    output_txt.write(elect_results)

    # COUNTY RESULTS: names, raw vote count, calculate turnout %, print to terminal, append TXT
    # Set header string
    header2 = (f"COUNTY RESULTS SUMMARY\n-----------------------------------\n")
    print(header2)
    output_txt.write(header2)
    
    # Do calcs and outputs
    for each_cnty in per_cnty_votes:
        votes = per_cnty_votes[each_cnty]
        now_ratio = float(votes) / float(all_votes) * 100
        county_res = (f"{each_cnty} had {now_ratio:.1f}% of all votes ({votes:,}).\n")
        print(county_res)
        output_txt.write(county_res)

        # Decision tree on winning county % and raw vote count, declare winner.
        if win_cnty_px < now_ratio:
            win_cnty_px = now_ratio
            win_cnty = each_cnty
            win_cnty_votes = votes 

    #Print county results to Terminal + append TXT
    win_cnty_txt = (F"COUNTY RESULT: {win_cnty} had the the biggest voter turnout at {win_cnty_px:.1f}% with {win_cnty_votes} voters.\n")
    print(win_cnty_txt)
    output_txt.write(win_cnty_txt)

    # CANDIDATE RESULTS: raw vote count, calculate turnout %, print to terminal, append TXT
    # Set header string
    header3 = (f"\nCANDIDATE RESULTS SUMMARY\n-----------------------------------\n")
    print(header3)
    output_txt.write(header3)
    
    # Do calc and outputs
    for each_cddt in per_cddt_votes:
        votes = per_cddt_votes[each_cddt]
        now_ratio = float(votes) / float(all_votes) * 100
        cddt_res = (f"{each_cddt} had {now_ratio:.1f}% of all votes ({votes:,}).\n")
        print(cddt_res)
        output_txt.write(cddt_res)

        # Decision tree on winning candidate % and raw count, declare winner.
        if (win_cddt_px < now_ratio and win_cddt_raw < votes):
            win_cddt_px = now_ratio
            win_cddt = each_cddt
            win_cddt_raw = votes 

    #Print candidate results to Terminal + append TXT
    win_cddt_txt = (F"CANDIDATE RESULT: {win_cddt} won with {win_cddt_px:.1f}% of the votes, {win_cddt_raw} people voted for them.\n\n")
    print(win_cddt_txt)
    output_txt.write(win_cddt_txt)
