from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2022-01-01"},
        {"max_salary": 2000, "min_salary": 10, "date_posted": "2012-02-02"},
        {"max_salary": 5000, "min_salary": 50, "date_posted": "2020-02-02"},
    ]

    max_salary = [
        {"max_salary": 5000, "min_salary": 50, "date_posted": "2020-02-02"},
        {"max_salary": 2000, "min_salary": 10, "date_posted": "2012-02-02"},
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2022-01-01"},
    ]

    min_salary = [
        {"max_salary": 2000, "min_salary": 10, "date_posted": "2012-02-02"},
        {"max_salary": 5000, "min_salary": 50, "date_posted": "2020-02-02"},
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2022-01-01"},
    ]

    date_posted = [
        {"max_salary": 1000, "min_salary": 100, "date_posted": "2022-01-01"},
        {"max_salary": 5000, "min_salary": 50, "date_posted": "2020-02-02"},
        {"max_salary": 2000, "min_salary": 10, "date_posted": "2012-02-02"},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == max_salary

    sort_by(jobs, 'min_salary')
    assert jobs == min_salary

    sort_by(jobs, 'date_posted')
    assert jobs == date_posted
