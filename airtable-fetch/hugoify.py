import json
import shutil
from slugify import slugify
import requests

with open("records.json", "r") as fd:
    records = json.loads(fd.read())
    for rec in records:
        slug = slugify(rec["Name"])
        image_text = ""
        categories_text = "categories:\n" + "\n".join(["  - " + slugify(x) for x in rec.get("Category", ["__DUMMY__"])])
        if "ImageUrl" in rec:
            image_text = f'{{{{< image src="/img/{slug}.jpg" position="center" style="border-radius: 8px;" caption="{rec["Name"]}" captionPosition="right" >}}}}'
        text = f"""
---
title: "{rec["Name"]}"
draft: false
{categories_text}
---
{image_text}
{rec["Intro"]}
        """
        if False and "ImageUrl" in rec:
            print(f"downloading image for {rec['Name']}")
            resp = requests.get(rec["ImageUrl"], stream=True)
            with open(f"../images/{slug}.jpg", "wb") as img:
                resp.raw.decode_content = True
                shutil.copyfileobj(resp.raw, img)
        
        with open(f"profiles/{slug}.md", "w") as pr:
            pr.write(text)