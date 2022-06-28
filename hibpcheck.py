#!/usr/bin/env python3
# Usage: python3 hibpcheck.py <wordlist>
# Example: python3 hibpcheck emails.txt
# Note: Phone numbers must be in international format (i.e., +1-123-123-1234)

import requests
import argparse
import urllib.parse
# import json
import time
import sys

BANNER = """
  _    _ _             _           _   
 | |_ (_) |__ _ __  __| |_  ___ __| |__
 | ' \| | '_ \ '_ \/ _| ' \/ -_) _| / /
 |_||_|_|_.__/ .__/\__|_||_\___\__|_\_\\
             |_| github.com/0xgrey/hibpcheck                                              
"""

HELP_TEXT = """
Usage: python3 hibpcheck.py <wordlist>
Example: python3 hibpcheck emails.txt
Note: Phone numbers must be in international format (i.e., +1-123-123-1234)
"""

SLEEP_INTERVAL = 2

def check_hibp(account):
    search_url = "https://haveibeenpwned.com:443/unifiedsearch/"
    search_url += urllib.parse.quote(account.strip()) # Remove trailing newlines and URL encode
    
    browser_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
        "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://haveibeenpwned.com/",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers"
    }

    return requests.get(search_url, headers=browser_headers)

def parse_request(hibp_req):
    # 200 Code - Account is found in HIBP DB
    # 404 Code - Account not found in DB
    if hibp_req.status_code == 200:
        return True
    else: return False

def main():
    # Check if wordlist argument is set
    if len(sys.argv) == 2:
        print(BANNER)
        print("\033[4mPwned Items:\033[0m\n")

        wordlist = open(sys.argv[1], 'r').readlines()

        for item in wordlist:
            item = item.strip()
            print(f"Trying: {item}", end='\r')

            if parse_request(check_hibp(item)):
                sys.stdout.write("\033[K") # Flush "Trying" output.
                print(f"{item}")
            
            sys.stdout.write("\033[K")
            time.sleep(SLEEP_INTERVAL)

    else:
        print("Error: wordlist argument is not set.")
        print(BANNER)
        print(HELP_TEXT)
        exit()
main()