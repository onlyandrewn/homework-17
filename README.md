# this-american-life-scraper
 ### Scrapes [This American Life](https://www.thisamericanlife.org/)

It looks for new episodes posted to the homepage.

 ### Output
 ---
`episodes.csv`

A dataset of current and recently aired episodes of This American Life featured on their homepage. Fields include:

- num: Episode number
- date: Episode date
- name: Name of episode
- url: Link to episode
- desc: Episode description
- type: Current or recently aired

### Process
---
Used Beautiful Soup to scrape the featured episode and the list of recently aired episodes. 

Fetches data from the current episode, then loops over all recently aired episodes and concatenates them into `episodes.csv`