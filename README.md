# open-sesame


  ![alt text](https://github.com/humblelad/open-sesame/blob/master/images/osesame.png) 


## A python tool which runs to display random publicly disclosed Hackerone reports when bored. Automatically opens the report in browser. 

> Contains Over 8k Publicly disclosed Hackerone reports and addtl. wordlist of ~700 bug bounty writeups.

*This is a productivity tool for security enthusiasts and bug bounty hunters. I have written a blog here giving my idea of how to use this efficiently.*

link
![alt text](https://github.com/humblelad/open-sesame/blob/master/images/front.jpg) 

Additional features include:
  * Opening URL from custom wordlist which has bug bounty writeups.
  * Fetching and Updating the newly disclosed Hackerone publicly disclosed reports.

## Usage:
Pl install components in rquirements.txt




`python3 default.py` Opens a random magic URL from the collection of publicly disclosed h1 reports.

![alt text](https://github.com/humblelad/open-sesame/blob/master/images/default.jpg) 

`python3 default.py --custom` Opens a random magic URL from the collection of custom wordlist having bug bounty writeups.

![alt text](https://github.com/humblelad/open-sesame/blob/master/images/custom.jpg) 


`python3 default.py --refresh` Refreshes and adds newly publicly disclosed h1 reports to your file(final.txt)

![alt text](https://github.com/humblelad/open-sesame/blob/master/images/refresh.jpg) 


### Known Issues
  * The ability of not able to distinguish between completely publicly disclosed reports and reports with limited disclosures.
  * The tool may break in the way of how it works if it gets run after a long time. The default range specified is scraping 10 pages to reduce load on the site. If you believe you are running it after a long time, consider increasing the range upto 50 in *main for loop in refresh.py* before running. This will enable collecting all the reports till the recent report extracted in the final.txt .
  
 ### Thanks
  * h1.nobbd(dot)de
  * bugreader(dot)com
  * Awesome-Bugbounty-Writeups Repo
  * and other helpful sources.. :) 
  
