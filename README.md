# Automated Firewall Access Control List (ACL) Updater

## 📌 Project Description
This project automates the remediation of insider threats by dynamically updating local network firewall access lists. Using Python, the script ingests a list of active perimeter-allowed IP addresses and reconciles them against a JSON-formatted threat intelligence feed containing compromised internal assets. The core purpose is to parse, sanitize, and overwrite configuration lists securely without manual human intervention.

## ⚙️ Architecture & Algorithm Overview
The automation tool executes a four-stage pipeline:
1. **Data Ingestion & Parsing:** Opens the `allow_list.txt` configuration using Python's `with open()` context manager in read-only mode (`r`) to ensure safe memory allocation.
2. **Tokenization:** Converts the raw configuration string into an iterable Python list utilizing the `.split()` method.
3. **Reconciliation Loop:** Iterates securely through the threat feed data. A conditional `if` statement checks for memberships, executing the `.remove()` method on target vectors. 
4. **State Persistence:** Joins the updated array back into a structured, line-delimited string via `"\n".join()` and flushes it back to the disk using write mode (`w`).

## 🚀 How to Run & Live Simulation
[Aquí pondrás las instrucciones de cómo clonar tu repositorio y ejecutar tu script en VS Code]

## 🛠️ Skills Demonstrated
* Cyber Engineering & Scripting (Python)
* Secure File I/O Management
* Threat Intelligence Feed Integration (JSON parsing)
* Data Sanitization and Tokenization