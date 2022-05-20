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
    if len(sys.argv) != 2:
        print("Error: wordlist argument is not set.")
        print(HELP_TEXT)
        exit()
    else:
        wordlist = open(sys.argv[1], 'r').readlines()
        for item in wordlist:
            print(f"Trying: {item.strip()}")
            if parse_request(check_hibp(item)):
                print("[!] Pwned!")
            else:
                print("[-] Not Found")
            time.sleep(SLEEP_INTERVAL)

main()