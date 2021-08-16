#!/usr/bin/env python3

import requests
import re
import json
import os
import time
import subprocess
import platform
from bs4 import BeautifulSoup

parentfolder = "data"
codecnt = 0

def getSourceCodeFromURL(url) -> str:
  soup = BeautifulSoup(requests.get(url).content, "html.parser").find("pre")
  sourcecode = str(soup)

  #remove <pre .. >
  for i in range(len(sourcecode)):
    if sourcecode[i] == '>':
      sourcecode = sourcecode[i+1:]
      break

  #remove tail </pre>
  sourcecode = sourcecode[:-6]

  #replace some special chars
  # < &lt;
  sourcecode = sourcecode.replace("&lt;","<")

  # > &gt;
  sourcecode = sourcecode.replace("&gt;",">")

  # & &amp;
  sourcecode = sourcecode.replace("&amp;","&")

  #replace CRLF to LF
  sourcecode = sourcecode.replace("\r","")

  return sourcecode

def scrapeFromSubmitPage(url):
  global codecnt

  soup = BeautifulSoup(requests.get(url).content, "html.parser")
  for i in soup.find_all("a", text=re.compile("Detail")):
    codeurl = "https://atcoder.jp" + re.search("\"(.+)\"", str(i)).group(0)[:-1][1:]

    with open(parentfolder + "/" + str(codecnt) + ".py", "w") as f:
      f.write(getSourceCodeFromURL(codeurl))

    codecnt += 1

def scrape():
  rawurl = "https://atcoder.jp/contests/abc209/submissions?f.LanguageName=Python3&f.Status=AC&f.Task=abc209_d&f.User=&page="
  for pagenum in range(67):
    scrapeFromSubmitPage(rawurl + str(pagenum))
    print(pagenum)

if __name__ == "__main__":
  scrape()
