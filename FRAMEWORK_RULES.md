# QA Automation Framework Rules & Best Practices

This document outlines the strict industry-standard conventions and architectural patterns used in this repository. All AI assistants (Copilot, Cursor, Claude) and contributors must adhere to these rules.

## 1. Architectural Pattern: Page Object Model (POM)
- We do not use monolithic test files.
- The framework strictly separates test execution from page interaction logic.
- All page interactions (clicks, fills, waits) must be wrapped in a `BasePage` utility class.
- Page classes (e.g., `HomePage`, `CareersPage`) inherit from `BasePage` and contain locators and business logic.
- Tests should only contain assertions and calls to Page Object methods. No raw Playwright `page.locator()` calls inside the `tests/` directory.

## 2. Test Dependency & Scope
- Tests must have a single responsibility. 
- Do not chain tests together. For example, the homepage loading verification and the careers page job verification must be separate tests (`test_home_page.py` and `test_careers.py`) to prevent false negatives.
- Use `pytest` fixtures inside `conftest.py` to inject browser instances and Page Objects into test functions.

## 3. Naming Conventions (Strict Pythonic / PEP 8)
- **Files and Directories:** Use `snake_case` (e.g., `base_page.py`, `test_careers.py`).
- **Pytest Files:** Test files MUST start with `test_` to be discovered.
- **Classes:** Use `PascalCase` (e.g., `HomePage`, `TestCareersFlow`).
- **Pytest Classes:** If grouping tests in a class, it MUST start with `Test`.
- **Functions/Methods/Variables:** Use `snake_case` (e.g., `verify_blocks_loaded()`, `custom_click()`).
- **Pytest Functions:** Test methods MUST start with `test_`.
- **Constants:** Use `UPPER_SNAKE_CASE` for static values like URLs or timeouts.