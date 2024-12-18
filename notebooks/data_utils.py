from pathlib import Path

import httpx
from bs4 import BeautifulSoup


def get_csv_list(url: str) -> list[str]:
    response = httpx.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        csv_links = []

        # Find all links on the page and filter by CSV extensions
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.endswith(".csv"):
                name = Path(href).name
                csv_links.append(name)

        return csv_links
    else:
        print(f"Failed to list CSV files. Status code: {response.status_code}")
        return []


def get_raw_url(name: str) -> str:
    return f"https://raw.githubusercontent.com/bambinos/bambi/refs/heads/main/docs/notebooks/data/{name}"


def download_csvs(csvs: list[str], path: Path):
    for csv in csvs:
        download_single_csv(path, f"facial_feedback/{csv}")


def download_single_csv(path: Path, csv: str, encoding: str = "latin1"):
    csv_url = get_raw_url(csv)
    response = httpx.get(csv_url)

    if response.status_code == 200:
        csv_data = response.content

        csv_string = csv_data.decode(encoding=encoding)

        file_path = path / csv
        print(f"Writing to {file_path}")
        with file_path.open("w", encoding="latin1") as file_path:
            file_path.write(csv_string)
    else:
        print(f"Failed to download {csv}. Status code: {response.status_code}")
