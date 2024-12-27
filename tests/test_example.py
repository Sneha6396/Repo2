import pytest

# Add pytest options to capture custom command-line arguments
def pytest_addoption(parser):
    parser.addoption("--data1", action="store", default=None, help="Data passed from Repo-A")
    parser.addoption("--data2", action="store", default=None, help="Another data value")

@pytest.fixture
def custom_data(request):
    return {
        "data1": request.config.getoption("--data1"),
        "data2": request.config.getoption("--data2"),
    }

def test_with_arguments(custom_data):
    data1 = custom_data["data1"]
    data2 = custom_data["data2"]

    print(f"Data1: {data1}")
    print(f"Data2: {data2}")

    # Example assertions to check the data passed
    assert data1 == "value1"
    assert data2 == "value2"

