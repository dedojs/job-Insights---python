from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    all_jobs = read(path)
    jobs_type = set()

    for type in all_jobs:
        jobs_type.add(type["job_type"])

    return jobs_type


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    result = []

    for value in jobs:
        if value["job_type"] == job_type:
            result.append(value)

    return result


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    all_jobs = read(path)
    industry = set()

    for type in all_jobs:
        if type["industry"] != "":
            industry.add(type["industry"])

    return industry


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    result = []

    for value in jobs:
        if value["industry"] == industry:
            result.append(value)

    return result


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    salary = []

    for value in all_jobs:
        if value["max_salary"] != "":
            try:
                salary.append(int((value["max_salary"])))
            except ValueError:
                print(ValueError)

    return max(salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    salary = []

    for value in all_jobs:
        if value["min_salary"] != "":
            try:
                salary.append(int((value["min_salary"])))
            except ValueError:
                print(ValueError)

    return min(salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    min = "min_salary"
    max = "max_salary"

    if (min or max) not in job:
        raise ValueError
    elif (type(job[min]) or type(job[max])) != int:
        raise ValueError
    elif job[min] > job[max]:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    return job[max] >= salary >= job[min]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    result = []

    for job in jobs:
        try:
            filter_jobs = matches_salary_range(job, salary)
            if filter_jobs:
                result.append(job)
        except ValueError:
            ...

    return result


# salaries = [0, 1, 5, 1000, 2000, -1, -2]


# print(matches_salary_range({"max_salary": 10000, "min_salary": 200}, -1))
