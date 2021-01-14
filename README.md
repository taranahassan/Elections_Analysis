# Elections_Analysis

## Overview of Election Audit

A manager, Seth, from the **Colarado Board of Elections** has tasked his staff, Tom, with the Elections Audit from tabulated results of the **US Congressional Precinct of Colarado.**  Tom has tasked us for assisting him in generating a vote count report with the following requirements:

1. Total number of votes casted overall for the election.
2. Total number of votes casted for each county.
3. Calculating the total percentage of votes for each county.
4. County with the highest voter turnout.
5. Calculating the total votes each candidates received.
6. Calculating the total percentage of votes for each candidate.
7. Identifying the winner of the election based on popular votes.

Typically this task is done by Excel, however Seth is interested in automating this process using Python.  If this audit is successful, then the code will be useful for other Congressional Elections, Senatorial Elections and local elections.  


### Resources used

- *Data source:* election_results.csv (https://github.com/taranahassan/Elections_Analysis/blob/main/Resources/election_results.csv)
- Software used was Python 3.7 to execute the code and Visual Studio Code 1.52.1 was to write the script for Python

## Election Audit Results

The analysis of the Congressional Election results identify:
1. There are a total of **369,711** votes casted in this election.
2. There were a total of 3 counties with their respective total votes:
      - Jefferson with **38,855** votes casted with *10.5%* of total votes.
      - Denver with **306,055** votes casted with *82.8%* of total votes.
      - Arapahoe with **24,801** votes casted with *6.7%* of total votes.
3. **Denver** had the largest turnout of voters.
      
4. There were a total of 3 candidates with their respective total votes:
      - Charles Casper Stockham received total of **85,213** votes with *23.0%* of the total votes.
      - Diana DeGette received total of **272,892** votes with *873.8%* of the total votes.
      - Raymon Anthony Doane received total of **11,606** votes with *3.1%* of total votes.
      
5. **Diana DeGette won the election leading with 73.8% of total votes, totalling her votes to 272,892.**

Below is a screenshot of the election results saved in a text file.

![Election_results](https://github.com/taranahassan/Elections_Analysis/blob/main/Image_examples/Elections_results.png?raw=true)



## Election Audit Summary

The code written using Python was successful in automating the process to tally up the results for each category.  Setting up variable names with a value before dictating the action required is essential. ![Setting_variable_example](https://github.com/taranahassan/Elections_Analysis/blob/main/Image_examples/Setting_variable_example.png?raw=true)

There was the use of for loop method which lets us search through the entire dataset.  ![For_loop_example](https://github.com/taranahassan/Elections_Analysis/blob/main/Image_examples/For_loop_example.png?raw=true)

The if-then statements were used to pick out the selected information we require. ![If_statement_example](https://github.com/taranahassan/Elections_Analysis/blob/main/Image_examples/If_statement_example.png?raw=true)

Once the code is set up to retrieve the specific data, we are able to format the output to be readable.  ![Formatting_output_example](https://github.com/taranahassan/Elections_Analysis/blob/main/Image_examples/Formatting_output_example.png?raw=true)

The code can be reused for other Congressional elections as well, nothing in the code would need to be changed except maybe the file path and the data source file that needs to be opened and read.
We could use this code for a Senatorial Election.  Dataset would be much larger therefore much more beneficial and efficient when doing an election audit.  The same code would need to be expanded.  Since the current code only extracts information for counties and candidates for the precinct of Colarado, we would need to expand that to provide multiple precincts within a city and then multiple cities within a state.  The following edits can be made:
      1. Include more variables to initialize total votes for each city and state in addition to the county already set.
      2. Each city will have their own candidates running for the House of Representatives and each state will have candidates running for the Senate position.  

In the *1st for loop with if-then statements* we have, is extracting list of counties, each counties totaling votes and percentages, the list of candidates and their respective votes and percentages. Therefore:
      3. We would need to initialize a *2nd for loop with if-then statements* to extract the same for cities; each cities' totaling votes and percentages, candidates within the          city and their respective votes and percentages.  
      4. A *3rd for loop with if-then statements* will extract the same for each state.  
      5. The code thereafter to print and save to the text file for all the data extracted can be copied for cities and states; the only edit would be to change the variables            that reference to the list and dictionaries created for each category.
