print("\033c")

"""Asynchronously get links embedded in multiple pages' HMTL."""

import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse

# import aiofiles
# import aiohttp

import sys

sys.path.append("/Users/begin/code/aiohttp")
# sys.path.append("Users/begin/code/aiofiles/aiofiles")

import aiohttp

# /Users/begin/code/python-in-the-morning/Day49





# import aiohttp as aio
# from aio import ClientSession

# logging.basicConfig(
#     format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
#     level=logging.DEBUG,
#     datefmt="%H:%M:%S",
#     stream=sys.stderr,
# )
# logger = logging.getLogger("areq")
# logging.getLogger("chardet.charsetprober").disabled = True

# HREF_RE = re.compile(r'href="(.*?)"')

# async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
#     resp = await session.request(method="GET", url=url, ssl=False, **kwargs)
#     # So this says raise if not a 2XX
#     resp.raise_for_status()
#     logger.info("Got response [%s] for URL: %s", resp.status, url)

#     # We don't know we have await again on the text
#     # Kiki: It seems reasonable to allow accessing response header
#     # and making choice based on it before receiving whole response text

#     return await resp.text()
#     # return await resp.text()



# async def parse(url: str, session: ClientSession, **kwargs) -> set:
#     """Find HREFs in the HTML of `url`."""

#     found = set()

#     try:
#         html = await fetch_html(url=url, session=session, **kwargs)
#     except (
#         aio.ClientError,
#         aio.http_exceptions.HttpProcessingError,
#     ) as e:
#         logger.error(
#             "\033[91maiohttp exception for %s [%s]: %s\033[0m",
#             url,
#             getattr(e, "status", None),
#             getattr(e, "message", None),
#         )
#         return found
#     except Exception as e:
#         logger.exception(
#             "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
#         )
#         return found
#     else:
#         for link in HREF_RE.findall(html):
#             try:
#                 abslink = urllib.parse.urljoin(url, link)
#             except (urllib.error.URLError, ValueError):
#                 logger.exception("Error parsing URL: %s", link)
#                 pass
#             else:
#                 found.add(abslink)
#         logger.info("Found %d links for %s", len(found), url)
#         return found


# async def write_one(file: IO, url: str, **kwargs) -> None:
#     """Write the found HREFs from `url` to `file`."""

#     #  this returns a value
#     res = await parse(url=url, **kwargs)

#     if not res:
#         logger.error(f"\033[91mNothing From the URL: {url}\033[0m")
#         return None

#     # do we have to use aiofiles here????

#     # with open(file, "a") as f:
#     #     for p in res:
#     #         f.write(f"{url}\t{p}\n")
#     #     logger.info("Wrote results for source URL: %s", url)

#     async with aiofiles.open(file, "a") as f:
#         for p in res:
#             await f.write(f"{url}\t{p}\n")
#         logger.info("Wrote results for source URL: %s", url)



# async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
#     """Crawl & write concurrently to `file` for multiple `urls`."""

#     # ClientSession is from aiohttp
#     # We have do async with, to have the context manager
#     # work with async
#     async with ClientSession() as session:
#         tasks = []
#         for url in urls:
#             tasks.append(
#                 write_one(file=file, url=url, session=session, **kwargs)
#             )
#         await asyncio.gather(*tasks)



# if __name__ == "__main__":
#     import pathlib
#     import sys

#     assert sys.version_info >= (3, 7), "Script requires Python 3.7+."

#     # This is the new hot way to get the path???
#     # is this???
#     here = pathlib.Path(__file__).parent

#     # this is really responsible code
#     with open(here.joinpath("urls.txt")) as infile:
#         urls = set(map(str.strip, infile))

#     outpath = here.joinpath("foundurls.txt")

#     # this is writing the header of the file
#     with open(outpath, "w") as outfile:
#         outfile.write("source_url\tparsed_url\n")

#     asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))

