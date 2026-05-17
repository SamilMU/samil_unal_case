# Insider One QA Automation Framework

## Project Description
This repository contains a Quality Assurance automation framework built for the Insider One Case Study. It utilizes Python to execute UI testing (Playwright), API testing (Requests), and Performance testing (Locust). The framework is designed around a scalable Page Object Model (POM) architecture, ensuring high reusability and clean test execution.

*Note: AI assistance was utilized to generate boilerplate code, documentation and Regex patterns for Tasks 2 (UI Automation) and 3 (API/Load Testing). All AI generations were strictly constrained by a custom `FRAMEWORK_RULES.md` and validated manually via runtime execution.*

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SamilMU/samil_unal_case.git
   cd samil_unal_case
    ```
    
2. **Initialize a Virtual Environment & Install Dependencies:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows
    # source venv/bin/activate    # On macOS/Linux

    pip install -r requirements.txt
    ```

3. **[Optional] Install Playwright Browsers:**
    ```bash
    playwright install
    ```

## How to Run the Tests

# Run All Tests 
To satisfy the requirement of zero manual intervention, this framework includes an orchestrator script that runs the entire suite sequentially including installing the browser libraries of playwright. It is skipped if already installed .(API -> Performance -> UI).

```bash
python run_all_tests.py
```

# Run UI Tests (Playwright):
Note: Configured to run headless (browser invisible) by default via conftest.py.

```bash
python -m pytest tests/ui/ -v
```

# Run API Tests (Swagger Petstore):
Includes professional logging output.

```bash
python -m pytest tests/api/ -v -s
```

# Run Load Tests (Locust headless):
Simulates 1 user for 30 seconds with cache-busting logic.

```bash
locust -f tests/load/locustfile.py --headless -u 1 -r 1 -t 30s
```

## Project Structure

* /prompts/ - Documentation of AI collaboration iterations.

* /src/pages/ - Page Object Model classes and Base utilities.

* /tests/ui/ - Playwright UI test scripts and fixtures.

* /tests/api/ - Requests-based CRUD operations.

* /tests/load/ - Locust performance scripts.


***