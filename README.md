# qa-automation-demo
A showcase repository demonstrating automated software testing with Selenium, Pytest, and GitHub Actions CI/CD. Includes UI tests, API tests, and reporting integration with HTML reports and artifacts.

This is a **demo automation project** that tests login functionality on [SauceDemo](https://www.saucedemo.com/).

## Features
- Selenium + Pytest
- Page Object Model
- Positive and negative login test
- HTML reporting with screenshots
- Easy CI/CD integration (Azure DevOps, Jenkins)


## Project Structure
```
qa-automation-demo/
│── tests/
│ ├── ui/ # UI tests (Selenium)
│ ├── api/ # API tests (Requests)
│── requirements.txt
│── pytest.ini
│── .github/
│ └── workflows/
│ └── ci.yml
```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/<your_username>/qa-automation-demo.git
   cd qa-automation-demo
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Run tests
   ```
   pytest
   ```

## CI/CD Integration
This project uses GitHub Actions to automatically execute tests:

All tests run on each push or pull request to the main branch
Test results are uploaded as artifacts (pytest-report) and available for download

## Purpose
This project serves as a portfolio showcase for QA Automation and CI/CD.
It can be extended with additional tests, integrated into different build pipelines, or connected to test management tools.
