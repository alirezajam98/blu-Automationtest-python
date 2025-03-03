
# Android Automation

## Overview
This project is an automation framework for testing Android applications using **Appium** and **Pytest**. It supports:
- Multi-device configurations
- Detailed logs and HTML reports
- Automated end-to-end flows for KYC and card-related functionalities.

---

## Features
- **Multi-Device Support**: Test multiple Android devices effortlessly.
- **Modular Design**: Organized test structure for easy scalability and maintenance.
- **Detailed Logging**: Logs saved in `test_log.log` for debugging and tracking.
- **Screenshot Capture**: Automatically saves screenshots for failed tests.
- **HTML Reports**: Test results are saved as HTML reports in the `report/` folder.
- **Custom Configurations**: Easily configurable test parameters using `device_config.py`.

---

## Installation

### Prerequisites
1. **Python 3.8+**
2. **Node.js** (for Appium)
3. **Appium** installed globally via npm:
   ```bash
   npm install -g appium
   ```
4. **Android SDK** with required platform tools.

### Steps
1. Clone the repository:
   ```bash
   git clone https://git.bluteam.ir/a.jamshidi/android-automation.git
   cd android-automation
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # For Windows: .venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Appium server:
   ```bash
   appium
   ```

---

## Usage

### Run All Tests
Execute the main test runner:
```bash
python run_test.py
```

### Run Specific Test File
To run a specific test file:
```bash
pytest tests/kyc/test_national_ID_card_upload.py
```

### Run Tests for Specific Device
Configure the desired device in `run_test.py` and execute:
```bash
python run_test.py
```

---

## Project Structure
```
android-automation/
├── conftest.py               # Global test configurations and fixtures
├── run_test.py               # Main test execution script
├── devices/
│   └── device_config.py      # Device configurations
├── tests/
│   ├── card/  
├── pages/
│   ├── kyc_pages/            # Pages element ID for kyc   functionalities
│   └── card_pages/           # Pages element ID for card flows
├── utils/
│   ├── config.py             # Utility functions for test execution
│   ├── utils.py              # Utility functions like username generation
│   └── kyc_panel.py          # KYC-related test utilities
├── screenshots/              # Folder for storing screenshots
├── report/                   # Folder for storing HTML reports
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## Device Configuration
All device configurations are stored in `devices/device_config.py`. Add or modify device configurations as follows:
```python
device_configs = {
    "Galaxy S24 Ultra": {
        "platformName": "Android",
        "platformVersion": "14.0.0",
        "udid": "192.168.137.93:5555",
        "appActivity": "com.samanpr.blu.presentation.BaseActivity",
        "appPackage": "com.samanpr.blu.dev",
        "automationName": "UiAutomator2"
    },
    "Galaxy A11": {
        "platformName": "Android",
        "platformVersion": "12.0.0",
        "udid": "R9HN70VWB5J",
        "appActivity": "com.samanpr.blu.presentation.BaseActivity",
        "appPackage": "com.samanpr.blu.dev",
        "automationName": "UiAutomator2"
    }
}
```

---

## Key Features

### Logging
Logs are saved in `test_log.log` for all tests. Example log snippet:
```
2024-11-27 15:30:00 - INFO - Running tests on Galaxy S24 Ultra...
2024-11-27 15:30:01 - INFO - Found 5 tests for device 'Galaxy S24 Ultra'
```

### HTML Reports
Test results are saved as HTML files in the `report/` directory. For example:
```
report/report_Galaxy_S24_Ultra.html
```

### Screenshot Capture
Screenshots for failed tests are saved in the `screenshots/` folder:
```
screenshots/test_failure_01.png
```

---

## Writing Tests
To write new tests, add files under the `tests/` directory. Example test structure:
```python
import pytest

def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
```

---

## Running CI/CD
Integrate with GitLab CI/CD or any CI tool for continuous integration. Example `.gitlab-ci.yml` file:
```yaml
stages:
  - test

test:
  script:
    - python run_test.py
```

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-branch
   ```
4. Open a Pull Request.

---

# Allure Integration in Test Automation

## Overview

Allure is a flexible lightweight multi-language test reporting tool. It provides a clear representation of test execution results and allows tagging and organizing tests effectively.

---

## Key Features

- **Detailed Test Reports**: Generate interactive and visually appealing reports.
- **Steps Tracking**: Log detailed steps for each test.
- **Tagging**: Organize tests using tags like severity, epic, feature, etc.
- **Attachments**: Add screenshots, logs, or other files.
- **Integration**: Supports integration with multiple CI/CD tools.

---

## Installation

1. Install Allure Commandline Tool:
   ```bash
   brew install allure  # For macOS
   scoop install allure # For Windows
   ```
   For other platforms, refer to the [Allure Installation Guide](https://docs.qameta.io/allure/#_get_started).

2. Add Allure Pytest Package:
   ```bash
   pip install allure-pytest
   ```

3. Add Allure to your CI/CD pipeline if required.

---

## Usage in Python Tests

### Adding Allure Annotations

```python
import allure

@allure.epic("User Management")
@allure.feature("Login Functionality")
@allure.story("User logs in with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_login():
    with allure.step("Open login page"):
        # Step 1: Open login page
        pass

    with allure.step("Enter credentials"):
        # Step 2: Enter username and password
        pass

    with allure.step("Submit login form"):
        # Step 3: Submit login form
        assert True  # Example assertion
```

---

## Allure Decorators and Tags

### `@allure.epic`
Groups tests under a high-level category, e.g., a project or module.

### `@allure.feature`
Defines a specific feature under the epic.

### `@allure.story`
Further categorizes features into specific user stories or scenarios.

### `@allure.severity`
Sets the severity level of the test. Available levels:
- `BLOCKER`
- `CRITICAL`
- `NORMAL`
- `MINOR`
- `TRIVIAL`

### `allure.step`
Wraps a section of code as a step in the report.

### `allure.attach`
Adds attachments to the test report. Common usages:
```python
allure.attach.file("screenshot.png", name="Screenshot", attachment_type=allure.attachment_type.PNG)
allure.attach("Some text data", name="Log", attachment_type=allure.attachment_type.TEXT)
```

---

## Generating Reports

1. Run tests with Allure:
   ```bash
   pytest --alluredir=allure-results
   ```

2. Generate the report:
   ```bash
   allure serve allure-results
   ```

---

## Example Report Screenshot

Below is a sample screenshot of an Allure test report:

![Allure Report Sample](https://webdriver.io/assets/images/allure-bb6c9b036b07594235a5aca5aff5ac43.png)

---

## Additional Resources

- [Official Documentation](https://docs.qameta.io/allure/)
- [Allure Pytest Integration](https://docs.qameta.io/allure/#_pytest)

## License
This project is licensed under the blu License.
