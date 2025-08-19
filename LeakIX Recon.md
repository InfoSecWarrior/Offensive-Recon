
# LeakIX Recon – Alternate to Shodan

**LeakIX** is an open-source OSINT engine for finding exposed credentials, leaky databases, and misconfigured services across the internet.
Website: [https://leakix.net](https://leakix.net)

---

## Overview

LeakIX focuses on:

* Exposed credentials (`.env`, `config.json`)
* Open directories (`index of /backup`)
* Misconfigured applications (debug endpoints, admin panels)
* Leaky databases (MongoDB, Redis, Elasticsearch)
* Files containing secrets (`.git`, `.bak`, `.zip`)

---

## Key Features

| Feature                | Description                                  |
| ---------------------- | -------------------------------------------- |
| Full-text Search       | Search by IP, domain, keywords, banners      |
| Leak Detection         | Finds `.env`, `.git`, `backup`, `admin`      |
| Database Reports       | Detects MongoDB, Elasticsearch, Redis leaks  |
| Service Fingerprinting | Shows exposed services and software versions |
| Public + Private Scans | Anonymous or authenticated deep scans        |

---

## Basic Usage

Visit: [https://leakix.net](https://leakix.net)
Search like Google Dorks.

**Examples:**

```
.env
index of /backup
mysql password
site:.gov
product:elasticsearch
```

---

## Common Queries

| Query                   | Purpose                      |
| ----------------------- | ---------------------------- |
| `.env`                  | Leaked environment variables |
| `site:.gov`             | Filter to government domains |
| `product:elasticsearch` | Exposed Elasticsearch        |
| `index of /backup`      | Backup directory listing     |
| `password`              | Passwords in HTTP responses  |
| `config.json`           | App configurations           |
| `mongo` / `redis`       | Unsecured database instances |

---

## Advanced Queries

```
.env AND password
product:elasticsearch country:IN
site:*.edu filetype:bak
"index of /admin"
"DB_PASSWORD" ext:env
"config" AND "token" AND site:*.edu
```

---

## Authenticated Scanning

Register for:

* Custom scans
* Leak monitoring
* API access (beta)

---


