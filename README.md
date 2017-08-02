# Pie
An Intranet Search Engine (Ongoing Project)

# Crawling The Intranet

![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/1.png)

Crawling of intranet was done with the help of 'requests' library for Python 3. Beautiful Soup was used for the parsing of HTML for searching new links on visited pages.

![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/2.png)

A database was implemented with Sqlite3 in the form of a stack. A database was required because the number of intranet links easily crossed 50,000 due to which it wasn't safe to implement it in a simple array or stack on RAM. 

When the database creation was complete, it needed some filtering as there were some duplicate links due to white spaces and other issues.
The code for filtering the links are present in the 'Cleaning' folder.

The links were then sorted and separated based on the domain names which were as shown in the image given below.
![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/3.png)

# Url Indexing

The indexing 
![alt text](https://github.com/OrionMonk/Pie/blob/master/image_files/4.png)
