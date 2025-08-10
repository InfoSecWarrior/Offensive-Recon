
# Autonomous System (AS / ASN / IP) Lookup Guide

An Autonomous System (AS) is a large network managed by a single organization under one routing policy. They form the backbone of internet routing.

---

## What You Can Look Up

| Lookup Type     | Description                                       |
| --------------- | ------------------------------------------------- |
| ASN (AS Number) | Unique identifier like `AS15169` for each AS      |
| AS Name / Org   | Company or entity owning the ASN                  |
| IP → ASN        | Find which AS controls a given IP                 |
| ASN → IP Ranges | List of IP prefixes (CIDR blocks) owned by an ASN |

---

## Online Tools for AS/ASN/IP Lookups

| Tool Name     | Description                           | URL                                                        |
| ------------- | ------------------------------------- | ---------------------------------------------------------- |
| BGP.he.net    | ASN info, prefixes, peers             | [bgp.he.net](https://bgp.he.net)                           |
| IPInfo        | ASN, org, country, geolocation        | [ipinfo.io](https://ipinfo.io)                             |
| CIDR Report   | Prefix aggregation, ASN-to-IP mapping | [cidr-report.org](https://www.cidr-report.org)             |
| RIPEstat      | ASN/IP data, graphs, history          | [stat.ripe.net](https://stat.ripe.net)                     |
| ViewDNS       | ASN org info, IP ranges               | [viewdns.info](https://viewdns.info/asnlookup/)            |
| UltraTools    | ASN + WHOIS details                   | [ultratools.com](https://www.ultratools.com/tools/asnInfo) |
| Linux `whois` | CLI-based ASN/IP lookup               | `whois <IP or ASN>`                                        |
| Team Cymru    | IP → ASN from CLI                     | See below                                                  |

---

## CLI-Based ASN/IP Lookup

### 1. Using `whois` (Linux built-in)

**Command:**

```bash
whois <IP or ASN>
```

**Example:**

```bash
whois 8.8.8.8
whois AS15169
```

**Sample Output:**

```
OrgName:    Google LLC
ASNumber:   AS15169
NetRange:   8.8.8.0 - 8.8.8.255
```

---

### 2. Team Cymru IP → ASN (Supports Bulk Lookups)

**Install:**

```bash
sudo apt install whois
```

**Single IP:**

```bash
whois -h whois.cymru.com " -v 8.8.8.8"
```

**Bulk IP:**

```bash
whois -h whois.cymru.com " -v < your_ip_list.txt"
```

**Sample Output:**

```
AS      | IP        | BGP Prefix   | CC | Registry | Allocated  | AS Name
15169   | 8.8.8.8   | 8.8.8.0/24   | US | arin     | 1992-12-01 | GOOGLE - Google LLC, US
```

---

