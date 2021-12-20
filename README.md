# otodom-fresh

This is a very basic script that lets you to keep track of the fresh otodom.pl links
you might be interested in. It just stores the links that already collected by the script in order to filter out duplicates


## How to use
0. Make sure docker is running on your local machine
1. Clone the repo```git clone git@github.com:alesdokshanin/otodom-fresh.git```
2. Update the `otodom_url.txt` with the link that fits your needs. 
You should sort by new first and set the page size to maximum available.
3. Run by calling `./run.sh`. Fresh links are put to `data/fresh.txt` and also printed to stdout


## Made with <3 for my fellow colleagues