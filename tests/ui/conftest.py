import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from src.pages.home_page import HomePage
from src.pages.careers_page import CareersPage

@pytest.fixture(scope="function")
def page_context():
    """
    MVP Framework Setup & Teardown.
    Launches the browser, creates a context/page, yields it to the test, 
    and strictly tears it down afterward.
    """
    with sync_playwright() as p:
        # Slowed down for demonstration purposes, remove slow_mo for faster execution
        # browser: Browser = p.chromium.launch(headless=False, slow_mo=10, args=["--window-size=2560,1440", "--start-maximized"])

        ## For CI/CD and faster execution, we can run headless and without slow_mo
        browser: Browser = p.chromium.launch(headless=True)
        
        # We use a custom viewport to ensure responsive UI elements don't hide our buttons or it doesn't switch to a mobile layout. Adjust as needed.
        context = browser.new_context(viewport={"width": 2560, "height": 1440})
        page: Page = context.new_page()
        
        yield page 
        
        # This guarantees the browser is killed even if the test fails
        context.close()
        browser.close()

@pytest.fixture
def home_page(page_context) -> HomePage:
    """Injects the HomePage object, pre-loaded with the browser context."""
    return HomePage(page_context)

@pytest.fixture
def careers_page(page_context) -> CareersPage:
    """Injects the CareersPage object, pre-loaded with the browser context."""
    return CareersPage(page_context)