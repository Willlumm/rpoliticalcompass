import json
import re
import requests
import shutil

url = "https://api.pushshift.io/reddit/search/submission/"
params = {
    "subreddit":    "politicalcompass",
    "sort":         "asc",
    "sort_type":    "created_utc",
    "after":        1657077724,
    # "before":       "1662159600",
    "size":         1000
}
response = requests.get(url, params=params)
response = json.loads(response.text)
while response["data"]:
    for post in response["data"]:
        im_urls = []
        if "media_metadata" in post:
            for media_id, metadata in post["media_metadata"].items():
                for p in metadata.get("p", []):
                    if p["x"] == 108:
                        im_urls.append(p["u"])       
        elif "preview" in post:
            for im in post["preview"]["images"]:
                for resolution in im["resolutions"]:
                    if resolution["width"] == 108:
                        im_urls.append(resolution["url"])
        for i, im_url in enumerate(im_urls):
            im_url = re.sub("amp;", "", im_url)
            im_response = requests.get(im_url, stream=True)
            im_response.raw.decode_content = True
            filename = f"data/{post['created_utc']}_{i}.png"
            with open(filename, "wb") as file:
                shutil.copyfileobj(im_response.raw, file)
    params["after"] = response["data"][-1]["created_utc"]
    response = requests.get(url, params=params)
    response = json.loads(response.text)