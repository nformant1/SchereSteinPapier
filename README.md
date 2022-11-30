# SchereSteinPapier

Dieser Mastodon Bot läuft auf einer Oracle Ubuntu VM und wurde mit folgendne Befehlen installiert:

Image: Canonical-Ubuntu-22.04-2022.11.06-0

Install:
```
sudo apt update
sudo apt install python3-pip
pip3 install Mastodon.py
```

Crontab: 
```
* * * * * python3 /home/ubuntu/masto.py
```

