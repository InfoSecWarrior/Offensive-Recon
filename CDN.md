# CDN Detection and Analysis Guide

## Core Definitions

### What is a CDN (Content Delivery Network)?

A **CDN** is a *geographically distributed network of proxy servers and data centers* that work together to provide fast delivery of internet content. By caching content closer to end users, CDNs reduce latency, improve load times, and decrease bandwidth costs.

### What is an Edge Server?

An **Edge Server** is a *CDN server located at the network edge* (closer to end users) that caches and delivers content. When you access a website using CDN, you're typically connecting to an edge server rather than the origin server.

### What is an Origin Server?

The **Origin Server** is the *original web server where content is hosted*. CDNs pull content from origin servers and distribute it across edge servers worldwide.

### What is a PoP (Point of Presence)?

A **PoP** is a *physical location where CDN servers are deployed*. Each PoP contains multiple edge servers and is strategically placed in data centers around the world to minimize distance to users.

### What is BGP (Border Gateway Protocol)?

**BGP** is the *protocol that manages how packets are routed across the internet* between autonomous systems (AS). CDNs use BGP to:
- Announce their IP addresses from multiple locations
- Route users to the nearest edge server
- Implement anycast routing

### What is Anycast?

**Anycast** is a *network addressing method where the same IP address is announced from multiple locations*. CDNs use anycast to automatically route users to the nearest edge server using the same IP address.

### What is an IXP (Internet Exchange Point)?

An **IXP** is a *physical infrastructure where different Internet Service Providers (ISPs) and CDNs connect to exchange traffic*. CDNs place servers at IXPs to reduce latency and costs.

### What is Caching?

**Caching** is the process of *storing copies of files in temporary storage locations* for faster access. CDNs cache static content (images, CSS, JavaScript) and sometimes dynamic content at edge servers.

### What is Cache Hit/Miss?

- **Cache Hit:** When requested content is found in the CDN cache and served directly
- **Cache Miss:** When content isn't in cache and must be fetched from the origin server

### What is a WAF (Web Application Firewall)?

A **WAF** is a *security layer that filters and monitors HTTP traffic* between web applications and the internet. Many CDNs include WAF services to protect against common attacks.

---

## How to Check if a Website is Using a CDN

### 1. Use Online Tools

#### CDN Finder Tools

- **CDNPlanet CDN Finder:** https://www.cdnplanet.com/tools/cdnfinder/
- **DNS Checker:** https://www.whatsmydns.net/
- **WebPageTest:** https://www.webpagetest.org/ → Check the "CDN Provider" column in the result waterfall

**Example Test:**
Test https://www.hotstar.com/ using CDNPlanet:
1. Enter the URL
2. Click "Find CDN"
3. Results will show CDN provider (e.g., "Akamai")

---

### 2. Check HTTP Response Headers

Use `curl` or browser developer tools to inspect HTTP headers:

```bash
curl -I https://example.com
```

**CDN-Specific Headers to Look For:**

| CDN Provider | Header Signatures |
|-------------|------------------|
| **Cloudflare** | `cf-ray`, `cf-cache-status`, `server: cloudflare` |
| **AWS CloudFront** | `x-amz-cf-id`, `x-amz-cf-pop`, `via: CloudFront` |
| **Akamai** | `x-akamai-*`, `akamai-grn`, `server: AkamaiGHost` |
| **Fastly** | `x-served-by`, `x-cache`, `x-fastly-request-id` |
| **Generic CDN** | `x-cache`, `x-cache-hits`, `via`, `age` |

**Example:**
```bash
curl -I https://www.github.com
```
- Look for: x-served-by: cache-sin18040-SIN
- Indicates Fastly CDN usage

---

### 3. Check DNS Records

CDNs often use CNAME records to point domains to their infrastructure:

Using nslookup
```bash
nslookup example.com
```

Using dig (more detailed)
```bash
dig example.com
```

Check CNAME specifically
```bash
dig www.example.com CNAME
```

**Common CDN Domain Patterns:**
- `*.cloudflare.net`
- `*.akamaiedge.net`
- `*.akamaihd.net`
- `*.fastly.net`
- `*.cloudfront.net`
- `*.azureedge.net`
- `*.edgekey.net`
- `*.edgecastcdn.net`

---

### 4. Analyze IP Address Ownership

**Step 1: Get the website IP**
```bash
ping example.com
```
```bash
dig +short example.com
```

**Step 2: Look up IP ownership**
```bash
whois <IP-ADDRESS>
```

**CDN Provider Indicators in WHOIS:**
- **Cloudflare:** "Cloudflare, Inc."
- **Akamai:** "Akamai Technologies"
- **AWS:** "Amazon.com, Inc." or "AMAZON-"
- **Fastly:** "Fastly"

**Example:**
```bash
whois 104.26.10.221
```
```
# OrgName: Cloudflare, Inc.
```
---

### 5. Use Browser Developer Tools

**Steps:**
1. Open **Developer Tools** (F12)
2. Go to **Network** tab
3. Reload the page (Ctrl+R)
4. Click on the main document request
5. Check **Response Headers** section

**What to Look For:**
- Server header indicating CDN
- Cache-related headers
- CDN-specific headers
- Remote Address showing CDN IPs

---

### 6. Use BuiltWith or Wappalyzer

**Technology Detection Tools:**
- **BuiltWith:** https://builtwith.com/
- **Wappalyzer:** https://www.wappalyzer.com/

These browser extensions and websites automatically detect:
- CDN providers
- Web servers
- Analytics tools
- Security services

---

### 7. CDN Performance Checkers

**Test CDN performance globally:**
- **Uptrends:** https://www.uptrends.com/tools/cdn-performance-check
- **DebugBear:** https://www.debugbear.com/test/cdn-performance

These tools show:
- Response times from different locations
- CDN PoP locations serving content
- Cache hit rates
- Performance metrics

---

## CDN Detection Summary Table

| Method | Command/Tool | Pros | Cons |
|--------|-------------|------|------|
| **Online Tools** | CDNPlanet, BuiltWith | Easy, comprehensive | Requires web access |
| **HTTP Headers** | `curl -I` | Quick, accurate | Command line knowledge |
| **DNS Records** | `dig`, `nslookup` | Shows infrastructure | May not show all CDNs |
| **IP Lookup** | `whois` | Confirms ownership | IPs can be shared |
| **Browser Tools** | DevTools (F12) | Visual, detailed | Manual process |
| **Detection Tools** | Wappalyzer | Automatic | May miss custom CDNs |

---
