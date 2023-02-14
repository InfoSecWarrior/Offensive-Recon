## Sitemap.
A **Sitemap** is a file that lists all of the pages of a website, along with information about each page, such as when it was last updated and how important it is relative to other pages. Sitemaps are used to help search engines understand the structure of a website, which can make it easier for the website to be found and indexed by the search engines. *Sitemaps can be submitted to search engines as an ```XML``` file, and many websites also include an ```HTML``` sitemap to help users navigate the website.*
		
-   **How its Work**
			
	**1. Spidering:-** Search engine spiders, also known as crawlers or robots, use the information in the sitemap to crawl and index the pages of a website. The spiders follow the links in the sitemap to discover new pages and retrieve the content of each page. The spiders can use the information in the sitemap to determine the priority and frequency of updates for each page.

    **2. Crawling:-** The process of crawling is the act of visiting each page of a website and retrieving the content of the page. The spiders use the information in the sitemap to determine which pages to crawl and how often to crawl them. The crawl frequency is based on the priority of the page and the frequency of updates. The spiders use the content of each page to index the site and update their search results.

    ```Check the website's footer or header for a link to the sitemap.```
	
    Try appending ```/sitemap.xml```or ```/sitemap.html``` to the end of the website's URL. 

    ***Some Of The Websites To generate the sitemap.***
			
	-   [My sitemap generator.](https://www.mysitemapgenerator.com/)

	-   [XML Sitemaps Generator.](https://www.xml-sitemaps.com/)
		
	***Command line tools to Generate sitemap.***
		
    -   **Install the Sitemap generator command-line tool.**
        
        ```
        pip3 install dirhunt
        ```
    -   Examples of dirhunt.
        ```
        dirhunt target_URL
        ```
        ```
        dirhunt target_URL --to-file filename.json
        ```

-   **Find robots.txt.**

    The robots.txt is a file that lists the pages of a website that search engines should not crawl. To find the robots.txt file, append ```/robots.txt``` to the end of the website's URL
