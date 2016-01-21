import scraperwiki #this is a useful tool to help import web pages
import lxml.html #this is a good tool for digging into a web page. In weird coding language both of these things are called 'libraries'.
#
# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/") #Here you are telling the computer to use scraperwiki 
#to scrape a page. The fact that the page is between functions shows it is a function. 
#print html #you then have to tell the computer to print the results of that command
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html) #with root you are creating an object which you can then use to operate. You just just leave this line.
tds = root.cssselect('td') #this what you are looking for. 'td' in this case is the correct html tag surrounding the information you want 
#to grab. This will change though - you need to check the html code of the original source. 
for td in tds:
 record = {"cell" : td.text}
 print record
 scraperwiki.sqlite.save(["cell"], record)
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
