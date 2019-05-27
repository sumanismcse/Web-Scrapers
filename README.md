# Web-Scrapers
Web Scraping for Machine Learning datasets and required unstructered data

# Scrape0.py
The first step is to import the requests library and download the webpage.Save the file and run this script from your command line and you should see the entire HTML of the page spilled out.

# Scrape.py
Next import the BeautifulSoup HTML parsing library and feed it the page.Save the file and run the script again and you should see the page’s HTML again, but in a prettier format this time.

# Scrape2table.py
Save the file and run scrape.py again. This time it only prints out the table we’re after, which was selected by instructing BeautifulSoup to return only those <table> tags with resultsTable as their class attribute.
  
# Scraperow3table.py
Save and run the script. You’ll not see each row printed out separately as the script loops through the table.

# Scraper4tablerowcell.py
we can loop through each of the cells in each row by select them inside the loop.

# Scraper5tablerowcellremovenonbreakingspace.py
When that prints you will notice some annoying &nbsp; on the end of many lines. That is the HTML code for a non-breaking space, which forces the browser to render an empty space on the page. It is junk and we can delete it easily with this Python trick.

# Python list streaming one row at a time.py
The name pretty much defines it.

# Scrape7pythonliststreamoflist of lists.py
To write that list out to a comma-delimited file, we need to import Python’s built-in csv module at the top of the file. Then, at the botton, we will create a new file, hand it off to the csv module, and then lead on a handy tool it has called writerows to dump out our list of lists.

# Scrape8 to list out to a delimited file without headers
Since there are no longer any print statements in the file, the script is no longer dumping data out to your terminal. However, if you open up your code directory you should now see a new file named inmates.csv waiting for you. Open it in a text editor or Excel and you should see structured data all scraped out.

There is still one obvious problem though. There are no headers!

# Scraper9 perfect.py
 Let’s just skip the first row when we loop though, and then write the headers out ourselves at the end.
 
 
 # Best Scraper with multiple pages and semistructured data.py & Web Scraper.ipynb
This is a scrape of a semistructured data with wrappers taken back and forth from the webpage throughout continuos 7 pages.It was pretty annoying in some ways to go and forth for the divs and classes but they are pretty much the same in a large database of a website so scraping like this saves a lot hard work i.e. to label the data acquired.
