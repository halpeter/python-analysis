# Python-Analysis

## Background
This analysis uses python script to analyze CSV data. The scripts read in CSVs, utilize with open, for loops, conditional statements, lists, append functionalitly, and basic statistical calculations (such as minimum, maximum, average, and percent change).

## PyBank

* In this part of the project, my task wass to create a Python script for analyzing the financial records of a company. I was given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* My task was to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* This is the result after running the script:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* This python script is saved here (PyBank/main.py) and the termial output is saved here as well (PyBank/output.txt).

## PyPoll

* In this part of the porject, I was tasked with helping a small, rural town modernize its vote counting process.

* I was given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. My task was to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* This is the result after running the script:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* This python script is saved here (PyPoll/main.py) and the termial output is saved here as well (PyPoll/output.txt).
