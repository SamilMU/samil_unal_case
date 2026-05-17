from src.pages.careers_page import CareersPage

class TestCareersFlow:

    def test_qa_jobs_filtering_and_redirect(self, page_context):
        """
        Validates the lever redirectin via open positions, job listing details accuracy, 
        and the Lever form redirection.
        """
        careers_page = CareersPage(page_context)

        careers_page.navigate()
        careers_page.verify_page_loaded()
        careers_page.handle_cookies()  # In case the cookie banner appears on this page as well

        careers_page.verify_open_roles_section()
        careers_page.filter_qa_jobs()

        careers_page.verify_redirection_to_lever_and_job_list_presence()

        careers_page.filter_job_list_by_location("Istanbul")

        careers_page.verify_qa_jobs_details()

        careers_page.click_apply_and_verify_redirect()

    def test_software_development_jobs_filtering(self, page_context):
        """
        Validates the careers page filtering for Software Development jobs,
        proving the reusability of the POM architecture.
        """
        careers_page = CareersPage(page_context)

        # 1. Open page, verify it is loaded, and handle cookies if the banner appears
        careers_page.navigate()
        careers_page.verify_page_loaded()
        careers_page.handle_cookies()

        # 2. Navigate to open roles and filter for Software Development
        careers_page.verify_open_roles_section()
        careers_page.filter_software_development_jobs()

        # 3. Verify redirection to Lever and job list presence
        careers_page.verify_sd_redirection_and_job_list_presence()

        # 4. Filter the job list by location ("Istanbul, Turkiye")
        careers_page.filter_job_list_by_location("Istanbul, Turkiye")

        # 5. Verify job details (Location only)
        careers_page.verify_software_development_jobs_details()

        # 6. Click apply and verify Lever redirect
        careers_page.click_apply_and_verify_redirect_without_posting_content()