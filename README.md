# election-analysis-python-basics

## Overview of Election Audit
* Client is Colorado State and is asking for an automated election audit using Python
* Deliverables outputs include:
    * Overall voter count metric: number of total voters
    * Metrics on winning candidate: raw votes and percentage
    * Metrics on voting count per county: raw votes and percentage
    * Outputs requested in .py format (for terminal applicability) and .txt (for plain text)
* Relevant Files
    * Client input files is found here: [Colorado_Election_Results](https://github.com/nabilram/election-analysis-python-basics/blob/main/resources/election_results.csv)
    * Output .py file is found here: [Election_Audit_Python_Script](https://github.com/nabilram/election-analysis-python-basics/blob/main/resources/python_practice.py)
    * Output .txt file report is here: [Election_Audit_TXT_Report](https://github.com/nabilram/election-analysis-python-basics/blob/main/resources/analysis/election_analysis.txt) 
    * Output terminal screenshot, see below:

![Terminal_SS_Election_Audit](https://github.com/nabilram/election-analysis-python-basics/blob/main/resources/terminal_output.PNG)

## Results of Election Audit

### Overall Vote Count
* A total of 369,711 voters were casted from the 3 counties

### County Audit Sumary
* Jefferson had 10.5% of all votes (38,855)rea
* Denver had 82.8% of all votes (306,055)
* Arapahoe had 6.7% of all votes (24,801)
* COUNTY RESULT: Denver had the the biggest voter turnout at 82.8% with 306055 voters

### Candidate Audit Summary
* Charles Casper Stockham had 23.0% of all votes (85,213)
* Diana DeGette had 73.8% of all votes (272,892)
* Raymon Anthony Doane had 3.1% of all votes (11,606)
* CANDIDATE RESULT: Diana DeGette won with 73.8% of the votes, 272892 people voted for them

## Summary and Futher Application
* Scaling up the code to accomodate wider scope (more counties, or even more states) is possible
    * Application to more counties in next electoral cycle is advised for quality electoral checks and balances
* Additional features and data points may assist the client in their efforts to increase voter turn out outside of Denver
    * Data points on voter's gender, ethnicity, age, and others will yield better voter-based analytics

## Challenges and Lessons Learned
* Python is a lot more intuitive in its auto-classification of obects (unlike VBA or C, for example)
    * Assigning variable types and array lists names is not always necessary
* Caution on elongating code with un necessary defnitions and declarations must be taken
* Data analyst must familiarize themself with Python abilities so maximize its use