
# 🌐 [IP Traceroute Tool](https://en.wikipedia.org/wiki/Traceroute)

Tracks packet routes from source to destination. Diagnoses **delays**, **hops**, **routing loops**.

---

## ⚙️ [How It Works](https://www.cloudflare.com/learning/network-layer/what-is-traceroute/)

* Sends packets with **increasing TTL**
* Routers return `Time Exceeded` ICMP
* Reveals each hop till target

---

## 🧰 [Popular Tools](https://en.wikipedia.org/wiki/Traceroute#Variants)

| Tool                                                                                                  | OS      | Type        |
| ----------------------------------------------------------------------------------------------------- | ------- | ----------- |
| [`traceroute`](https://linux.die.net/man/8/traceroute)                                                | Linux   | UDP/ICMP    |
| [`tracert`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert) | Windows | ICMP        |
| [`mtr`](https://github.com/traviscross/mtr)                                                           | Linux   | Real-time   |
| [`tcptraceroute`](https://github.com/mct/tcptraceroute)                                               | Linux   | TCP         |
| [`tracepath`](https://man7.org/linux/man-pages/man8/tracepath.8.html)                                 | Linux   | Lightweight |
| [`nmap --traceroute`](https://nmap.org/book/man-host-discovery.html)                                  | All     | Built-in    |

---

## 🔍 Examples

```bash
traceroute google.com        # Linux
tracert google.com           # Windows
mtr google.com               # Real-time
sudo tcptraceroute google.com 80
tracepath google.com
```

---

## 🌐 \[Online Tools]

| Tool                  | Link                                                     |
| --------------------- | -------------------------------------------------------- |
| GRC DNS Traceroute    | [🔗](https://www.grc.com/dns/traceroute.htm)             |
| Ping.eu               | [🔗](https://ping.eu/traceroute/)                        |
| DNSChecker            | [🔗](https://dnschecker.org/ip-traceroute.php)           |
| T1 Shopper            | [🔗](https://www.t1shopper.com/tools/trace-route/)       |
| YouGetSignal (Visual) | [🔗](https://www.yougetsignal.com/tools/visual-tracert/) |

---

## 📊 [Comparison Table](https://en.wikipedia.org/wiki/Traceroute#Implementations)

| Tool          | Protocol | Strength                      |
| ------------- | -------- | ----------------------------- |
| traceroute    | UDP/ICMP | Classic + flexible            |
| tracert       | ICMP     | Fast on Windows               |
| mtr           | ICMP/UDP | Live stats, packet loss       |
| tcptraceroute | TCP      | Good behind firewalls         |
| tracepath     | UDP      | MTU discovery, no root needed |

---

## ⚙️ [Advanced Flags](https://man7.org/linux/man-pages/man8/traceroute.8.html)

| Flag | Use                      |
| ---- | ------------------------ |
| `-n` | Skip DNS lookup (faster) |
| `-w` | Set timeout              |
| `-q` | Set probes per hop       |
| `-m` | Max TTL                  |

```bash
traceroute -I example.com           # ICMP mode
sudo traceroute -T -p 443 -n google.com  # TCP/HTTPS style
```

---

## 🧠 Pro Tips

* **ICMP/UDP blocked?** → Use TCP (`-T`)
* **No root?** → Use `tracepath`
* **Want live stats?** → Use `mtr`

---

