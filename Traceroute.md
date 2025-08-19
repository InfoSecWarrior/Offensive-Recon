# Network Path Analysis with Traceroute

Traceroute is an essential network diagnostic tool that maps the path packets take from source to destination, revealing routing issues, latency problems, and network topology. This guide covers theory, tools, and practical implementation across multiple platforms.

---

## What is Traceroute?

Traceroute is a network diagnostic tool that discovers and displays the route (path) packets take across an IP network. It identifies:
- Each router (hop) along the path
- Round-trip time (RTT) to each hop
- Potential points of failure or congestion

### How It Works

1. **TTL Mechanism**: Sends packets with incrementally increasing Time-to-Live (TTL) values starting at 1
2. **ICMP Response**: When TTL expires at a router, it returns an ICMP "Time Exceeded" message
3. **Path Discovery**: Each response reveals one hop in the path
4. **Completion**: Process continues until destination is reached or max hops exceeded

### Network Path Fundamentals

- **Network Path**: Sequence of routers packets traverse between source and destination
- **Hop**: Each router that forwards the packet
- **RTT**: Round-trip time for packet to reach hop and return
- **Protocol Options**: UDP (default Linux), ICMP (default Windows), TCP (firewall bypass)

---

## Traceroute Tools Comparison

| Tool              | Platform       | Protocol Options          | Root Required | Key Feature                        |
|:------------------|:---------------|:--------------------------|:--------------|:-----------------------------------|
| **traceroute**    | Linux/Unix     | UDP (default), ICMP, TCP  | For TCP only  | Most flexible, highly configurable |
| **tracert**       | Windows        | ICMP only                 | No            | Simple, built-in Windows tool      |
| **mtr**           | Linux/Unix     | ICMP (default), UDP       | No            | Real-time statistics + traceroute  |
| **tcptraceroute** | Linux/Unix     | TCP only                  | Yes           | Firewall bypass specialist         |
| **tracepath**     | Linux          | UDP only                  | No            | Lightweight, MTU discovery         |
| **nmap**          | Cross-platform | ICMP, UDP, TCP            | Yes           | Integration with port scanning     |

### Protocol Capability Matrix

| Tool                   | UDP Support | ICMP Support | TCP Support | Notes                           |
|:-----------------------|:------------|:-------------|:------------|:--------------------------------|
| **traceroute (Linux)** | ✅ Default  | ✅ (`-I`)    | ✅ (`-T`)   | Most versatile tool             |
| **tracert (Windows)**  | ❌          | ✅ Default   | ❌          | ICMP Echo Requests only         |
| **mtr**                | ✅ (`--udp`)| ✅ Default   | ⚠️          | TCP requires patches/scripts    |
| **tcptraceroute**      | ❌          | ❌           | ✅ Default  | Designed for TCP specifically   |
| **tracepath**          | ✅ Default  | ❌           | ❌          | UDP-only, no root needed        |

---

## 3. Practical Commands and Examples

### Linux traceroute

Basic UDP Traceroute (Default)
```bash
traceroute google.com
```

ICMP Traceroute (Like Windows)
```bash
traceroute -I google.com
```

TCP Traceroute for HTTPS port
```bash
sudo traceroute -T -p 443 google.com
```

TCP Traceroute for HTTP port
```bash
sudo traceroute -T -p 80 google.com
```

No DNS resolution (faster)
```bash
traceroute -n google.com
```

Specify max hops and timeout
```bash
traceroute -m 30 -w 2 google.com
```

Multiple queries per hop
```bash
traceroute -q 5 google.com
```

### Windows tracert

Basic usage
```cmd
tracert google.com
```

No DNS resolution
```cmd
tracert -d google.com
```

Custom timeout and max hops
```cmd
tracert -w 1000 -h 20 google.com
```

### MTR (My Traceroute)

Interactive mode
```bash
mtr google.com
```

Report mode with 100 cycles
```bash
mtr -r -c 100 google.com
```

UDP mode
```bash
mtr --udp google.com
```

TCP mode (if supported)
```bash
mtr --tcp --port 443 google.com
```

### TCP Traceroute

Trace to web server on port 80
```bash
sudo tcptraceroute google.com 80
```

Trace to HTTPS server
```bash
sudo tcptraceroute google.com 443
```

Trace to mail server
```bash
sudo tcptraceroute mail.google.com 25
```

### Tracepath

Basic usage (no root required)
```bash
tracepath google.com
```

Specify port
```bash
tracepath -p 33434 google.com
```

---

## 4. Real-World Analysis Examples

### Example 1: Standard Traceroute Output

```
traceroute to 1.1.1.1 (1.1.1.1), 64 hops max, 52 byte packets
 1  myrouter (192.168.47.1)  2.755 ms  1.452 ms  1.325 ms
 2  * * *
 3  69.168.32.65 (69.168.32.65)  18.159 ms  18.658 ms  15.091 ms
 4  * * *
 5  206.126.237.30 (206.126.237.30)  30.453 ms  50.242 ms  24.342 ms
 6  one.one.one.one (1.1.1.1)  29.000 ms  26.784 ms  26.017 ms
```

**Analysis**:
- Hop 1: Local router (low latency)
- Hops 2,4: No response (firewall/filtering)
- Hop 3,5: ISP routers
- Hop 6: Destination reached

### Example 2: MTR Clean Path

```
HOST: myrouter              Loss%  Snt  Last   Avg  Best  Wrst StDev
  1.|-- 10.10.1.1           0.0%   10   0.3   0.4   0.3   0.4   0.0
  2.|-- 141.0.147.177       0.0%   10   2.7   2.7   2.5   3.1   0.2
  3.|-- 172.16.28.38        0.0%   10   2.8   6.4   2.8  22.2   6.1
  4.|-- 172.17.13.76        0.0%   10   1.1   2.8   1.1  14.6   4.2
  5.|-- 172.17.13.49        0.0%   10   1.4   4.0   1.3  25.0   7.4
  6.|-- 172.17.13.24        0.0%   10   2.5   2.7   2.0   5.1   1.1
  7.|-- one.one.one.one     0.0%   10   1.3   1.2   1.2   1.3   0.0
```

**Analysis**:
- All hops show 0% packet loss (healthy connection)
- Low latency throughout (avg 1.2ms to destination)
- Some variance in hop 3-5 (StDev indicates jitter)
- Overall excellent path quality

---
