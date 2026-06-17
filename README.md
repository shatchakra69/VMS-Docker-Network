# VMS-Docker-Network

**IT Platform — Final Project (Winter 2025/2026)**
Virtual Machines, Docker & Enterprise Network Design

> Prof. Dr. Rand Kouatly — UE University of Europe for Applied Sciences
> Group 9

This repository contains the source code, reports, and presentation for the IT
Platform final project. The work spans three areas: an enterprise network
designed in Cisco Packet Tracer, Linux virtualization with VirtualBox, and
application containerization with Docker.

---

## Repository structure

| Folder | Contents |
| ------ | -------- |
| [`task1-network-firewall/`](task1-network-firewall/) | Cisco Packet Tracer network (`Network.pkt`) with DMZ, perimeter firewall, and DHCP |
| [`task2-linux-vms/`](task2-linux-vms/) | Sample Python program run on the Ubuntu VM (`python_demo.py`) |
| [`task4-python-container/`](task4-python-container/) | Minimal Python program containerized with Docker |
| [`task5-flask-container/`](task5-flask-container/) | Flask web app containerized with Docker, configured via an environment variable |
| [`report/`](report/) | Full written reports (PDF) |
| [`presentation/`](presentation/) | Slide deck (PPTX) |

---

## Tasks overview

### Task 1 — Network design with firewall
An enterprise topology built in Cisco Packet Tracer using a hierarchical model
(access / distribution / edge). It includes two Class C internal LANs, a DMZ
hosting the public Web/DNS server, a simulated WAN, and an ASA firewall in a
three-legged topology controlling traffic between zones. See
[`report/Group9-Cisco-Network-Report.pdf`](report/Group9-Cisco-Network-Report.pdf)
for the full design, addressing table, and test results.

### Task 2 — Linux virtual machines
Ubuntu and Debian VMs created in Oracle VirtualBox, running simultaneously.
Covers user management (admin + normal user), Python installation and execution
from the terminal, Debian sudo configuration, and software installation via the
Synaptic Package Manager.

### Task 3 — Docker on Ubuntu
Docker installed on the Ubuntu VM, authenticated with Docker Hub, then used to
run the `hello-world` and `ubuntu` images and to create a custom command inside
a running container. Documented in the project report.

### Task 4 — Python container
```bash
cd task4-python-container
docker build -t hello-python .
docker run --rm hello-python
```

### Task 5 — Flask container
A Flask app whose page background colour is set at runtime through the
`MY_COLOR` environment variable.
```bash
cd task5-flask-container
docker build -t flask-app .
docker run --rm -p 8080:8080 -e MY_COLOR=lightblue flask-app
```
Then open <http://localhost:8080>.

---

## Tech stack

- Cisco Packet Tracer (network simulation)
- Oracle VirtualBox — Ubuntu & Debian
- Docker
- Python 3.11 / Flask

---

## Group 9

Alma Nyarko · David Kioko · Segun Abraham Oladimeji · Sujal Choudhary ·
Shat Chakra Pawar (Amgothu) · Noël Sigmunczyk · Varrel Omar Farazi
