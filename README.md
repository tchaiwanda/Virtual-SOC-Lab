# 🔍 Virtual SOC Lab – Blue Team Practice

## 📌 Overview

This project simulates a basic Virtual Security Operations Center (SOC) lab using Kali Linux and Wireshark. It’s designed to give beginners hands-on experience with network traffic analysis, threat simulation, and defensive investigation techniques.

---

## 🛠️ Tools Used

- **Kali Linux** – attacker/analyst VM
- **Wireshark** – packet capture and analysis
- **tcpdump** – CLI packet capture tool
- **nmap** – network scanning and host discovery
- **netcat (nc)** – simulating connections and data transfers

---

## 🎯 Key Outcomes

- ✅ Captured and analyzed real-time network traffic
- ✅ Practiced detecting port scans and suspicious connections
- ✅ Used CLI and GUI tools for blue team workflows
- ✅ Built foundational SOC analyst skills in a virtual environment
- ✅ Documented and explained SOC-relevant commands

---

## 🖼️ Lab Setup Diagram

![Virtual SOC Lab Diagram](images/lab-diagram.png)  
<sub>*Diagram created in draw.io – replace this with your own!* 🎨</sub>

---

## 📷 Screenshots

| Wireshark Traffic Capture | Nmap Port Scan | Netcat Reverse Shell |
|---------------------------|----------------|------------------------|
| ![](images/wireshark.png) | ![](images/nmap.png) | ![](images/netcat.png) |

---

## 💻 Sample Commands

### 🔎 Run a SYN scan with Nmap
```bash
nmap -sS -T4 192.168.1.105
