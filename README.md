# E2E Ecommerce Framework : Play with Python

This project is a demonstration of how I have implemented end-to-end testing using Selenium WebDriver and Pytest framework. I have learned how to use these tools and applied my knowledge to create a test suite that can run tests against a web application.

The project uses Pytest as a test runner, which allows me to write test functions using the built-in assertion library. I have also used Selenium WebDriver to automate browser interactions and simulate user actions.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

* Python 3.x
* pip

### Installing

1. Clone the repository: `git clone git@github.com:Sr-Shohan/E2E_Framework.git`
2. Change directory to the project: `cd your-repo`
3. Install the required packages: `pip install -r requirements.txt`

### Running the Tests

To run the tests, execute the following command from the project directory:
`pytest`

This will run all the tests in the project.

To run the tests, open a terminal window, activate the virtual environment (if you haven't already), and navigate to the project directory. Then, run the following command:


    `pytest --alluredir=./allure-results`
This will run all the tests and generate a report in the allure-results directory. To view the report, run the following command:

    `allure serve allure-results/`

## Built With

* [Selenium](https://www.selenium.dev/) - Web testing framework
* [pytest](https://docs.pytest.org/en/stable/) - Testing framework
* [Allure](https://docs.qameta.io/allure/) - Test report generator


