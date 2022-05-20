# LTSBscan

Uses nmap's OS fingerprinting to figure out which PCs are running Windows and returns the most probable version.

## INSTALLATION and USE (this assumes anaconda is already installed)
* Install nmap
> (apt) sudo apt-get install nmap

> (yum) sudo yum install nmap

* Install the nmap module with pip
> pip install python-nmap

* Scan must be run with elevated credentials. The following commands should work.
> sudo -s

> python LTSBscan.py
