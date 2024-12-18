Web Application testing using Python, Selenium and Pytest

Multi-browser framework for End-to-End Automation Testing with PyTest-Selenium

Prerequisites:
In order to run these tests please install:
Python 3.8+
pip - Python package manager
WebDriver (e.g., ChromeDriver, GeckoDriver, any other )

Installation Process:
Get a clone this repository:
git clone https://github.com/yourusername/your-project.git
cd Project_Name

Dependencies: All required dependencies kept in this text file
pip install -r requirements.txt

Project Structure
Assignment/
│
├── tests/                   # All test cases
│   ├── test_tiles.py        # test file
│   └── conftest.py          # Shared fixtures/configuration
│
├── pages/                   # Page Object Model (POM) classes
│
├── locators/                # Folder containing locators for each page
│   └── locators.py          # File with all the XPath locators
│
├── utils/                   # Utility functions/helpers
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
1. Run all tests:
 pytest  # default browser Chrome
 pytest --browser=firefox
 pytest --browser=chrome
2.Generate an HTML Report:
 pytest --html=reports/html/report.html  # HTML reports created under reports folder

Screenshots: Captured for failed tests and saved in screenshots/.

