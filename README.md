# D7 Friendship Pact
An algorithm-based matchmaker inspired by the Marriage Pact. Created for <a href="https://www.finddistrict7.org">FIND, Inc.'s District 7</a> by Jaco Asistores (2023-2025 Webmaster) with survey questions created in collaboration with Sofia Romulo (2024-2025 Treasurer). Find the survey here _(link not available)_.

Uses the <a href="https://daffidwilde.github.io/matching/">matching library</a> to solve the <a href="https://en.wikipedia.org/wiki/Stable_roommates_problem">stable-roommate problem</a> and create pairs of compatible friends.

## Testing and Usage:

```
python src/Main.py test-files/d7fp_test_responses.csv
```
where `test-files/d7fp_test_responses.csv` would be the path of your actual CSV file. Yay! You did it!

_Note: the test .csv file uses fake names and emails._

This program was paired with this <a href="https://script.google.com/d/1CPkEmwWxN7RbDC-Ff98mPNnoHGyC-wo8JB3xXhbvZ5W1uTiVIJRXyA5S/edit?usp=sharing">Google Apps Script</a> that sent automated emails to each participant with all the relevant details of their pairing, using the output .csv files as Google Sheets.

## Potential Improvements

- ***Question weights***. If different questions were weighted differently (e.g. _Do you mind when your peers consume alcohol?_ could theoretically have a higher weight than _Do you like to watch movies?_), then questions that are deemed more important can have greater effect on the final compatibility calculation, and the survey can be further refined.
- ***Improve `CSVReader.py`***. When submitting social media accounts in the short answer portion of the survey, many participants included multiple forms of social media separated by commas, which in turn interfered with the CSV reader as it stripped responses. Currently, the sample size is small enough where these errors can be handled manually before rerunning. To fix this, `CSVReader.py` should skip commas within double quotation marks when stripping responses.
- ***Redundancies for missing data***. Some participants skimmed over some questions and did not answer, leaving a blank value in the CSV file. Currently, these invalid rows are just returned and handled manually before rerunning; however, if sample sizes increase, this can become troublesome quickly. Two concurrent solutions should be implemented:
  - First, make all the questions in the survey required, so no question goes unanswered (a simple oversight when the survey was initially released).
  - Second, check programmatically if there are any blank values, and handle them accordingly (fill in with median value as a placeholder?). 
