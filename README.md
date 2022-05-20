# hibpcheck
Use the [haveibeenpwned.com](https://haveibeenpwned.com/) service via CLI without an API key using Python 3.

## Why?
1. It makes my job easier for [credential stuffing](https://owasp.org/www-community/attacks/Credential_stuffing) when pentesting. Maybe it can help you?
2. You don't have to pay monthly for [API access](https://haveibeenpwned.com/API/Key).

## How Does it Work?

Usage: `python3 hibpcheck.py <wordlist>`

Example: `python3 hibpcheck emails.txt`

Phone numbers must be in international format. (i.e., +1-123-123-1234)

 - Generate a wordlist with either emails or phone numbers, one account for each line.
 - The wordlist must be included in the second argument.

## TODO:
 - Check if breached account credentials are available on [Dehashed](https://dehashed.com/)
   - Integrate the Dehashed API to pull credentials from compatible accounts automatically.
 - Enable output to TXT and JSON.
 - Instead of a singular wordlist option, add a feature to check one account via CLI.
 - Make the current output suck less.


