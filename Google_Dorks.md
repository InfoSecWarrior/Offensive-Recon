# Google Dorking
**Google Dorking**, also known as **Google Hacking,** is a technique used to ***uncover sensitive information*** on the internet by utilizing advanced search techniques with the Google search engine. This involves using specific search ```operators``` and search queries to identify vulnerable websites and servers that may contain exploitable information.

There are two types of google Operators...


## Basic Operators
**Basic operators** are *simple and easy to use*. Here are some examples of basic operators:

No. | Operator | Description
--- | --- | ---
1 | + | Used to include a specific keyword in the search results
2 | - | Used to exclude a specific keyword from the search results
3 | "" | Used to search for an exact phrase
4 | * | Used to match any word in a search query
5 | . | Used to search for a range of numbers
6 | ~ | Used to search for pages that contain similar words
7 | OR | Used to search for pages that contain either one or both keywords

## Advanced Operators
**Advanced operators** are more *specific* and can be used to target your search more effectively. Here are some examples of advanced operators:

| No. | Operator | Description | Usage |
| --- | --- | --- | --- |
| 1 | intitle: | Search for a keyword in the title | intitle:keyword |
| 2 | allintitle: | Search for multiple keywords in the title | allintitle:keyword1 keyword2 |
| 3 | inurl: | Search for a keyword in the URL | inurl:keyword |
| 4 | allinurl: | Search for multiple keywords in the URL | allinurl:keyword1 keyword2 |
| 5 | intext: | Search for a keyword in the body of a page | intext:keyword |
| 6 | allintext: | Search for multiple keywords in the body of a page | allintext:keyword1 keyword2 |
| 7 | filetype: | Search for a specific file type | filetype:pdf |
| 8 | site: | Search for pages on a specific website | site:website.com |
| 9 | cache: | Search for cached pages | cache:website.com |
| 10 | link: | Search for pages that link to a specific page | link:website.com/page.html |
| 11 | related: | Search for pages related to a specific URL | related:website.com/page.html |
| 12 | info: | Display information about a specific web page | info:website.com/page.html |
| 13 | inachor: | Search for a keyword in the anchor text of links to a page | inachor:keyword |



### Rules for using Advanced Operators:
- There should be no space between the operator and the search term.
- Searches are NOT case sensitive.
- Use quotation marks if a search term has a space or use a period instead.
- Combine multiple operators for more specific and targeted search results.

## Dorks Lists...


| No. | Dork | Description |
| --- | --- | --- |
| 1 | "intitle:index.of" site:. | Search for directory listings on any website |
| 2 | "intitle:Index of /wp-content/uploads" site: | Search for WordPress uploads directory |
| 3 | intitle:"index of /files" site: | Search for files directory |
| 4 | intitle:"index of /Doc" site: | Search for documents directory |
| 5 | allinurl:wp-login.php?action=register | Search for WordPress registration pages |
| 6 | "Apache" intitle:"index.of /dist" | Search for Apache directory listings |
| 7 | inurl: */vendor/ site:. | Search for vendor directory |
| 8 | intitle:"index of /wp-content/plugins" | Search for WordPress plugins directory |
| 9 | intitle:"Index of /dist" | Search for software distribution directories |
| 10 | filetype:txt username password | Search for plain text login credentials |
| 11 | allintitle:"index of /logs" | Search for log files directory |
| 12 | intitle:"index of" /authorize_payment | Search for authorize_payment directory |
| 13 | intitle:"index of" /backup | Search for backup directories |
| 14 | intitle:"index of *password" | Search for password files |
| 15 | intitle:"index of" *username *password filetype:txt | Search for username and password files |
| 16 | intitle:"index.of /database" | Search for database directory |
| 17 | intitle:"index of" database.yml | Search for database configuration files |
| 18 | intitle:"index of */vendor/drupal/console-en/" | Search for Drupal Console directory |
| 19 | intitle:"index of" */admin+password site:.com | Search for admin and password directories on a specific website |
| 20 | intitle:"Index of c:\Windows\" | Search for directory listings in Windows folders |
| 21 | intitle:"index of\" inurl:ftp (pub | incoming) | Search for FTP directory listings |
| 22 | intitle:index.of passwd passwd.bak | Search for password files |
| 23 | intext:"Index of /" +password.txt | Search for password files in directory listings |
| 24 | intitle:"index of" /private | Search for private directories |
| 25 | intitle:index of */private_key | Search for private key files |
| 26 | intitle:"index of" /wp-includes/ | Search for WordPress includes directory |
| 27 | intitle:"index of" */wp-content/plugins/wp-shopping-cart | Search for WordPress shopping cart plugins directory |
| 28 | inurl:/wp-includes/Requests/ -site:*wordpress.org | Search for WordPress Requests directory |
| 29 | intitle:index.of db | Search for database files |
| 30 | intitle:"index of" *wp-config.php.save | Search for WordPress configuration files |
| 31 | intitle:"index of" *config.inc.php | Search for configuration files |
| 32 | intitle:"index of" "ftp" | Search for FTP servers query 
| 33 | intitle:"index of" /wp-content/plugins/ "documentation" | A search query for finding documentation on specific WordPress plugins
| 34 | intitle:"index of" /wp-content/plugins/ "user guide" | A search query can be helpful in finding user guides or manuals related to specific WordPress plugins
| 35 | intitle:"index of" *.php | Finding directory listings of PHP files 
| 36 | intext:"Index of /" +password.txt | Search Publicly Accessible Password Listings
| 37 | intitle:index of intext:settings.inc.php | Searching for web pages that contain directory listings of files that include the "settings.inc.php" file 
| 38 | inurl:/wp-content intitle:"index of" */passwd | Finding Potentially Sensitive Information in WordPress wp-content Directory Listings
