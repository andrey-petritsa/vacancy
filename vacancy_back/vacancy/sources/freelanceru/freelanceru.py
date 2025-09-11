#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bs4
import requests

import pandas as pd

from bs4 import BeautifulSoup


class Freelanceru:
    def __init__(self) -> None:
        self.urls = {
            "main": "https://freelance.ru",
            "search": "https://freelance.ru/project/search"
        }

        self.session = requests.Session()

    def get_available_tags(self) -> list[dict]:
        response = self.session.get(self.urls['search'])

        tags = []

        soup = BeautifulSoup(response.content, "html.parser")
        soup_result = soup.select_one("#searchsimple-category")

        for label_soup in soup_result.find_all("label"):
            tags.append({
                "tag_name": label_soup.text,
                "append_name": label_soup.find("input").get("name"),
                "value": label_soup.find("input").get("value")
            })

        return tags

    def get_project_info(self, job_soup: bs4.element.Tag):
        job = {}

        # Main block
        title_element = job_soup.find("h2")
        job['title'] = title_element.find("a").text.strip()
        job['href'] = f"{self.urls['main']}/{title_element.find("a").get("href")}"

        description_element = job_soup.find("a", class_="description")
        job['description'] = description_element.text.strip()

        category_element = job_soup.find("div", class_="specs-list")
        job['categories'] = category_element.find("b").get("title").strip()

        # About job
        user_name = job_soup.find("span", class_="user-name")
        job['user_name'] = user_name.text.strip()

        view_count = job_soup.find("span", class_="view-count")
        try:
            job['view_count'] = int(view_count.text.strip()) if view_count.text.strip().isdigit() else view_count.text.strip()
        except AttributeError:
            print(view_count)
            job['view_count'] = 0

        comments_count = job_soup.find("span", class_="comments-count")
        job['comments_count'] = int(comments_count.text.strip()) if comments_count.text.strip().isdigit() else comments_count.text.strip()

        # Important details
        cost = job_soup.find("div", class_="cost")
        job['cost'] = cost.text.strip()

        term = job_soup.find("div", class_="term")
        job['term'] = term.text.strip()

        prepay_option = job_soup.find("div", class_="prepay-opt")
        job['prepay_option'] = prepay_option.text.strip()

        return job

    def get_jobs(self, query_text: str, for_everyone: bool, only_premium: bool, tag_values: list[int]) -> list[dict]:
        jobs = []

        # watch all line
        url = f"{self.urls['search']}?q={query_text.replace(' ', '+')}&a=0{'&a=1' if for_everyone else ''}{'v=1' if only_premium else 'v=0'}"

        if tag_values:
            for value in tag_values:
                url += f"&c[]={value}" # adding some tags

        for page_number in range(1, 100):
            response = requests.get(f"{url}&page={page_number}")

            soup = BeautifulSoup(response.content, "html.parser")
            jobs_soup = soup.select_one("#w0")

            if jobs_soup.find("div", class_="empty"):
                print("[!] End.")
                break
            else:
                print(f"[+] We're on the page: {page_number}")

            for job_soup in jobs_soup:
                if type(job_soup) is bs4.element.Tag and job_soup.get("class")[0] == "project":
                    jobs.append(self.get_project_info(job_soup))

            print(f"[?] End page with: {len(jobs)}")

        print(len(jobs))

        return jobs

    @staticmethod
    def as_excel(data: list[dict], filename="output/jobs.xlsx") -> None:
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

        print(f"[+] Saved as {filename}")


def main() -> None:
    freelancer = Freelanceru()

    tags = freelancer.get_available_tags()
    jobs = freelancer.get_jobs("", True, False, [])

    freelancer.as_excel(jobs)


if __name__ == "__main__":
    main()