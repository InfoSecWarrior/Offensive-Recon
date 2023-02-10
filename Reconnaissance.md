# Reconnaissance.

**Reconnaissance** is gathering information about a target system or network, to identify vulnerabilities that could be exploited. This process is also known as **Footprinting** or **Information Gathering.**

*There are two main types of reconnaissance:*

**Passive:-** Passive reconnaissance involves gathering information without directly interacting with the target system. This can be done through publicly available sources, such as websites and search engines.

**Active:-** Active reconnaissance involves directly interacting with the target system. This can include techniques such as network scans and vulnerability scans and can raise the risk of detection.

## Ethical Hacker / Pentester looking for?

1.  **Network Information.**

    Domain name

    Internal Domain
    
    IP Address
    
    Unmonitored/private websites
    
    TCP/UDP Services
    
    VPN/IDS/IPS/access controls
    
    VPN info
    
    Phone numbers/VoIP
    
    Network topology
    
    Network devices

2.  **Operating System Information.**

    Users and group names/info

    Banner grabbing
    
    Routing tables
    
    SNMP
    
    System architecture
    
    Remote systems
    
    System names
    
    Passwords
    
    Dumpster diving
    
    Version
    
    Patch level

3.  **Organization Information.**

    Organization website
    
    Company directory

    Employee information
    
    Business structure
    
    Location details
    
    Comments in HTML source code
    
    Security policies deployed
    
    webserver links
    
    Background of organization
    
    Marketing and advertising
    
    Prevailing events
    
    Partners
    
    Phone
    
    Financial information

## External Network Pentester looking for?

An **external network** refers to a network that is outside of an organization's internal network and is accessible from the internet. Examples of external networks include public Wi-Fi networks, cloud-based services, and other third-party networks. *External network reconnaissance is a stage in external network penetration testing where the testers gather information about the target system.* The purpose of this phase is to gather information about the target network, including:

1.  **Network Information**

2.  **Operating systems and applications**

3.  **Publicly accessible information**

4.  **Phone**

5.  **Website Mirroring**

6.  **Archive Sites**

7.  **Github recon**

8.  **Whois**

9.  **Web server Content**

10. **Email Header**

11. **Google and Search Engine**

12. **People Sites**

13. **Social Network**

14. **Job Sites**

15. **Alert Website**

## Internal Network Pentester looking for?

Internal network penetration testing is a type of security testing that focuses on evaluating the security of an organization's internal network infrastructure.

1.  **IP Address**

2.  **Internal DNS**

3.  **Private Website**

4.  **Dumpster Diving**

5.  **Shoulder Surfing**


# Overall Reconnaissance.

1.  **Recon with Website.**

    -   **Visit Website.**

        -   Employee Details.
        -   Location Details.
        -   Addresses
        -   Phone number.

    -   **Find Website Sitemap.**

        A **Sitemap** is a file that lists all of the pages of a website, along with information about each page, such as when it was last updated and how important it is relative to other pages. Sitemaps are used to help search engines understand the structure of a website, which can make it easier for the website to be found and indexed by the search engines. *Sitemaps can be submitted to search engines as an ```XML``` file, and many websites also include an ```HTML``` sitemap to help users navigate the website.*
		
		**How its Work**
			
		1. **Spidering:-** Search engine spiders, also known as crawlers or robots, use the information in the sitemap to crawl and index the pages of a website. The spiders follow the links in the sitemap to discover new pages and retrieve the content of each page. The spiders can use the information in the sitemap to determine the priority and frequency of updates for each page.

    	2. **Crawling:-** The process of crawling is the act of visiting each page of a website and retrieving the content of the page. The spiders use the information in the sitemap to determine which pages to crawl and how often to crawl them. The crawl frequency is based on the priority of the page and the frequency of updates. The spiders use the content of each page to index the site and update their search results.

        ```Check the website's footer or header for a link to the sitemap.```
		
		Try appending ```/sitemap.xml```or ```/sitemap.html``` to the end of the website's URL. 

		***Some Of The Websites To generate the sitemap.***
			
		-   https://www.mysitemapgenerator.com/

		-   https://www.xml-sitemaps.com/
		
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

    -   **Get Source code.**

        *Some command line tools to get website source code.*
        ```bash
        wget -m target_URl
        ```
		```
        httrack website_Url
        ```
    -   **Find Websites Archive.**

        ***Some Of The Websites To Find Websites Archive.***
        
        [1. The Wayback Machine.](https://web.archive.org/)
        
        [2. Archive Today.](https://archive.ph/)
       
        [3. Archive IT.](https://archive-it.org/)

    -   **Archive End Points.**

        Install the waybackurls tool.
        ```bash
        go install github.com/tomnomnom/waybackurls@latest
        ```
        ```
        cp -v go/bin/waybackurls /usr/local/bin/
        ```
        Run waybackurls
        ```bash
        waybackurls targert_Urls
        ```
    -   **Find the website technology stack.**

        -   Check the Website Source code
        -   Find the ```Readme.html``` file, append ```/readme.html``` to the end of the website's URL 
        
        -   Find the ```license.txt``` file, append ```/license.txt``` to the end of the website's URL
        
        -   Find the ```Feed``` file, append ```/feed``` to the end of the website's URL
        
        -   [BuiltWith.](https://builtwith.com/)

            [Chrome Extensions](https://chrome.google.com/webstore/detail/builtwith-technology-prof/dapjbgnjinbpoindlpdmhochffioedbn?hl=en)

        -   [wappalyzer.](https://www.wappalyzer.com/)

            [Chrome Extensions](https://chrome.google.com/webstore/detail/wappalyzer-technology-pro/gppongmhjkpfnbhagpmjfkannfbllamg)
        -   [WhatRuns.](https://www.whatruns.com/)
            
            [Chrome Extensions](https://chrome.google.com/webstore/detail/whatruns/cmkdbmfndkfgebldhnkbfhlneefdaaip?hl=en)
