API- PATCH Method testing using Python, Requests and Pytest


Prerequisites:
In order to run these tests please install:
Python 3.8+
pip - Python package manager
Requests Library

Installation Process:
Get a clone this repository:
git clone https://github.com/yourusername/your-project.git
Assignment_API_Pytest

Dependencies: All required dependencies kept in this text file
pip install -r requirements.txt

Project Structure
Assignment/
│
├── tests/                          # All test cases
│   ├── test_PATCH_METHOD.py        # test file
│   └── conftest.py                 # Shared fixtures/configuration
│
├── utils/                   # Utility functions/helpers
│   └── api_helper.py        # A Helper Class for various functions associated with API Calls.
│
├── data/                    # Test data
│   └── config.yaml          # Configuration settings
│
├── reports/                 # Test reports and logs
│   └── html/                # HTML reports
│
├── screenshots/             # Screenshots for failures or debugging
│
├── .env                     # Environment variables (optional)
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
├── pytest.ini               # Pytest configuration
└── README.md                # Project documentation

Config File:
All all configurable parameters in config.yaml file under data folder:
 base_url
 timeout

How to run the test:
1.Run all tests:
 pytest 
2.Generate an HTML Report:
 pytest --html=reports/html/report.html  # HTML reports created under reports folder

Screenshots: Captured for failed tests and saved in screenshots/.

