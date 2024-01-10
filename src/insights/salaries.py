from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = list()
        for job in self.jobs_list:
            if job["max_salary"].isdigit():
                salaries.append(int(job["max_salary"]))
        
        return max(salaries)
 
    def get_min_salary(self) -> int:
        salaries = list()
        for job in self.jobs_list:
            if job["min_salary"].isdigit():
                salaries.append(int(job["min_salary"]))
   
        return min(salaries)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("min_salary ou max_salary estão ausentes no dict")

        if not (
            str(job["min_salary"]).isdigit() 
            and str(job["max_salary"]).isdigit()
        ):
            raise ValueError("min_salary ou max_salary estão ausentes no dict")

        min_salary = float(job["min_salary"])
        max_salary = float(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError("min_salary é maior que max_salary")

        if not (
            isinstance(salary, int)
            or (isinstance(salary, str) and salary.isdigit())
        ):
            raise ValueError("salary não é um número inteiro ou string num")
        
        salary = float(salary)
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
