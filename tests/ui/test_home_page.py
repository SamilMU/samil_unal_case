from src.pages.home_page import HomePage

class TestHomeFlow:

    def test_insider_home_page_loads(self, page_context):
        """
        Validates that the Insider home page opens successfully 
        and all main blocks are loaded. Some are asserted more thoroughly than others but for the sake of this being a case-study, most unique elements of each block are checked for presence.
        """
        home_page = HomePage(page_context)
        
        home_page.navigate()
        
        home_page.verify_page_loaded()

        home_page.verify_homepage_all_sections()

        home_page.handle_cookies()
        
        assert "Insider" in page_context.title()