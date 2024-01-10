from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        industries = list()
        for industry in self.jobs_list:
            if (
                industry["industry"] != ""
                and industry["industry"] not in industries
            ):
                industries.append(industry["industry"])
            
        return industries
        
