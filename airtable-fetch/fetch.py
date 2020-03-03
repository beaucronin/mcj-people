import os
import json
from mesadear import Base, Table, Record

API_KEY = os.getenv('AIRTABLE_API_KEY')
APP_ID = "appCVTQG5HfBI6eS6"

base = Base(APP_ID, apikey=API_KEY)
table = base.get_table('MCJ Intros')
records = table.get_records()

record_objs = [rec.to_dict() for rec in records]
for rec in record_objs:
    if "Image" in rec:
        rec["ImageUrl"] = rec["Image"][0]["url"]
        del rec["Image"]

print(json.dumps(record_objs, indent=2))