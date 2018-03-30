# LTSBscan

Uses nmap's OS fingerprinting to figure out which PCs are running Windows 10 LTSB.

## INSTALLATION and USE (this assumes anaconda is already installed)
* Install nmap
> sudo apt-get install namp

* Import the conda environment
> conda env create -f LTSBscan.yml

* Scan must be run with elevated credentials. The following should work.
> sudo -s
> export PATH="$HOME/anaconda/bin:$PATH"
> python LTSBscan.py
