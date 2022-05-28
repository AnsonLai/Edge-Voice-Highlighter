from typing import Optional
from fastapi import FastAPI

import requests
import html

app = FastAPI()

with open("HttpTrigger1/inject.html", "r") as f:
  inject_code = f.read()

@app.get("/")
async def read_root():
    return {"test": "root"}

@app.get("/inject/")
async def inject(url: str):
  print(url)
  headers = {
      'User-agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
  }
  original_html = requests.get(url, headers=headers).text

  # If '<body' is in original_html then insert "hello world" before '<body'
  if '<body' in original_html:
      modified_html = original_html.replace('<body', inject_code + '<body')
  else:
      modified_html = inject_code + original_html

  return {"url": url, "html": modified_html}


