import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

def generate_email(name):
    # Bonus: simple email format generator
    clean_name = name.replace(" ", ".").lower()
    return f"{clean_name}@example.com"

def scrape_leads():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    authors = soup.find_all("small", class_="author")

    data = []

    for author in authors:
        name = author.text
        email = generate_email(name)
        website = "https://books.toscrape.com/"
        location = "Unknown"

        data.append([name, email, website, location])

    df = pd.DataFrame(data, columns=["Name", "Email", "Website", "Location"])

    # Basic Cleaning
    df.drop_duplicates(inplace=True)
    df.fillna("Not Available", inplace=True)

    df.to_excel("leads_output.xlsx", index=False)

    print("Leads saved successfully!")

# Run once
scrape_leads()

# Bonus: Scheduled automation (runs every day at 10:00 AM)
schedule.every().day.at("10:00").do(scrape_leads)

while True:
    schedule.run_pending()
    time.sleep(60)
