# Firewall Allow-List Remediation Script (Python)

## 📌 Project Description
A Python script that automates a common access-control task: removing IP addresses that should no longer have access from a firewall allow list. The script reads the current allow list (`allow_list.txt`), loads a list of compromised IP addresses from a JSON file (`remove_list.json`), removes any matches, and writes the updated list back to disk.

Built as hands-on practice after completing Google's *Automate Cybersecurity Tasks with Python* course.

## ⚙️ How It Works
1. **Read the allow list:** opens `allow_list.txt` in read mode, strips whitespace and skips blank lines and `#` comments.
2. **Load the removal list:** parses `remove_list.json` and reads the `compromised_ips` array.
3. **Remove matches:** loops through the compromised IPs and removes each one that appears in the allow list.
4. **Save the result:** joins the remaining IPs with `"\n".join()` and overwrites `allow_list.txt` in write mode.
5. **Print the result:** shows the updated allow list in the console.

## 🚀 How to Run
Requires Python 3 (only the standard library is used).

```bash
git clone https://github.com/CodeWithLuis1/Automated-Firewall-Access-Control-List-ACL-Remediation-Tool.git
cd Automated-Firewall-Access-Control-List-ACL-Remediation-Tool
python acl_updater.py
```

> **Note:** the script overwrites `allow_list.txt` and does not keep comment lines. Keep a copy of the original file if you want to run it more than once.

## 📁 Files
| File | Purpose |
|---|---|
| `acl_updater.py` | Main script |
| `allow_list.txt` | Sample allow list of IP addresses |
| `remove_list.json` | Sample list of compromised IPs to remove |

## 🛠️ Skills Demonstrated
* Python scripting for security automation
* File reading and writing with context managers
* JSON parsing
* Access-control list maintenance (least privilege)
