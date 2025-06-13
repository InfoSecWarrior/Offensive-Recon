
# 🛰️ [AS / ASN / IP Lookup](https://en.wikipedia.org/wiki/Autonomous_system_%28Internet%29)

**Autonomous Systems (AS)** = Internet’s backbone routes, each with a unique ASN (e.g., `AS15169` for Google).

---

## 📌 [What You Can Lookup](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)

| 🔍 Type      | 🧠 Info It Gives                |
| ------------ | ------------------------------- |
| ASN          | Unique AS Number like `AS13335` |
| AS Org Name  | Entity owning that ASN          |
| IP → ASN     | Who controls the IP             |
| ASN → Ranges | CIDR blocks used by that AS     |

---

## 🌐 \[Top Online Lookup Tools]

| Tool                                                                        | Link                   |
| --------------------------------------------------------------------------- | ---------------------- |
| **[bgp.he.net](https://bgp.he.net)**                                        | ASN, routes, BGP peers |
| **[ipinfo.io](https://ipinfo.io)**                                          | ASN + Geo + Org        |
| **[stat.ripe.net](https://stat.ripe.net)**                                  | ASN graphs, history    |
| **[cidr-report.org](https://www.cidr-report.org)**                          | IP prefix reports      |
| **[viewdns.info](https://viewdns.info/asnlookup/)**                         | ASN + IP ranges        |
| **[ultratools.com](https://www.ultratools.com/tools/asnInfo)**              | WHOIS + ASN Info       |
| **[Team Cymru](https://team-cymru.com/community-services/ip-asn-mapping/)** | CLI ASN ↔ IP lookups   |

---

## 💻 \[CLI ASN/IP Lookups]

### 🔹 Linux `whois`

```bash
whois 8.8.8.8
whois AS15169
```

Output:
`Google LLC`, ASN `AS15169`, Net `8.8.8.0/24`

---

### 🔹 [Team Cymru](https://team-cymru.com/community-services/ip-asn-mapping/)

```bash
sudo apt install whois
whois -h whois.cymru.com " -v 8.8.8.8"
```

Bulk:

```bash
whois -h whois.cymru.com " -v < your_ips.txt"
```

Sample:

```
AS      | IP        | Prefix       | Org
15169   | 8.8.8.8   | 8.8.8.0/24   | GOOGLE
```

---

## 🛠️ \[Automate It]

Want to:

* Bulk lookup 1,000s of IPs?
* Export JSON/CSV?
* Auto-resolve ASN info?

→ Ping me. I’ll drop a 🔥 Bash or Python script.

---

> 💡 **Red Team Pro Tip**: Combine `whois` + `nmap` + `dig` for OSINT magic. 🧠🔧

---

