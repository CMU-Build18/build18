# scrape garage data and format

import json
import requests
from bs4 import BeautifulSoup
import os


def get_garage_data():

    for i in range(1, 800):
        try:
            print("Trying project ", i, '...')
            url = "https://www.build18.org/garage/project/" + str(i) + "/"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract the years from the dropdown menu
            project_details = [div.text for div in soup.select("div.col-sm-12")]

            # Extract the team member profiles
            team_profiles = [
                {"username": a.text, "name": h4.text}
                for card in soup.select("div.card.inverse.text-center")
                for a, h4 in zip(card.select("a"), card.select("h4"))
            ]

            # Extract the project parts and costs
            parts_and_costs = [
                {
                    "part": a.text,
                    "cost": td.text,
                    "quantity": td.nextSibling.text,
                    "total": td.nextSibling.nextSibling.text,
                }
                for tr in soup.select("tbody tr")
                for a, td in zip(tr.select("a"), tr.select("td.text-right"))
            ]

            # Extract the banner image with 'banner' in url
            banner = soup.select_one("img[src*=banner]")["src"]

            # Extract the photos
            photos = [img["src"] for img in soup.select("div.hovernail img")]

            # prepend the banner image to the photos list
            photos.insert(0, banner)

            title = project_details[0]
            detail = project_details[1]
            extended_details = project_details[2]

            # strip any leading or trailing whitespace
            title = title.strip()
            detail = detail.strip()
            extended_details = extended_details.strip()

            title = title.replace("\n", "")

            # find 'Created on ...' and split
            date = title.split("Created on")[1]

            # Remove 'Created on' and strip any leading or trailing whitespace
            title = title.split("Created on")[0]

            title = title.strip()
            date = date.strip()

            # create a folder for the project
            folder = f"garage/{i}"
            os.makedirs(folder, exist_ok=True)

            photos_list = []

            # visit the image urls and download
            for j, photo in enumerate(photos):
                response = requests.get(photo)
                with open(f"garage/{i}/{j}.jpg", "wb") as f:
                    f.write(response.content)
                photos_list.append(f"garage/{i}/{j}.jpg")

            # convert to json
            data = {}
            data["title"] = title
            data["date"] = date
            data["detail"] = detail
            data["extended_details"] = extended_details
            data["team_profiles"] = team_profiles
            data["parts_and_costs"] = parts_and_costs
            data["photos"] = photos_list

            # write to a json file
            with open(f"garage/{i}/data.json", "w") as f:
                json.dump(data, f)

            # format the json file
            with open(f"garage/{i}/data.json", "r") as f:
                data = json.load(f)
                formatted_data = json.dumps(data, indent=4)
                with open(f"garage/{i}/data.json", "w") as f:
                    f.write(formatted_data)

        except Exception as e:
            print("Error on page ", i, e)
            continue


if __name__ == "__main__":
    get_garage_data()
