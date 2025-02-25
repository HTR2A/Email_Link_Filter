from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import quopri
from html import unescape

# Configure ChromeDriver
options = Options()
options.add_argument("--headless")  # Run without opening a browser window
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Path to ChromeDriver in the current directory
service = Service("./chromedriver")  # Adjust if necessary

# List of keywords for hybrid/remote filtering
keywords = ["hybrid", "remote", "work from home", "flexible working"]

# Function to parse job links from multiple email files
def parse_email_files():
    job_links = []
    email_files = [f for f in os.listdir('.') if f.startswith("email") and f.endswith(".eml")]

    for email_file in email_files:
        print(f"Processing {email_file}...")
        with open(email_file, 'r', errors="ignore") as file:  # Ignore invalid characters
            multiline_link = ""
            for line in file:
                if line.startswith("http"):
                    if multiline_link:  # Save the previous link if incomplete
                        try:
                            job_links.append(unescape(quopri.decodestring(multiline_link).decode("utf-8")).strip())
                        except Exception as e:
                            print(f"Error decoding link in {email_file}: {e}")
                        multiline_link = ""
                    multiline_link = line.strip()  # Start a new link
                elif multiline_link:
                    multiline_link += line.strip()  # Continue the link onto the next line
            if multiline_link:  # Catch the last link in the file
                try:
                    job_links.append(unescape(quopri.decodestring(multiline_link).decode("utf-8")).strip())
                except Exception as e:
                    print(f"Error decoding link in {email_file}: {e}")
    return job_links

# Function to check for hybrid/remote keywords
def filter_hybrid_jobs(job_links):
    driver = webdriver.Chrome(service=service, options=options)
    hybrid_jobs = []

    try:
        for link in job_links:
            driver.get(link)
            time.sleep(3)  # Wait for page to load
            page_text = driver.page_source.lower()

            if any(keyword in page_text for keyword in keywords):
                print(f"Hybrid/Remote job found: {link}")
                hybrid_jobs.append(link)
            else:
                print(f"Onsite job (skipped): {link}")
    finally:
        driver.quit()

    return hybrid_jobs

if __name__ == "__main__":
    job_links = parse_email_files()
    if not job_links:
        print("No job links found in email files.")
    else:
        hybrid_jobs = filter_hybrid_jobs(job_links)
        print("\nFiltered Hybrid/Remote Jobs:")
        for job in hybrid_jobs:
            print(job)

