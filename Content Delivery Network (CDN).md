
## Content Delivery Network (CDN)

A CDN is a geographically distributed network of servers that delivers web content faster by caching static and dynamic assets closer to users. This improves performance, reliability, and security.

### How a CDN Works

1. **Caching** – Stores static assets (HTML, CSS, JS, images, videos) from the origin server.
2. **Routing Requests** – Directs users to the nearest or optimal edge server.
3. **Content Delivery** – Serves cached content instantly; if not cached, fetches from origin, caches, and delivers.
4. **Dynamic Content Optimization** – Improves routing, reduces latency, and uses TCP/UDP optimizations.

### Key Benefits

* **Faster Performance** – Reduces load time by serving content from nearby servers.
* **Lower Latency** – Minimizes delays from long-distance data travel.
* **Scalability** – Handles traffic spikes without overloading the origin server.
* **High Availability** – Load balancing and automatic failover.
* **Security** – DDoS protection, WAF support, TLS/SSL encryption.
* **Optimized Delivery** – Image/video compression, Brotli/Gzip, HTTP/2, QUIC/HTTP/3 support.

### Common Use Cases

* Video streaming platforms
* E-commerce sites
* Global SaaS applications
* News/media outlets
* Online gaming

### Popular CDN Providers

* Cloudflare
* Amazon CloudFront (AWS)
* Akamai
* Fastly

### Additional Considerations

* **Cache Invalidation** – Purge outdated content when updated.
* **Analytics & Reporting** – Monitor traffic, detect threats, measure performance.
* **Edge Computing** – Execute code at the edge for personalization and API modifications.

---

## Detecting CDN Usage

### Tools

* CDN Finder (CDNPlanet)
* What's My DNS
* WebPageTest (CDN Provider column)

### HTTP Headers

```bash
curl -I https://example.com
```

Look for:
`cf-ray`, `cf-cache-status` (Cloudflare)
`x-amz-cf-id` (AWS CloudFront)
`x-akamai-*` (Akamai)
`x-cache`, `via` (Generic CDN)

### DNS Records

```bash
nslookup example.com
dig example.com
```

Check for:
`*.cloudflare.net`, `*.akamaiedge.net`, `*.fastly.net`

### IP Ownership

```bash
ping example.com
whois <IP-ADDRESS>
```

Match IP to CDN provider.

### Browser Developer Tools

* Open Network tab
* Reload page
* Check headers for CDN location clues

### BuiltWith / Wappalyzer

Full tech stack details including CDN detection.

---

