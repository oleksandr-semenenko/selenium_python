# Selenium + Python Test Automation Framework
This repository contains a Python-based UI test automation framework built with Selenium WebDriver and pytest.

The framework follows the Page Object Model (POM) design pattern and demonstrates a hybrid QA approach, combining strong manual testing expertise with automation framework development.

---

## 🚀 Key Features

- Modular and scalable project structure
- Page Object Model (POM) implementation
- Reusable BasePage abstraction
- Explicit waits implemented within action methods to reduce flaky tests
- Test data separation using factory pattern
- Environment variables for secure configuration
- Pytest fixtures for reusable setup/teardown
- CI-ready structure (GitHub Actions compatible)
- Docker support for isolated execution

---

## 🏗 Architecture Overview

The framework is built using the Page Object Model (POM) design pattern.

Core Design Principles
- BasePage contains reusable interaction methods:
  - open()
  - wait_and_find()
	- type()
	- click()
- Each Page Object inherits from BasePage
- Explicit waits are implemented inside action methods to improve stability
- Test data is separated into utils/data_factory.py
- Pytest fixtures are defined in conftest.py
- Environment variables are used for credentials and configuration
- The structure is designed to be CI/CD and Docker ready

This design improves:
- Maintainability
- Readability
- Reusability
- Test stability

## 🎯 Hybrid QA Focus

This project reflects a Hybrid QA approach, combining:
- Strong manual testing background
- Business-level scenario validation
- Automation framework design
- Clean separation of UI logic and test logic
- Technical implementation using Python and Selenium


## 🧪 Example Test

```python
def test_update_job_title(employee_profile_page):
    employee_profile_page.set_job_title(
        data_factory.random_job_title()
    )
    employee_profile_page.save()
    employee_profile_page.verify_job_title_updated()
```

## 🏗️ Project Structure

```plaintext
selenium_python/
├── .github/workflows/ui-tests.yml   # GitHub Actions workflow
├── pages/                           # Page Object classes
├── tests/                           # Test cases
├── utils/                           # Utility functions (data factory, helpers)
├── data/                            # Test data files (optional/extendable)
├── drivers/                         # WebDriver binaries (optional)
├── config/                          # Configuration files (optional)
├── test-reports/                    # Test execution reports
├── requirements.txt                 # Python dependencies
├── conftest.py                      # Global pytest fixtures
└── pytest.ini                       # Pytest configuration
```

---

## 🛠 Prerequisites

- Python 3.9+
- pip
- Chrome / Firefox browser
- WebDriver (chromedriver/geckodriver) available in PATH

---

## 📦 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/oleksandr-semenenko/selenium_python.git
    cd selenium_python

    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Running Tests

### 💡 Run all tests:

```bash
pytest -v
```

### 📌 Run a specific test file:

```bash
pytest tests/test_example.py
```

### Run tests with marker:
```bash
pytest -m regression -v
```

## ⚙️ Environment Configuration

The framework supports environment variables.
Example (macOS/Linux):
```bash
export BASE_URL=https://example.com
export LOGIN=user
export PASSWORD=secret
```

Example (Windows PowerShell):

```powershell
setx BASE_URL "https://example.com"
```

## 🚀 CI Integration

The project is compatible with:
- GitHub Actions
- Bitbucket Pipelines
- Docker-based execution

The workflow file is located in:
```bash
    .github/workflows/
```

## 🧠 Future Improvements

- Integration with Allure reporting
- API automation layer (requests + pytest)
- Parallel test execution
- Test environment configuration management

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🙌 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request.
