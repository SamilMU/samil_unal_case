import re
from typing import Union
from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

        ## Cookie header accept only necessary btn (common across pages)
        self.cookie_inform_dialog_only_necessary_btn = "#cookie-law-info-bar.wt-cli-cookie-bar #wt-cli-accept-btn"

    def highlight_and_click(self, locator_or_string: Union[str, Locator], js_click: bool = False):
        """
        Waits for an element to be visible, highlights it in yellow for visual debugging,
        and performs a click (either standard Playwright click or a JS fallback click).
        """
        if isinstance(locator_or_string, str):
            element: Locator = self.page.locator(locator_or_string).first
        else:
            element: Locator = locator_or_string
        
        element.wait_for(state="visible")
        
        # Highlight the element for visual debugging
        element.evaluate("node => node.style.backgroundColor = 'yellow'")
        element.evaluate("node => node.style.border = '2px solid red'")
        
        if js_click:
            # Force click via JavaScript if standard click is not working
            element.evaluate("node => node.click()")
        else:
            element.click()

    def is_element_visible(self, locator_string: str) -> bool:
        """
        Returns True if the element is visible on the page, avoiding test failure 
        if we just want to check presence.
        """
        element = self.page.locator(locator_string).first
        try:
            element.wait_for(state="visible", timeout=3000)
            return True
        except Exception:
            return False

    def scroll_to_and_highlight(self, locator_or_string: Union[str, Locator], apply_bg: bool = True) -> Locator:
        """
        Scrolls the element into the viewport if it isn't already, 
        and highlights it for visual debugging.
        Accepts either a CSS string or an existing Playwright Locator object.
        """

        if isinstance(locator_or_string, str):
            element = self.page.locator(locator_or_string).first
        else:
            element = locator_or_string
            
        element.scroll_into_view_if_needed()

        # Highlight the element for visual debugging
        try:
            element.evaluate("node => node.style.outline = '2px solid red'")
            if apply_bg:
                element.evaluate("node => node.style.backgroundColor = 'rgba(255, 255, 0, 0.3)'")
        except Exception:
            pass
            
        return element

    def verify_element(self, locator_or_string: Union[str, Locator], expected_text: Union[str, re.Pattern] = None, apply_bg: bool = True):
        """
        Scrolls to the element, highlights it, and natively asserts its visibility.
        """
        element = self.scroll_to_and_highlight(locator_or_string, apply_bg)
        
        expect(element).to_be_visible()
        
        if expected_text:
            expect(element).to_contain_text(expected_text)

    def handle_cookies(self):
        """If a cookie banner appears, dismiss it so it doesn't block clicks."""
        if self.is_element_visible(self.cookie_inform_dialog_only_necessary_btn):
            self.highlight_and_click(self.cookie_inform_dialog_only_necessary_btn)
    
    def click_and_wait_for_response(self, locator_or_string: Union[str, Locator], url_substring: str, expected_status: int = 200, apply_bg: bool = True):
        """
        Scrolls to an element, clicks it, and waits for a specific network response 
        to return the expected status code before proceeding.
        """

        element = self.scroll_to_and_highlight(locator_or_string, apply_bg)
        
        with self.page.expect_response(
            lambda response: url_substring in response.url and response.status == expected_status,
            timeout=10000
        ) as response_info:
            element.click()
            
        return response_info.value