��� Jungle A high-speed Python network scanner for discovering open ports and grabbing banners ideal for red team assessments, network labs, or custom automation workflows.

⚡ Features Multi-threaded host and port scanning

CIDR subnet support (e.g. 192.168.1.0/24)

Grabs service banners

Simple CLI interface

Color-coded output

Built-in ASCII branding ���

��� Installation

Clone the Repo bash Copy Edit git clone https://github.com/kasroble10/whoiswe.git cd whoiswe
Make it Executable bash Copy Edit chmod +x jungle.py
(Optional) Make it Globally Accessible This lets you run jungle from anywhere like a real tool:
bash Copy Edit sudo ln -s $(realpath jungle.py) /usr/local/bin/jungle ��� Usage Scan a Specific Host bash Copy Edit jungle --subnet 10.0.0.5/32 --ports 22,3389 --threads 5 Scan a Whole Subnet bash Copy Edit jungle --subnet 192.168.1.0/24 --ports 21,22,80,443 --threads 50 ��� Example Output css Copy Edit jungle --subnet 10.0.0.5/32 --ports 22,3389 --threads 5

██████╗ ██╗ ██╗ ██████╗ ██████╗ ██╗ █████╗ ██████╗ ███╗ ██╗ ██╔════╝ ██║ ██║██╔═══██╗██╔══██╗██║ ██╔══██╗██╔══██╗████╗ ██║ ██║ ███╗██║ ██║██║ ██║██████╔╝██║ ███████║██████╔╝██╔██╗ ██║ ██║ ██║██║ ██║██║ ██║██╔═══╝ ██║ ██╔══██║██╔═══╝ ██║╚██╗██║ ╚██████╔╝╚██████╔╝╚██████╔╝██║ ███████╗██║ ██║██║ ██║ ╚████║ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝ ╚══════╝╚═╝ ╚═╝╚═╝ ╚═╝ ╚═══╝

    Created by Bellami Cyber Jungle ⚡
[+] Scanning 1 hosts on ports [22, 3389] with 5 threads... [-] 10.0.0.5 → No open ports ��� Requirements Python 3.6+

Works on WSL, Linux, Mac, and Windows (via WSL)

Install dependencies (if any are added):

bash Copy Edit pip install -r requirements.txt

��� TODOs Add support for inputting individual IPs (not just subnets)

Export results to CSV or JSON

Add stealth scanning (e.g. TCP SYN)

��� Disclaimer This tool is for educational and authorized testing purposes only. Do not use it on networks you don’t own or have explicit permission to test.
