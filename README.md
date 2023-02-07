# python_newsapi
Purpose: To publish the top headlines of news related to a topic or country so that we spend not more than 5 minutes to read news every day.

Steps involved in gathering the news and publishing it:

Main source of news : Gathered by an API call to https://newsapi.org/docs/endpoints/top-headlines. The pre-requisite to collect the news from this site is an API Key.
A python script has been created to make this API call , collect the data in JSON format, convert it into a csv file using Pandas library. The url link is converted into hyperlink by making use of regular expressions
The collected news is uploaded into google drive folder.
The script is run as a cron job so that the script runs daily at a specified hour. You may have to set up a wake schedule for your sysytem which requires you to log in as root and set up the schedule.
Typical output:

<img width="1819" alt="image" src="https://user-images.githubusercontent.com/61753816/217335372-147ba5df-05bc-45e5-9596-1e4124c2791f.png">
