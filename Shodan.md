Shodan is a powerful search engine specifically designed to help security researchers and network administrators discover devices and services connected to the internet. When conducting reconnaissance using Shodan, you can gather valuable insights about exposed systems and services that might be potential security risks.

Shodan is a search engine for finding devices and systems exposed to the internet. It allows advanced search queries using filters to refine results. Here are some commonly used Shodan search filters:

  →          https://www.shodan.io/

Setting up a Shodan Account

Create a Shodan account on Shodan’s website.

Obtain the API key from your account dashboard for advanced queries and automation. (Only used for CLI searches)

---

### Exploring Shodan Search

General Search: Type a service or technology (e.g., apache, ftp, wordpress, etc.)

### Search Filters in Shodan

  →     https://www.shodan.io/search/filters

Filters: Narrow your search with filters like:

`country:`      (e.g., `country:IN` for India)

`city:`         (e.g., `city:delhi`)

`port:`         (e.g., `port:22`)

`org:`          (e.g., `org:Google`)

`product:`      (e.g., `product:nginx`)

`Example:`      `apacheport:80 country:US`.

---

### **Basic Shodan Filters**

1. **`ip:`** Find devices at a specific IP address.
    
    **Example:** `ip:8.8.8.8`
    
2. **`port:`** Search for services running on a specific port.
    
    **Example:** `port:22` (Search for SSH servers)
    
3. **`hostname:`** Find devices with specific hostnames.
    
    **Example:** `hostname:example.com`
    
4. **`org:`** Search for devices belonging to a specific organization.
    
    **Example:** `org:"Google"`
    
5. **`city:`** Search for devices in a specific city.
    
    **Example:** `city:"New York"`
    
6. **`country:`** Search for devices in a specific country.
    
    **Example:** `country:"US"`
    
7. **`geo:`** Find devices at specific geographic coordinates (latitude,longitude).
    
    **Example:** `geo:37.7749,-122.4194`
    
8. **`asn:`** Search devices based on an ASN (Autonomous System Number).
    
    **Example:** `asn:15169` (Google's ASN)
    

---

### **Advanced Filters**

1. **`after:` / `before:`** Find results based on when they were discovered.
    
    **Example:** `after:2025-01-01` (After January 1, 2025)
    
2. **`title:`** Search for specific words in the HTML title.
    
    **Example:** `title:"Login Page"`
    
3. **`product:`** Search for specific software or services.
    
    **Example:** `product:"Apache"`
    
4. **`version:`** Combine with `product:` to search for specific versions of software.
    
    **Example:** `product:"nginx" version:"1.18.0"`
    
5. **`os:`** Search for specific operating systems.
    
    **Example:** `os:"Windows"`
    
6. **`device:`** Search for specific types of devices.
    
    **Example:** `device:"router"`
    
7. **`ssl:`** Search for SSL certificate information.
    
    **Example:** `ssl:"Let's Encrypt"`
    

---

### **Combined Searches**

You can combine multiple filters for precise searches using logical operators like `AND`, `OR`, and `NOT`.

**Example:** `country:"IN" port:3389 product:"Remote Desktop"`

---

### **Shodan Specific Tags**

1. **`vuln:`** Search for devices with specific vulnerabilities (CVE).
    
    **Example:** `vuln:CVE-2021-44228`
    
2. **`category:`** Filter results by Shodan tags or categories.
    
    **Example:** `category:"industrial-control-systems"`
    
    1. **`tag:`** Search devices with specific tags assigned by Shodan.
    
    **Example:** `tag:"webcam"`
    

---

If you're using the Shodan API or web interface, you can combine these filters to create more refined queries. Always ensure ethical and legal usage when exploring Shodan!

---

## Shodan Search Filters in Table Form

  →     https://www.shodan.io/search/filters

Here's a table summarizing all the Shodan search filters for easy reference:

| **Filter** | **Description** | **Example** |
| --- | --- | --- |
| **`ip:`** | Search devices at a specific IP address. | `ip:8.8.8.8` |
| **`port:`** | Search for services running on a specific port. | `port:22` |
| **`product:`** | Search for devices running specific software or services. | `product:"Apache"` |
| **`asn:`** | Search devices based on an ASN (Autonomous System Number). | `asn:15169` |
| **`net:`** | Search for devices within a specific IP range or subnet. | `net:192.168.1.0/24` |
| **`hostname:`** | Search devices with specific hostnames. | `hostname:example.com` |
| **`os:`** | Search for specific operating systems. | `os:"Windows"` |
| **`country:`** | Search devices in a specific country. | `country:"US"` |
| **`city:`** | Search devices in a specific city. | `city:"Delhi"` |
| **`geo:`** | Search devices at specific geographic coordinates (latitude, longitude). | `geo:37.7749,-122.4194` |
| **`org:`** | Search devices belonging to a specific organization. | `org:"Google"` |
| **`title:`** | Search for specific words in the HTML title of a webpage. | `title:"Login Page"` |
| **`after:`** | Find results discovered after a specific date. | `after:2025-01-01` |
| **`before:`** | Find results discovered before a specific date. | `before:2024-12-31` |
| **`version:`** | Combine with `product:` to search for specific software versions. | `product:"nginx" version:"1.18.0"` |
| **`device:`** | Search for specific types of devices (e.g., routers, webcams). | `device:"router"` |
| **`ssl:`** | Search for SSL certificate information. | `ssl:"Let's Encrypt"` |
| **`vuln:`** | Search for devices with specific vulnerabilities (CVE). | `vuln:CVE-2021-44228` |
| **`category:`** | Filter results by Shodan categories or tags. | `category:"industrial-control-systems"` |
| **`tag:`** | Search for devices with specific tags assigned by Shodan. | **`tag:"webcam"`** |
| **`hash:`** | Search for devices using a specific favicon hash (useful for identifying web apps). | **`hash:123456789`** |
| **`http.favicon.hash:`** | Search for devices using a specific favicon hash (calculated using the MurmurHash3 algorithm). | **`http.favicon.hash:-123456789`** |
| **`http.component:`** | Search for devices running specific web components (e.g., frameworks, libraries, plugins). | **`http.component:"jquery"`** |
| **`hash_screenshot:`** | Search for devices with a specific screenshot hash (hash of the image content of the device's UI). | `hash_screenshot:-987654321` |

### **Logical Operators**

- **`AND`**: Combine filters (default behavior). **Example:** `country:"US" port:80`
- **`OR`**: Match any of the specified filters. **Example:** `port:22 OR port:443`
- **`NOT`**: Exclude specific filters. **Example:** `country:"US" NOT port:80`

Let me know if you need more details!

---

### Examples:

  https://www.shodan.io/search/examples

 `port:22`

`port:21`

`port:8080 Apache`

`port:8080 iis`

`server:Microsoft-IIS/7.5`

`port:8080 product:"Apache Tomcat/Coyote JSP engine"`

`port:8080 product:"Apache Tomcat"`

`product:"Apache Tomcat"`

`http.favicon.hash:-297069493`

`country:"IN" city:"Mumbai"`

`org:google`

`http.component:"woocommerce"`

`http.component:"angular" country:"US" port:443`

`NOT http.component:"react"`

`http.component:"PHP"`

`http.component:"MySQL"`

`http.component:"WordPress"`

`http.component:"Yoast SEO"`

`http.component:"wordpress" http.status:200`

`http.component:"wordpress" http.status:200 port:443 product:"Apache httpd" version:"2.4.52"`

`http.component:"wordpress" has_screenshot:True`

---

***If you only have one result from the keyword then you can try searching the facivon icon of that one result to have more search results***

***If your account don’t have the power to search the CVE in Shodan then search the vulnerable version which is vulnerable from the CVE***

---

### Setting Up Shodan API Key in CLI / Setting Up Shodan API Key in Shodan Tool

  → Click on “Account”

  → Then Under “API Key” click “Show”

  → Copy the API Key

```bash
# shodan -h
```

```bash
# shodan init <API Key>
```

The API Key will be setted to your Shodan CLI Tool

---
