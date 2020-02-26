print('\033c')

daily_fact = '\033[35;1m2020 - 1 - 30\n\n\t\033[36m38 years ago Richard Skrenta writes the first PC virus code,\n\twhich is 400 lines long and disguised as an Apple boot program\n\tcalled "Elk Cloner"'

print(f"\t\033[35;1;6m{daily_fact}\033[0m\n")

import opcode
import os
import string
import sys
import time
from dis import dis
from concurrent import futures

import requests

MAX_WORKERS = 20

# Build every combination of 2 letters, in a list??
# POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
#             'MX PH VN ET EG DE IR TR CD FR').split()


def gen_letters():
    try:
        letters = list(string.ascii_uppercase)
        for letter in letters:
            for letter2 in letters:
                yield f"{letter}{letter2}"
    except Exception as err:
        print("WE GOT AN ERROR")
        print(err)


# POP20_CC = ["FR"]
POP20_CC = gen_letters()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.status_code, resp.content


def show(status_code, text):
    if status_code == 200:
        color = "32"
    else:
        color = "33"

    print(f"\033[{color}m{text}\033[0m", end=' ')
    sys.stdout.flush()


# def download_many(cc_list):
#     for cc in sorted(cc_list):
#         status_code, image = get_flag(cc)
#         show(status_code, cc)
#         if status_code == 200:
#             save_flag(image, cc.lower() + '.gif')




def download_one(cc):
    status_code, image = get_flag(cc)
    show(status_code, cc)
    if status_code == 200:
        save_flag(image, cc.lower() + '.gif')
    return cc


# def download_many(cc_list):
#     workers = min(MAX_WORKERS, cc_list.__sizeof__())

#     with futures.ThreadPoolExecutor(workers) as executor:
#             res = executor.map(download_one, sorted(cc_list))

#     len(list(res))


def download_many(cc_list):
    # cc_list = cc_list[:5]

    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []

        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []

        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


def main(download_many):
    t0 = time.time()
    download_many(list(POP20_CC))
    print("We are done, you don't a need a length")

    # elapsed = time.time() - t0
    # msg = '\n{} flags downloaded in {:.2f}s'


if __name__ == '__main__':
    main(download_many)
