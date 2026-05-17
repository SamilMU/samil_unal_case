import re
from src.pages.base_page import BasePage
from playwright.sync_api import expect

class CareersPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://insiderone.com/careers/#open-roles"
        
        # --- LOCATORS ---
        ## Hero Banner
        self.hero_banner_title = ".insiderone-hero-banner-content-left-content h1" ## Text : Ready to disrupt?
        self.hero_banner_subheading = ".insiderone-hero-banner-content-left-content .insiderone-hero-banner-content-subheading" ## Text : Join a global community of builders and create your life’s work
        self.hero_banner_explore_open_roles_btn = ".insiderone-hero-banner-content-buttons a[href='#open-roles']" ## Text : Explore open roles

        ## Open Roles Section
        self.explore_open_roles_section_title = ".inso-container .insiderone-icon-cards-heading h2" ## Text : Explore open roles
        self.explore_open_roles_section_subheading = ".inso-container .insiderone-gallery-icon-cards-sub-heading" ## Text : Discover our teams, making the world’s marketing and customer engagement teams unstoppable
        self.explore_open_roles_section_see_all_teams_btn = ".inso-container .inso-btn.see-more" ## Text : See all teams
        ## Open Roles - QA Card
        self.explore_open_roles_qa_card_title = ".inso-container [data-department='Quality Assurance'] .insiderone-icon-cards-grid-item-title" ## Text : Quality Assurance
        self.explore_open_roles_qa_card_description = ".inso-container [data-department='Quality Assurance'] .insiderone-icon-cards-grid-item-description" ## Text : Obsessed with perfection? So are we. Our Q&A team meticulously tests every detail to ensure our products are flawless, delivering nothing less than excellence for our customers and theirs.
        self.explore_open_roles_qa_card_open_positions_btn = ".inso-container [data-department='Quality Assurance'] .insiderone-icon-cards-grid-item-btn" ## Text : # Open Positions (We can check text content without the # part for now, since we are not checking requests.)

        ## Open Roles - Software Development Card
        self.explore_open_roles_se_card_title = ".inso-container [data-department='Software Development'] .insiderone-icon-cards-grid-item-title" ## Text : Software Development
        self.explore_open_roles_se_card_open_positions_btn = ".inso-container [data-department='Software Development'] .insiderone-icon-cards-grid-item-btn" ## Text : # Open Positions

        # Job Listings Section
        self.job_list_container = ".postings-group:has(.posting)" # The parent box holding all jobs
        self.job_item = ".postings-group .posting" # The individual job card
        self.job_item_apply_btn = ".posting-apply" ## Text : Apply
        self.job_item_position_name = "[data-qa='posting-name']"
        self.job_item_position_workplace_type = ".posting-categories .workplaceTypes" ## Options : Remote...
        self.job_item_position_contract_type = ".posting-categories .commitment" ## Options : Full-Time (Remote)...
        self.job_item_position_location = ".posting-categories .location" ## Assesment 3 requires this to be "Istanbul, Turkey" but there is a posting for "Berlin, Germany / Munich / Amsterdam, Netherlands / London, United Kingdom", also no Turkey, now Turkiye. So we filter.

        ## Job List filtering by location
        self.job_list_filter_btn = "//div[@class='filter-button filter-button-mlp' and text()='Location']" ## We use xpath
        self.job_list_filter_dropdown_options = "//div[@class='filter-popup' and @style]//li/a" 

        ## Job Posting Details on Lever
        self.lever_job_details_who_we_are_looking_for = "text=Who We Are Looking For"
        self.lever_job_details_what_you_will_do = "text=What You Will Do"
        self.lever_job_details_what_you_will_need = "text=What You Will Need"
        self.lever_job_details_what_we_offer = "text=What We Offer"
        self.lever_job_details_apply_for_this_job_btn = "[data-qa='btn-apply-bottom'] .postings-btn.template-btn-submit"


    def navigate(self):
        """Navigates directly to the open roles anchor."""
        self.page.goto(self.url)

    def verify_page_loaded(self):
        self.verify_element(self.hero_banner_title, "Ready to disrupt?")
        self.verify_element(self.hero_banner_subheading, "Join a global community of buildersand create your life’s work")
        self.verify_element(self.hero_banner_explore_open_roles_btn, "Explore open roles")

    def verify_open_roles_section(self):
        self.highlight_and_click(self.hero_banner_explore_open_roles_btn)
        self.verify_element(self.explore_open_roles_section_title, "Explore open roles")
        self.verify_element(self.explore_open_roles_section_subheading, "Discover our teams, making the world’s marketing and customer engagement teams unstoppable")
        self.verify_element(self.explore_open_roles_section_see_all_teams_btn, "See all teams")

    def filter_qa_jobs(self):
        """Clicks through the team filters to isolate QA roles."""
        self.highlight_and_click(self.explore_open_roles_section_see_all_teams_btn)
        
        self.scroll_to_and_highlight(self.explore_open_roles_qa_card_title)
        self.verify_element(self.explore_open_roles_qa_card_title, "Quality Assurance")
        self.verify_element(self.explore_open_roles_qa_card_description, "Obsessed with perfection? So are we. Our Q&A team meticulously tests every detail to ensure our products are flawless, delivering nothing less than excellence for our customers and theirs.")
        self.verify_element(self.explore_open_roles_qa_card_open_positions_btn, "Open Positions")
        
        self.click_and_wait_for_response(self.explore_open_roles_qa_card_open_positions_btn, "/cdn-cgi/challenge-platform", expected_status=200) ## Can be used on flaky points or points that needs api response too. 

    def filter_software_development_jobs(self):
        """Clicks through the team filters to isolate Software Development roles."""
        self.highlight_and_click(self.explore_open_roles_section_see_all_teams_btn)

        self.scroll_to_and_highlight(self.explore_open_roles_se_card_title)
        self.verify_element(self.explore_open_roles_se_card_title, "Software Development")
        self.verify_element(self.explore_open_roles_se_card_open_positions_btn, "Open Positions")

        self.click_and_wait_for_response(self.explore_open_roles_se_card_open_positions_btn, "/cdn-cgi/challenge-platform", expected_status=200)

    def verify_redirection_to_lever_and_job_list_presence(self):
        """After clicking the QA filter, we should be redirected to Lever with the list of QA jobs."""
        expect(self.page).to_have_url("https://jobs.lever.co/insiderone?team=Quality%20Assurance")

        """Asserts the main container for the jobs has loaded."""
        self.verify_element(self.job_list_container, apply_bg=False)

    def verify_sd_redirection_and_job_list_presence(self):
        """After clicking the Software Development filter, verifies Lever URL and job list presence."""
        expect(self.page).to_have_url("https://jobs.lever.co/insiderone?team=Software%20Development")
        self.verify_element(self.job_list_container, apply_bg=False)

    def filter_job_list_by_location(self, location: str):
        """Filters the job list by a specific location."""
        self.highlight_and_click(self.job_list_filter_btn)

        self.page.locator(self.job_list_filter_dropdown_options).first.wait_for(state="visible")

        location_option = self.page.locator(self.job_list_filter_dropdown_options).filter(has_text=location).first
        self.highlight_and_click(location_option)

    def verify_qa_jobs_details(self):
        """
        Loops through every visible job card to ensure the position, 
        department, and location perfectly match the requirements.
        """

        self.page.locator(self.job_item).first.wait_for(state="visible")
        

        jobs = self.page.locator(self.job_item).all()
        
        assert len(jobs) > 0, "No QA jobs were found on the page."

        for job in jobs:
            # Dynamic but somewhat common QA role titles.
            expected_title = re.compile(r"Software (Quality Assurance|QA) Engineer")
            self.verify_element(job.locator(self.job_item_apply_btn))

            self.verify_element(job.locator(self.job_item_position_name), expected_title)
            self.verify_element(job.locator(self.job_item_position_workplace_type), "Remote")
            self.verify_element(job.locator(self.job_item_position_contract_type), "Full-Time (Remote)")
            self.verify_element(job.locator(self.job_item_position_location), "Istanbul") ## Should assert against test file variable. Maybe in the future.

    def verify_software_development_jobs_details(self):
        """
        Loops through every visible job card to ensure the location
        is Istanbul, Turkiye after filtering.
        """
        self.page.locator(self.job_item).first.wait_for(state="visible")

        jobs = self.page.locator(self.job_item).all()

        assert len(jobs) > 0, "No Software Development jobs were found on the page."

        for job in jobs:
            self.verify_element(job.locator(self.job_item_position_location), "Istanbul, Turkiye")

    def click_apply_and_verify_redirect(self):
        """
        Clicks the apply button on the first job and verifies Lever redirection. Asserts some titles on new page. 
        """
        self.click_apply_and_assert_redirect_to_lever()
        self.verify_element(self.lever_job_details_who_we_are_looking_for)
        self.verify_element(self.lever_job_details_what_you_will_do)
        self.verify_element(self.lever_job_details_what_you_will_need)
        self.verify_element(self.lever_job_details_what_we_offer)
        self.verify_element(self.lever_job_details_apply_for_this_job_btn, "apply for this job")

    def click_apply_and_verify_redirect_without_posting_content(self):
        """
        Clicks the apply button on the first job and verifies Lever redirection. Only button assertion on the new page.
        """
        self.click_apply_and_assert_redirect_to_lever()
        self.verify_element(self.lever_job_details_apply_for_this_job_btn, "apply for this job")

    def click_apply_and_assert_redirect_to_lever(self):
        first_job_apply_btn = self.page.locator(self.job_item).first.locator(self.job_item_apply_btn)
        first_job_apply_btn.wait_for(state="visible")
        self.highlight_and_click(first_job_apply_btn)
        expect(self.page).to_have_url(re.compile(r"https://jobs.lever.co/insiderone/.+"))