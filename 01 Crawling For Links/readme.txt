The Folder Contains the Following Programs 

# make_db.py - Basically makes the whole database of valid links using two tables - "stack" and "visited". The final valid links are in the "visited" table. The "stack" table has all links, both intranet as well as internet links (some invalid ones too), and the program goes through the stack updating it each time with new links, and adding valid intranet links to the "visited" table.

# empty_db.py - Empties the tables in the database for a clean make of the database.

# links.db - The actual database file worked with. After code completion and crawling through all the links, the database now has the stack table empty and the visited table now contains all the valid addresses in the intranet.

# re_crawl.py - Contains a code snippet used in previous attempt to crawl the intranet. It did not work because the program exceeds the recursion limit of python. As it is dangerous to change the recursion limit of Python, a "stack" table was used in the database to save the links to be crawled.

