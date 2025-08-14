# SSL/TLS Certificate History Lookup

SSL/TLS Certificate History Lookup is a reconnaissance technique used to search public logs of all issued SSL certificates for a given domain. Because these logs are a mandatory part of the modern web, they create a rich, historical database perfect for discovering an organization's digital footprint.

---

## How It Works: The Role of Certificate Transparency (CT)

This entire process is possible thanks to **Certificate Transparency (CT)**, a public framework created to make the SSL/TLS certificate system more auditable and transparent.

- **What it is:** A system of public, append-only logs.
- **How it works:** When a Certificate Authority (CA) issues a certificate for a domain (e.g., `shop.example.com`), it *must* submit that certificate to multiple CT logs.
- **Why it helps attackers:** These logs are publicly accessible and searchable. By querying them, anyone can see a historical record of every public certificate ever issued for `example.com` and all its subdomains.

---

## Use Cases: Why This Is a Powerful Technique

| Use Case | Description |
| :--- | :--- |
| **Subdomain Discovery** | The primary use. Uncover hidden or forgotten subdomains like `dev.`, `vpn.`, `test.`, `api.`, and `admin.`, which often have weaker security. |
| **Infrastructure Mapping** | Understand how an organization structures its services and which hosts are tied to specific functions. |
| **Historical Analysis** | See which subdomains were active in the past. This can reveal old infrastructure that might still be online but unmaintained. |
| **OSINT & Recon** | A fundamental step in penetration testing and bug bounties to expand the attack surface and find more potential targets. |
| **Security Auditing** | Defensively, this helps organizations find forgotten assets or detect unauthorized certificates issued for their domains. |

---

## Methods for Certificate History Lookup

There are three primary ways to access this information, ranging from easy-to-use web tools to advanced manual queries.

### Method 1: Online Web-Based Tools (The Easy Way)

These websites provide a user-friendly interface to search CT logs.

| Tool | Description & URL |
| :--- | :--- |
| **crt.sh** | The de-facto standard. It's a simple, fast, and comprehensive web tool for searching CT logs. **URL:** [https://crt.sh/](https://crt.sh/) |
| **Censys** | A powerful search engine for internet-connected devices. Its certificate search uses a more advanced query language and can find certificates based on many different fields. **URL:** [https://search.censys.io/certificates](https://search.censys.io/certificates) |
| **CertSpotter** | An SSL certificate monitoring service by SSLMate that also provides a public search interface for CT logs. **URL:** [https://sslmate.com/certspotter/](https://sslmate.com/certspotter/) |

#### Example Walkthrough with `crt.sh`

1. **Navigate to** [https://crt.sh/](https://crt.sh/).
2. **Perform a Search:** To find all certificates for a domain and its subdomains, use the `%` character as a wildcard before the domain name.
   ```
   %.example.com
   ```
3. **Analyze the Results:** Look at the **"Matching Identities"** column. This column lists all the domain names (Subject Alternative Names or SANs) included in the certificate, which is often the best place to find a list of related subdomains.

---

### Method 2: Command-Line Tools (For Automation)

These tools are ideal for scripting, automation, and integrating into a larger reconnaissance workflow.

| Tool | Description & Example Command |
| :--- | :--- |
| **Subfinder** | A popular and fast subdomain discovery tool that aggregates results from many sources, including multiple CT log services. |
| | `go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` <br> `subfinder -d example.com` |
| **Amass** | Part of the OWASP project, Amass is an extremely powerful framework for in-depth network mapping and asset discovery. It heavily utilizes CT logs. |
| | `go install -v github.com/owasp-amass/amass/v4/...@master` <br> `amass enum -d example.com` |
| **ctfr** | A Python script specifically designed to crawl `crt.sh` to find subdomains for a given domain. |
| | `git clone https://github.com/UnaPibaGeek/ctfr.git` <br> `cd ctfr` <br> `pip3 install -r requirements.txt` <br> `python3 ctfr.py -d example.com` |

---

### Method 3: Manual API Queries (The Expert Way)

For a deep understanding, you can query a CT Log's API directly. This shows you exactly where the tools get their data. Let's use Google's CT Log as an example.

1. **Find a CT Log Server:** A list of known logs is available online. We'll use Google's "Argon2024" log.

2. **Construct the API URL:** The API endpoint to get entries is `https://ct.googleapis.com/logs/argon2024/ct/v1/get-entries`. It requires `start` and `end` parameters to define the range of entries to fetch.

3. **Make the Request using `curl`:** We'll fetch a single entry (entry 0).
   ```bash
   curl 'https://ct.googleapis.com/logs/argon2024/ct/v1/get-entries?start=0&end=0'
   ```

4. **Decode the Response:** The response is a JSON object. The certificate data inside is Base64 encoded and needs to be decoded and parsed (often using tools like OpenSSL) to read the domain names. This is a complex process, which is why automated tools are so popular.

This manual method demonstrates the raw, programmatic access available and highlights the value provided by the tools that automate this parsing for you.

---

## Defensive Tips (For Blue Team)

- **Use Wildcard Certificates:** A certificate for `*.example.com` will appear in logs, but it won't reveal the specific subdomains (`dev.`, `test.`, etc.) that use it. **Trade-off:** If the private key for a wildcard certificate is ever compromised, all your subdomains are at risk.

- **Monitor CT Logs for Your Domain:** Use services like CertSpotter or build your own scripts to alert you whenever a new certificate is issued for your domains. This helps you spot unauthorized certificates immediately.

- **Maintain a Comprehensive Asset Inventory:** The best defense is to have a complete, up-to-date inventory of all your domains and subdomains. If you know what you own, nothing discovered in CT logs will be a surprise.

  ---
  
