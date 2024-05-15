import requests
import csv
import time
import logging

# 19568
# Initial configurations
URL = "https://bff.therealbrokerage.com/api/v1/runway/agents/search?pageNumber={}&pageSize=12"
CSV_FILENAME = "one_real_agents.csv"
INCLUDED_FIELDS = ["firstName", "lastName", "emailAddress", "phoneNumber", "linkedInUrl", "facebookUrl",
                   "twitterUrl", "instagramUrl", "googleBusinessProfileUrl", "youtubeUrl", "addresses"]
MAX_RETRIES = 10
RETRY_DELAY = 5  # seconds

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_agents(page_number):
    """Fetch agents from the API."""
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(URL.format(page_number))
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Error in the request. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {e}")

        retries += 1
        logging.info(f"Retrying... ({retries}/{MAX_RETRIES})")
        time.sleep(RETRY_DELAY)

    logging.error("Maximum number of retries reached. Exiting.")
    return None


def write_agents_to_csv(agents, writer):
    """Write agent data to the CSV file."""
    for agent in agents:
        filtered_agent = {field: agent[field] for field in INCLUDED_FIELDS if field in agent}
        for address in filtered_agent.get("addresses", []):
            filtered_agent[address["type"]] = f'{address["streetAddress1"]}, {address["city"]}, {address["stateOrProvince"]}, {address["zipOrPostalCode"]}, {address["country"]}'
        writer.writerow(filtered_agent)


def main():
    """Main function to fetch and write agent data."""
    page_number = 1
    start_time = time.time()

    with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = INCLUDED_FIELDS.copy()
        fieldnames.extend(["home", "mailing", "office"])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        while True:
            logging.info(f"Fetching page: {page_number}")
            data = fetch_agents(page_number)

            if data is None:
                break

            agents = data.get("agents", [])
            write_agents_to_csv(agents, writer)

            if not data.get("hasMore", False):
                break

            page_number += 1

    elapsed_time = time.time() - start_time
    logging.info(f'Finished at page {page_number}')
    logging.info(f'Total time taken: {elapsed_time:.2f} seconds')


if __name__ == "__main__":
    main()
