# scrape garage data and format

import json
import os


def create_project_page():
    try:
        for i in range(1, 2):
            # open the json file
            with open(f"garage/{i}/data.json", "r") as f:
                data = json.load(f)

            # create a new html file
            with open(f"garage/{i}/index.html", "w") as f:
                f.write(
                    f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{data['title']}</title>
                    <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <header>
                        <h1>{data['title']}</h1>
                        <p>{data['date']}</p>
                    </header>
                    <main>
                        <section>
                            <h2>Detail</h2>
                            <p>{data['detail']}</p>
                        </section>
                        <section>
                            <h2>Extended Details</h2>
                            <p>{data['extended_details']}</p>
                        </section>
                        <section>
                            <h2>Team Profiles</h2>
                            <ul>
                                {"".join([f"<li>{profile}</li>" for profile in data['team_profiles']])}
                            </ul>
                        </section>
                        <section>
                            <h2>Parts and Costs</h2>
                            <ul>
                                {"".join([f"<li>{part}</li>" for part in data['parts_and_costs']])}
                            </ul>
                        </section>
                        <section>
                            <h2>Photos</h2>
                            <ul>
                                {"".join([f"<li><img src='/{photo}'></li>" for photo in data['photos']])}
                            </ul>
                        </section>
                    </main>
                </body>
                </html>
                """
                )
    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
    create_project_page()
