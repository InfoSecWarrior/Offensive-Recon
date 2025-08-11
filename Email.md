

## Email Tracking & Protocols

### What is Email?

**Email (Electronic Mail)** is a method for sending and receiving messages over the internet, enabling communication between users across various platforms and devices.

### Three Parts of an Email Address

**Example**: [sachin@armourinfosec.com](mailto:sachin@armourinfosec.com)

1. **Username (sachin)**: The unique identifier for the user’s account.
2. **Separator (@)**: Connects the username to the domain.
3. **Domain ([armourinfosec.com](http://armourinfosec.com/))**: Represents the organization, company, or service hosting the email.

---

### Mail User Agent (MUA)

**Definition**: A Mail User Agent (MUA) is software that enables users to compose, send, and receive emails.

### Examples of MUA Programs:

- **Microsoft Outlook**: Desktop email client for managing emails, calendars, and contacts.
- **Mozilla Thunderbird**: Open-source email client with robust customization options.

### Web-Based MUA Clients:

- **Gmail**: Google’s web-based email service.
- **Yahoo Mail**: Yahoo’s email platform.
- [**Outlook.com**](http://outlook.com/): Microsoft’s web-based email service.

---

### Mail Delivery Agent (MDA)

**Definition**: A Mail Delivery Agent (MDA) is software responsible for receiving emails from the Mail Transfer Agent (MTA) and delivering them to the recipient’s mailbox.

### MDA Workflow:

1. **Sender MUA** → **Sender MTA** → **Recipient MTA** → **MDA** → **Recipient Mailbox**.
    - The MTA routes the email to the recipient’s mail server.
    - The MDA delivers the email to the recipient’s mailbox (e.g., /var/mail/username or a Maildir structure).

### Common MDA Protocols:

| **Protocol** | **Description** | **Default Port** | **Secure Port** |
| --- | --- | --- | --- |
| **POP3** | Downloads emails to the client, typically deleting them from the server. | 110 | 995 (SSL/TLS) |
| **IMAP** | Accesses emails on the server, syncing across multiple devices. | 143 | 993 (SSL/TLS) |

### Popular MDA Software:

| **MDA Tool** | **Description** |
| --- | --- |
| **Procmail** | One of the oldest MDAs, supports advanced filtering and sorting of emails. |
| **Maildrop** | Lightweight MDA, commonly used with the Courier mail server. |
| **Dovecot** | Popular for IMAP/POP3 services and mailbox delivery. |
| **Postfix (Local)** | Can function as an MDA for local delivery when configured. |
| **Fetchmail** | Retrieves emails from remote servers, often used with an MDA for local delivery. |

### Key Points:

- The MDA **does not send emails**; it only handles local delivery to the recipient’s mailbox.
- MDAs may perform tasks like filtering, sorting, or forwarding emails based on rules.

---

### Mail Transfer Agent (MTA)

**Definition**: A Mail Transfer Agent (MTA) is software responsible for sending, receiving, and routing email messages between mail servers.

### What Does an MTA Do?

- Accepts outgoing emails from the sender’s MUA.
- Routes emails to the recipient’s MTA (or relays through intermediate MTAs).
- Hands off emails to the MDA for final delivery to the recipient’s mailbox.

### MTA Workflow:

**Sender MUA** → **Sender MTA** → **[Internet]** → **Recipient MTA** → **MDA** → **Recipient Mailbox**.

### Protocol Used:

| **Protocol** | **Purpose** | **Port (Unencrypted)** | **Port (Encrypted)** |
| --- | --- | --- | --- |
| **SMTP** | Sending and relaying emails | 25 | 465 (SSL), 587 (STARTTLS) |

### Popular MTA Software:

| **MTA Tool** | **Description** |
| --- | --- |
| **Postfix** | Secure, fast, and widely used open-source MTA (common default on Linux). |
| **Sendmail** | One of the earliest MTAs, powerful but complex to configure. |
| **Exim** | Flexible MTA, often used in cPanel hosting environments. |
| **Qmail** | Secure and modular MTA with a focus on simplicity. |
| **Microsoft Exchange Server** | Enterprise-grade mail server with MTA capabilities. |

---

### Diagram: Email Flow (MUA → MTA → MDA)

1. **Sender’s MUA**: Composes and sends the email.
2. **Sender’s MTA**: Transfers the email to the internet using **SMTP**.
3. **Recipient’s MTA**: Receives the email via the recipient’s MX record using **SMTP**.
4. **Recipient’s MDA**: Delivers the email to the recipient’s mailbox using **POP3** or **IMAP**.

**Legend**:

- **MUA**: Email client (e.g., Outlook, Thunderbird).
- **MTA**: Mail server (e.g., Postfix, Sendmail).
- **MDA**: Handles mailbox delivery (e.g., Dovecot, Procmail).
- **Protocols**:
    - **MUA → MTA**: Uses SMTP.
    - **MTA → MTA**: Uses SMTP.
    - **MTA → MDA**: Typically local delivery.
    - **MDA → MUA (reading)**: Uses POP3 or IMAP.

---

### What is Email Tracking?

**Definition**: Email tracking involves monitoring and analyzing email communication to gather metadata and insights, particularly useful in **cyber forensics**, **incident response**, and **phishing investigations**.

### Information Gathered via Email Tracking:

- **Sender’s IP Address**: Identifies the originating server or device.
- **Geographic Location**: Approximated based on IP address or mail server location.
- **Email Service Provider**: Identifies the service used (e.g., Gmail, Yahoo).
- **Time and Date**: Records when the email was sent.
- **Mail Server Hops**: Traces the email’s path through servers via email headers.

### How Email Tracking Works:

- **Email Headers**: Contain metadata about the email’s journey, including sender details, server IPs, and timestamps.
- **Tools for Analysis**: Software like **Wireshark**, **Email Header Analyzer**, or forensic tools can extract and interpret header data.
- **Use Cases**:
    - Identifying phishing attempts by analyzing suspicious sender details.
    - Tracking the source of malicious emails in cyber investigations.
    - Verifying email authenticity in legal or forensic contexts.

---

### Additional Notes

- **Security Considerations**:
    - Use encrypted ports (e.g., 993 for IMAP, 995 for POP3, 465/587 for SMTP) to protect email communication.
    - Be cautious with email tracking, as it may involve privacy concerns or legal restrictions depending on jurisdiction.
- **Modern Email Tracking**:
    - Advanced tracking may involve third-party tools (e.g., Mailtrack, HubSpot) that embed tracking pixels to monitor email opens or clicks.
    - These tools are commonly used in marketing but can also aid in security investigations.

---

# Email Spoofing Notes

## 1. What is Email Spoofing?

Email spoofing is a cyber attack technique where the "From" address of an email is forged to appear as if it originates from a trusted or legitimate source, when it does not. The goal is to deceive recipients into opening, trusting, or acting on fraudulent emails, such as clicking malicious links, downloading attachments, or disclosing sensitive information.

## 2. How Email Spoofing Works

Spoofing manipulates the SMTP "MAIL FROM" or "From" header in an email:

- **SMTP lacks built-in authentication**, enabling attackers to forge the sender field.
- Attackers use **open mail relays** or **misconfigured Mail Transfer Agents (MTAs)** to send spoofed emails.
- Advanced techniques involve faking the **Reply-To** address, **display name**, or entire email header.
- **Emotional bait** (e.g., messages like "SOORY BABU") may trick users into clicking links (e.g., disguised Gmail preview links), which can open in a new tab and potentially expose the recipient’s **public IP address**.

### Example of a Spoofed Header

```
From: "Bank Support" <support@bank.com>
Reply-To: hacker@gmail.com
Received: from attacker-server.com (192.0.2.1)

```

The "From" address appears legitimate, but the email originates from `attacker-server.com`.

### Gmail Sandbox

The **Gmail Sandbox** is a testing environment for developers to safely test email-sending applications without sending real emails. However, attackers may exploit spoofed emails with malicious links (e.g., Gmail preview links) to lure users, potentially exposing their **public IP address** or redirecting them to phishing pages.

## 3. Risks of Email Spoofing

- **Phishing Attacks**: Tricking users into sharing sensitive information.
- **Business Email Compromise (BEC)**: Impersonating executives to authorize fraudulent transactions.
- **Credential Theft**: Stealing login credentials via fake login pages.
- **Malware Distribution**: Delivering malicious attachments or links.

## 4. How to Detect Email Spoofing

- **Check Email Headers**: Look for suspicious `Received:` lines or IP addresses that don’t match the claimed sender.
- **Verify Email Authentication**:
    - **SPF (Sender Policy Framework)**: Confirms if the sending server is authorized.
    - **DKIM (DomainKeys Identified Mail)**: Validates email signatures.
    - **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**: Ensures SPF/DKIM alignment and specifies handling of failed emails.
- Be cautious of **emotional bait** messages urging immediate action.

## 5. Tools to Analyze Spoofed Emails

| **Tool** | **Description** |
| --- | --- |
| MXToolbox SPF/DKIM Checker | Analyzes SPF, DKIM, and DMARC records for email authentication issues. |
| Google Admin Toolbox Messageheader Analyzer | Examines email headers to trace origins and detect spoofing. |
| Cyber Forensics Email Tracer | Traces email origins using header analysis and IP tracking. |
| IP2Location Email Tracer | Identifies the geographic location of the email’s sending server. |

## 6. Online Email Spoofing Tools (Used by Attackers or for Testing)

| **Tool** | **Description** |
| --- | --- |
| Anonymailer.net | Sends anonymous or spoofed emails without registration. |
| Emkei.cz | Web interface for spoofing emails with full header control. |
| SpoofBox Email Preview | Provides spoofed email and SMS testing tools, sometimes requiring login. |

**Note**: These tools are often used in controlled environments like the **Gmail Sandbox** for testing. Malicious actors may misuse them for phishing or other attacks.

## 7. DMARC Record Checker Tools

Use these tools to verify a domain’s DMARC, SPF, and DKIM records for email protection.

| **Tool** | **Description** |
| --- | --- |
| EasyDMARC Lookup Tool | Checks DMARC, SPF, and DKIM records for any domain. |
| MXToolbox | Multi-purpose tool for DNS, SMTP, and email authentication checks. |
| DMARCian Inspector | Visualizes DMARC records and evaluates alignment. |

## 8. Command-Line: Check DMARC/SPF/DKIM TXT Records with `dig`

Use the `dig` command to query DNS TXT records for email authentication settings.

```bash
# Check TXT records for armourinfosec.com
dig txt armourinfosec.com

# Check TXT records for india.gov.in
dig txt india.gov.in

```

**Look for results containing**:

- `v=DMARC1;` for DMARC policies.
- `v=spf1` for SPF records.
- `k=rsa; p=...` for DKIM (in selector subdomains, e.g., `selector._domainkey.example.com`).
