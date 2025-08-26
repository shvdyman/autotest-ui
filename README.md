# UI Course Automation Tests

This project implements automated tests for the UI Course Test Application using Python, Pytest, Allure, and Playwright.

## 📋 Project Overview

The goal of this project is to automate the testing of the UI Course application. The automated tests verify various functionalities of the application to ensure its stability and correctness. The project structure follows best practices for organizing test code with clear, maintainable scripts.

**Test Application Source Code**: [GitHub Repository](https://github.com/shvdyman/autotest-ui)

## 🚀 Getting Started

### Prerequisites
- Python 3.11
- Git
- pip (Python package manager)

### Clone the Repository

git clone https://github.com/shvdyman/autotest-ui.git
cd autotest-ui
Create a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating system:

Linux / MacOS
python3 -m venv venv
source venv/bin/activate
Windows
python -m venv venv
venv\Scripts\activate
Install Dependencies
Once the virtual environment is activated, install the project dependencies listed in requirements.txt:

pip install -r requirements.txt
Additional Playwright Setup (if needed)
If you're running Playwright for the first time, you might need to install the required browsers:

playwright install
Running the Tests with Allure Report Generation
To run the tests and generate an Allure report, use the following command:

pytest -m "regression" --alluredir=./allure-results
This will execute all tests in the project and display the results in the terminal.

Viewing the Allure Report
After the tests have been executed, you can generate and view the Allure report with:

allure serve allure-results
This command will open the Allure report in your default web browser.
