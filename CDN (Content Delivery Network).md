
# CDN (Content Delivery Network)

**CDN** = Global network of servers delivering content fast, secure, and close to users.

---

## ⚙️ **How It Works**

1. **Caches static files** (HTML, CSS, JS, images).
2. **Routes user** to nearest edge server.
3. **Delivers content:**

   * Cached → Served instantly.
   * Not cached → Pulled from origin, then cached.

---

## ✅ **Why Use a CDN**

* ⚡ **Faster Load Times**
* 🌍 **Lower Latency**
* 📈 **Scalable Traffic Handling**
* 🔁 **Redundancy / Failover**
* 🔒 **Security (DDoS, WAF, TLS)**
* 🎯 **Optimized Delivery** (compression, HTTP/3)

---

## 🎯 **Popular CDNs**

* [Cloudflare](https://www.cloudflare.com)
* [AWS CloudFront](https://aws.amazon.com/cloudfront/)
* [Akamai](https://www.akamai.com)
* [Fastly](https://www.fastly.com)

---

## 🔍 **Detect CDN Usage**

**1. Online Tools:**

* [CDN Finder](https://www.cdnplanet.com/tools/cdnfinder/)
* [WebPageTest](https://webpagetest.org)
* [BuiltWith](https://builtwith.com)

**2. Headers:**

```bash
curl -I https://example.com
```

Look for: `cf-cache-status`, `x-amz-cf-id`, `akamai-*`

**3. DNS Records:**

```bash
dig example.com
```

Look for: `*.cloudflare.net`, `*.fastly.net`, etc.

**4. IP WHOIS:**

```bash
ping example.com
whois <IP>
```

Owned by a CDN? It's using one.

---

## 🧾 TL;DR

**CDN = Speed + Scale + Security**
CDNs cache + route + deliver content fast.
Check headers, DNS, or use tools to spot one.

---

