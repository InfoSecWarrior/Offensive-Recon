# Reverse Lookup Techniques

A comprehensive guide to all reverse lookup methods for reconnaissance and OSINT.

---
## 1. Reverse IP Lookup

**Purpose**: Find all domains hosted on the same IP address.

### Online Tools

| Tool | URL |
|:-----|:----|
| ViewDNS | [https://viewdns.info/reverseip/](https://viewdns.info/reverseip/) |
| HackerTarget | [https://hackertarget.com/reverse-ip-lookup/](https://hackertarget.com/reverse-ip-lookup/) |
| SecurityTrails | [https://securitytrails.com/](https://securitytrails.com/) |
| DNSlytics | [https://dnslytics.com/reverse-ip](https://dnslytics.com/reverse-ip) |

### Commands

Get IP of domain:
```bash
dig +short example.com
```

Using SecurityTrails API:
```bash
curl -H "APIKEY: YOUR_KEY" "https://api.securitytrails.com/v1/ips/nearby/192.168.1.1"
```

---

## 2. Reverse DNS Lookup (PTR)

**Purpose**: Find hostname associated with an IP address.

### Commands

Using dig:
```bash
dig -x 8.8.8.8
```

Using host:
```bash
host 8.8.8.8
```

Using nslookup:
```bash
nslookup 8.8.8.8
```

### Online Tools
- [MXToolbox](https://mxtoolbox.com/ReverseLookup.aspx)
- [DNSChecker](https://dnschecker.org/reverse-dns-lookup.php)

---

## 3. Reverse Mail Server (MX) Lookup

**Purpose**: Find all domains using the same mail server.

### Process

Step 1 - Find MX record:
```bash
dig +short example.com mx
```

Step 2 - Reverse lookup using:

| Tool | URL | Input |
|:-----|:----|:------|
| ViewDNS | [https://viewdns.info/reversemx/](https://viewdns.info/reversemx/) | MX hostname |
| SecurityTrails | [https://securitytrails.com/](https://securitytrails.com/) | Search: `mx:mail.server.com` |

---

## 4. Reverse Name Server (NS) Lookup

**Purpose**: Find all domains using the same nameserver.

### Online Tools

| Tool | URL | Features |
|:-----|:----|:---------|
| ViewDNS | [https://viewdns.info/reversens/](https://viewdns.info/reversens/) | Free, no registration |
| DNSlytics | [https://dnslytics.com/reverse-ns](https://dnslytics.com/reverse-ns) | Detailed analytics |
| SecurityTrails | [https://securitytrails.com/](https://securitytrails.com/) | Search: `ns:ns1.example.com` |

### Process

Find NS records:
```bash
dig +short example.com ns
```

Then use nameserver in reverse lookup tools above.

---

## 5. Reverse WHOIS Lookup

**Purpose**: Find all domains registered by same entity.

### Search By

- **Email**: Find domains registered with same email
- **Organization**: Find domains by company name
- **Name**: Find domains by registrant name

### Tools

| Tool | URL | Search Options |
|:-----|:----|:---------------|
| ViewDNS | [https://viewdns.info/reversewhois/](https://viewdns.info/reversewhois/) | Name, email |
| WhoisXMLAPI | [https://reverse-whois.whoisxmlapi.com/](https://reverse-whois.whoisxmlapi.com/) | Comprehensive |
| DomainTools | [https://reversewhois.domaintools.com/](https://reversewhois.domaintools.com/) | Professional tool |

---

## 6. Reverse SSL Certificate Lookup

**Purpose**: Find all domains with certificates from same organization.

### Using crt.sh

Search by organization:
```
https://crt.sh/?O=Example%20Company
```

Search by domain pattern:
```
https://crt.sh/?q=%.example.com
```

### Command Line

Using crt.sh API:
```bash
curl -s "https://crt.sh/?q=%.example.com&output=json" | jq -r '.[].name_value' | sort -u
```

---

## 7. Reverse Analytics Lookup

**Purpose**: Find domains using same Google Analytics, AdSense IDs.

### Tools

| Tool      | URL                                              | Tracks                  |
| :-------- | :----------------------------------------------- | :---------------------- |
| AnalyzeID | [https://analyzeid.com/](https://analyzeid.com/) | Multiple tracking codes |
| DNSlytics | [https://dnslytics.com/](https://dnslytics.com/) | Various identifiers     |

---

## 8. Reverse ASN Lookup

**Purpose**: Find all IP ranges and domains in an AS (Autonomous System).

### Find ASN

Using whois:
```bash
whois -h whois.radb.net 8.8.8.8
```

### ASN Lookups

| Tool | URL |
|:-----|:----|
| BGPView | [https://bgpview.io/](https://bgpview.io/) |
| Hurricane Electric | [https://bgp.he.net/](https://bgp.he.net/) |
| IPinfo | [https://ipinfo.io/](https://ipinfo.io/) |

---

## Automation Commands

### Get all domains on same IP:
```bash
curl -s "https://api.hackertarget.com/reverseiplookup/?q=192.168.1.1"
```

### Get all domains with same nameserver:
```bash
curl -s "https://api.securitytrails.com/v1/search/list" -H "APIKEY: YOUR_KEY" -H "Content-Type: application/json" -d '{"filter": {"ns": "ns1.example.com"}}'
```

### Find subdomains via SSL:
```bash
curl -s "https://crt.sh/?q=%.example.com&output=json" | jq -r '.[].name_value' | sort -u
```

---
---
