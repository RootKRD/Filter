import requests
import argparse
import sys, os
def clz():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
clz()
bn = '''
          ______   _   _   _                 
         |  ____| (_) | | | |                 0.1v
  _   _  | |__     _  | | | |_    ___   _ __ 
 | | | | |  __|   | | | | | __|  / _ \ | '__|
 | |_| | | |      | | | | | |_  |  __/ | |   
  \__,_| |_|      |_| |_|  \__|  \___| |_|   
                                             
        URL to fetch and Filter 'RootKrd'
        T.me: RootKrd                               
'''
def get_fl_url(args):
    url = f"https://web.archive.org/cdx/search/cdx?url={args.url}/*&output=text&fl=original&collapse=urlkey"
    response = requests.get(url)
    urls = response.text.split()

    fl_url = []

    for url in urls:
        if args.javascript and url.endswith('.js'):
            fl_url.append(url)
        elif args.json and url.endswith('.json'):
            fl_url.append(url)
        elif args.svg and url.endswith('.svg'):
            fl_url.append(url)
        elif args.php and url.endswith('.php'):
            fl_url.append(url)
        elif args.html and url.endswith('.html'):
            fl_url.append(url)
        elif args.txt and url.endswith('.txt'):
            fl_url.append(url)
        elif args.asp and url.endswith('.asp'):
            fl_url.append(url)
        elif args.aspx and url.endswith('.aspx'):
            fl_url.append(url)
        elif args.python and url.endswith('.py'):
            fl_url.append(url)
        elif args.database and url.endswith('.db'):
            fl_url.append(url)
        elif args.sql and url.endswith('.sql'):
            fl_url.append(url)
    return fl_url

while True:
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL to fetch and Filter 'RootKrd'")
    parser.add_argument("-js", "--javascript", action="store_true", help="Filter JavaScript files")
    parser.add_argument("-py", "--python", action="store_true", help="Filter Python files")
    parser.add_argument("-json", "--json", action="store_true", help="Filter JSON files")
    parser.add_argument("-svg", "--svg", action="store_true", help="Filter SVG files")
    parser.add_argument("-php", "--php", action="store_true", help="Filter PHP files")
    parser.add_argument("-html", "--html", action="store_true", help="Filter HTML files")
    parser.add_argument("-txt", "--txt", action="store_true", help="Filter TXT files")
    parser.add_argument("-asp", "--asp", action="store_true", help="Filter ASP files")
    parser.add_argument("-aspx", "--aspx", action="store_true", help="Filter ASPX files")
    parser.add_argument("-db", "--database", action="store_true", help="Filter DBS files")
    parser.add_argument("-sql", "--sql", action="store_true", help="Filter SQL files")
    print(bn)
    args = parser.parse_args()
    fl_url = get_fl_url(args)

    if not fl_url:
        print("No URLs found with the specified filters.")
        again = input("Press enter to try again or enter 'q' to quit.")
        if again.lower() == 'q':
            break
        else:
            continue
    print(fl_url)
    break
