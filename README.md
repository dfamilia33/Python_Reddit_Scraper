# Python_Reddit_Scraper

## Purpose
Script to find keywords of interest specified and send an email through a google email client notifying user of post of interest.
As it would be tedious for a human to scour a webpage constantly for specific posts, the goal was to have a background process looking for specific keywords to be notified of on the site Reddit

## Technologies

### Languages
* Python

### API
* Reddit API
* Python Reddit API Wrapper

### Tools
* CRON Task Scheduler



# How it works
Script runs as a background process that intermittently checks reddit posts for a keyword. If it is detected, and not already sent via email, the email client notifies the user.
