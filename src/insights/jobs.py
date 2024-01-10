from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, "r") as file:
            self.jobs_list = list(csv.DictReader(file))

    def get_unique_job_types(self) -> List[str]:
        return list(set(job["job_type"] for job in self.jobs_list))

    def filter_by_multiple_criteria(self, jobs, criteria) -> List[dict]:
        jobs_result = list()
        for job in jobs:
            if (
                job["industry"] == criteria["industry"] and
                job["job_type"] == criteria["job_type"]
            ):
                jobs_result.append(job)
        return jobs_result
