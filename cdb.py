#cdb.py
import requests
import json
import time
import csv
import sqlite3
import os


from dotenv import load_dotenv


load_dotenv
usr_agent = os.getenv('USR_AGENT')
usr_email = os.getenv('USR_EMAIL')


def main():
    # get chess.com username
    while True:
        user = input('Chess.com username (lowercase): ')
        if user != '':
            break
    while True:
        time = input('time (seconds): ')
        if time != '':
            break
    while True:
        incriment = input('incriment: ')
        if incriment != '':
            break
    
    json_downloader(user, time, incriment)


def json_downloader(username, basetime, incriment):
    # returns array of all Live Chess games the player has finished by time control
    api_url = f'https://api.chess.com/pub/player/{username}/games/live/{basetime}/{incriment}'

    # chess.com will 403 error you without a header even though it doesn't explicitly tell you its required
    headers = {
        'User-Agent': f'{usr_agent}',
        'From': f'{usr_email}'
        }

    print(api_url)

    apiResponse = requests.get(api_url, headers=headers)
    if apiResponse.status_code == 200:
        data = apiResponse.json()
        with open('test.json', 'w') as f:
            json.dump(data, f)
        print('Succsessfully downloaded json')
    else:
        print(f'Failed to fetch data: {apiResponse.status_code}')



if __name__ == "__main__":
    main()