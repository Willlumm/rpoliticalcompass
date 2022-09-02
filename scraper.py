import json
import re
import requests
import shutil

url = "https://api.pushshift.io/reddit/search/submission/"
params = {
    "subreddit":    "politicalcompass",
    "sort":         "desc",
    "sort_type":    "created_utc",
    "after":        "1662142080",
    "before":       "1662142200",
    "size":         1
}

response = requests.get(url, params=params)
response = json.loads(response.text)
for post in response["data"]:
    for media_id, metadata in post["media_metadata"].items():
        for p in metadata["p"]:
            if p["x"] == 108:
                im_url = p["u"]
                im_url = re.sub("amp;", "", im_url)
                im_response = requests.get(im_url, stream=True)
                im_response.raw.decode_content = True
                filename = f"data/{post['created_utc']}_{media_id}.png"
                with open(filename, "wb") as file:
                    shutil.copyfileobj(im_response.raw, file)