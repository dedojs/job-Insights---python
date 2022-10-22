from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    data = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    mock = {
        'title': 'Motorista',
        'salary': '3000',
        'type': 'full time',
    }
    assert mock in data
