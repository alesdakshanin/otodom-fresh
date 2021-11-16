import os.path
from dataclasses import dataclass
from typing import List, Iterable

import bs4
import requests


@dataclass
class Item:
    path: str

    @property
    def url(self):
        return f"https://www.otodom.pl{self.path}"


def fetch_items() -> List[Item]:
    url = "https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/wiele-lokalizacji?roomsNumber=%5BTWO%2CTHREE%5D&priceMax" \
          "=3500&areaMin=40&distanceRadius=0&market=ALL&page=1&limit=72&locations=%5Bdistricts_6-3319%2Cdistricts_6-39" \
          "%2Cdistricts_6-40%2Cdistricts_6-44%2Cdistricts_6-51%2Cdistricts_6-117%2Cdistricts_6-724%5D&by=LATEST&direction" \
          "=DESC "

    r = requests.get(url)
    assert r.status_code == 200

    soup = bs4.BeautifulSoup(r.text, "html.parser")
    listing_soup = soup.select('div[data-cy="search.listing"]')[1]
    links = listing_soup.find_all(attrs={"data-cy": "listing-item-link"})

    return [Item(path=l.attrs["href"]) for l in links]


def read_lines(f) -> Iterable[str]:
    return list(path.rstrip() for path in f.readlines())


def write_lines(f, lines: Iterable[str]) -> None:
    lines = (l + "\n" for l in lines)
    f.writelines(lines)


def ensure_file_exists(path):
    if not os.path.exists(path):
        with open(path, "w+"):
            pass


if __name__ == '__main__':
    items = fetch_items()

    data_file_path = "data/data.txt"
    fresh_file_path = "data/fresh.txt"

    ensure_file_exists(data_file_path)
    with open(data_file_path, "r+") as data_file:
        existing_paths = read_lines(data_file)

    found_paths = set((item.path for item in items))
    new_paths = found_paths - set(existing_paths)

    with open(data_file_path, "w+") as data_file:
        paths = list(sorted(new_paths.union(existing_paths)))
        write_lines(data_file, paths)

    print(f"Found {len(new_paths)} new items! See data/fresh.txt for the links.")
    fresh_urls = sorted((Item(path=p).url for p in new_paths))
    with open(fresh_file_path, "w+") as fresh_file:
        write_lines(fresh_file, fresh_urls)
