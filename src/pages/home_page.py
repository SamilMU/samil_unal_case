from src.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://insiderone.com/"

        ## HOMEPAGE - General
        self.page_complete_section = "section.homepage-hero"
        ## HOMEPAGE - Top most Menu
        self.header_top_menu = ".container .header-top-menu"
        self.header_top_menu_actions = ".container .header-top-action"
        ## HOMEPAGE - Top Menu
        self.header_logo_img = ".header-logo svg"
        self.header_menu_list = ".header-menu .header-menu-list"
        self.header_menu_platform_btn = ".header-menu .header-menu-list [data-text='Platform']"
        self.header_menu_industries_btn = ".header-menu .header-menu-list [data-text='Industries']"
        self.header_menu_customers_btn = ".header-menu .header-menu-list [data-text='Customers']"
        self.header_menu_resources_btn = ".header-menu .header-menu-list [data-text='Resources']"
        self.header_menu_platform_tour_btn = ".header-menu .header-menu-action [href*='product-demo']" ## Product demo is platform tour ? 
        self.header_menu_get_a_demo_btn = ".header-menu .header-menu-action [href*='request-a-demo']" 
        ## Top Menu Dropdowns
        self.header_menu_dropdown_general = ".header-menu-item-dropdown.show"
        ## Dropdowns - Platform
        self.platform_dropdown_platform_overview_link = ".header-menu-item-dropdown-item-wrapper .header-menu-item-dropdown-item:nth-child(1) [href*='platform']"
        self.platform_dropdown_platform_overview_desc = ".header-menu-item-dropdown-item-wrapper .header-menu-item-dropdown-item:nth-child(1) [href*='platform'] p" ## Text : Explore Insider One, everything you need, nothing you don’t, all in one place
        self.platform_dropdown_integration_hub_link = ".header-menu-item-dropdown-item-wrapper .header-menu-item-dropdown-item:nth-child(2) [href*='integrations']"
        self.platform_dropdown_integration_hub_desc = ".header-menu-item-dropdown-item-wrapper .header-menu-item-dropdown-item:nth-child(2) [href*='integrations'] p"
        ## Dropdowns - Platform - Capabilities
        self.platform_dropdown_capabilities_title = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) .title h3" ## Text : Capabilities
        self.platform_dropdown_capabilities_insider_one_ai = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) [href*='ai-overview']" ## Text : Insider One AI™
        self.platform_dropdown_capabilities_customer_data_management = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) [href*='customer-data-management']" ## Text : Customer Data Management
        self.platform_dropdown_capabilities_personalization = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) [href*='ai-personalization']" ## Text : Personalization
        self.platform_dropdown_capabilities_journey_orchestration = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) [href*='customer-journey/orchestration']" ## Text : Journey Orchestration
        self.platform_dropdown_capabilities_reporting_and_data = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) [href*='reporting-analytics']" ## Text : Reporting & Data
        self.platform_dropdown_capabilities_behavioral_analytics = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(2) a[href*='behavioral-analytics'].indented" ## Intend intentional. Text : Behavioral Analytics
        ## Dropdowns - Platform - Channels
        self.platform_dropdown_channels_title = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) .title h3" ## Text : Channels
        self.platform_dropdown_channels_web = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='web/']" ## Text : Web
        self.platform_dropdown_channels_email = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='email']" ## Text : Email
        self.platform_dropdown_channels_site_search = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='/eureka-search/'] span" ## Eureka search. Text : Site search
        self.platform_dropdown_channels_conversational_cx = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='conversational-cx']" ## Text : Conversational CX
        self.platform_dropdown_channels_whatsapp = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='whatsapp']" ## Text : WhatsApp
        self.platform_dropdown_channels_web_push = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='web-push']" ## Text : Web Push
        self.platform_dropdown_channels_instory = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='instory']" ## Text : InStory
        self.platform_dropdown_channels_app = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='/app']" ## Text : App
        self.platform_dropdown_channels_sms_and_rcs = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(3) [href*='sms']" ## Text : SMS & RCS
        ## Dropdowns - Platform - Why Insider One
        self.platform_dropdown_why_insider_one_title = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) .title h3" ## Text : WHY INSIDER ONE
        self.platform_dropdown_why_insider_one_join_migration_movement = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='migration-movement']" ## Text : Join the $0 Migration Movement™
        self.platform_dropdown_why_insider_one_join_migration_movement_desc = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='migration-movement'] p" ## Text : Migration without fear, lock‑in, or hidden costs.
        self.platform_dropdown_why_insider_one_the_insider_one_difference = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='why-insiderone']" ## Text : The Insider One Difference
        self.platform_dropdown_why_insider_one_the_insider_one_difference_desc = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='why-insiderone'] p" ## Text : Discover what makes us different
        self.platform_dropdown_why_insider_one_compare_vendors = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='compare-insiderone']" ## Text : Compare Vendors
        self.platform_dropdown_why_insider_one_compare_vendors_desc = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='compare-insiderone'] p" ## Text : Find out how we compare to other industry players
        self.platform_dropdown_why_insider_one_switch_to_insider_one = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='insiderone-switch']" ## Text : Switch to Insider One
        self.platform_dropdown_why_insider_one_switch_to_insider_one_desc = ".header-menu-item-dropdown.show > .container > .header-menu-item-dropdown-item:nth-child(4) [href*='insiderone-switch'] p" ## Text : Discover why world’s best-loved brands choose Insider One
        ## Dropdowns - Industries
        ## Dropdowns - Industries - Success Story Box
        self.industries_dropdown_success_story_box = "[href*=case-studies].header-menu-item-dropdown-item" ## It has M.A.C. image in it
        ## Dropdowns - Industries - Column 1 ## VISUAL BUG ? FIRST LINES OF DESCRIPTIONS ARE BEING HIDDEN WHEN HOVERED OVER. 
        self.industries_dropdown_retail_and_ecommerce_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='retail']" ## Text : Retail & Ecommerce
        self.industries_dropdown_retail_and_ecommerce_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='retail'] p" ## Text : From first click to repeat purchase, create experiences your customers will love
        self.industries_dropdown_financial_services_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='finance']" ## Text : Financial Services
        self.industries_dropdown_financial_services_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='finance'] p" ## Text : Build trust and loyalty with personalized experiences that increase engagement and retention
        self.industries_dropdown_travel_and_hospitality_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='travel']" ## Text : Travel & Hospitality
        self.industries_dropdown_travel_and_hospitality_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='travel'] p" ## Text : Inspire travelers, personalize the journey, boost bookings, and drive ancillary revenue 
        ## Dropdowns - Industries - Column 2
        self.industries_dropdown_beauty_and_cosmetics_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='beauty']" ## Text : Beauty & Cosmetics
        self.industries_dropdown_beauty_and_cosmetics_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='beauty'] p" ## Text : From skincare to self-care, engage customers with personalization, precision and style
        self.industries_dropdown_automotive_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='automotive']" ## Text : Automotive
        self.industries_dropdown_automotive_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='automotive'] p" ## Text : Connect the digital and showroom experience to accelerate engagement, leads, and retention
        self.industries_dropdown_telecommunications_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='telecom']" ## Text : Telecommunications
        self.industries_dropdown_telecommunications_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='telecom'] p" ## Text : Reduce churn, boost loyalty, and personalize for every customer
        ## Dropdowns - Resources
        ## Dropdowns - Resources - Interactive Platform Tour
        self.resources_dropdown_interactive_platform_tour = ".header-menu-item-dropdown.show [href*='product-demo-hub'].header-menu-item-dropdown-item" ## It has an image with span text "Interactive Platform Tour" and p text "Explore 80+ self-guided demos, no forms, no waiting"
        ## Dropdowns - Resources - Interactive Tools
        self.resources_dropdown_interactive_tools_title = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) .title h3" ## Text : INTERACTIVE TOOLS 
        self.resources_dropdown_whatsapp_explorer_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='whatsapp-templates']" ## Text : WhatsApp Explorer
        self.resources_dropdown_whatsapp_explorer_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='whatsapp-templates'] p" ## Text : Discover the power of WhatsApp for business
        self.resources_dropdown_sms_template_library_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='sms-templates']" ## Text : SMS Template Library
        self.resources_dropdown_sms_template_library_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='sms-templates'] p" ## Text : 60+ templates for seamless SMS marketing
        self.resources_dropdown_cdp_explorer_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='cdp-use-cases-explorer']" ## Text : CDP Explorer
        self.resources_dropdown_cdp_explorer_desc = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(2) [href*='cdp-use-cases-explorer'] p" ## Text : Learn how to put your customer data into action
        ## Dropdowns - Resources - Other Resources
        self.resources_dropdown_other_resources_title = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) .title h3" ## Text : OTHER RESOURCES
        self.resources_dropdown_case_studies_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='case-studies']" ## Text : Case Studies
        self.resources_dropdown_blog_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='blog']" ## Text : Blog
        self.resources_dropdown_ebooks_and_guides_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='ebook']" ## Text : E-Books & Guides
        self.resources_dropdown_glossary_link = ".header-menu-item-dropdown.show .header-menu-item-dropdown-item:nth-child(3) [href*='glossary']" ## Text : Glossary
        ## HOMEPAGE - Contents
        self.homepage_hero_content_title = ".homepage-hero-content .homepage-hero-content-title h1" ## Text : The leading Agentic Customer Engagement Platform
        self.homepage_hero_content_desc = ".homepage-hero-content .homepage-hero-content-description p" ## Text : Move from campaign execution to continuous AI decisioning. Unlock autonomous end-to-end engagement and become unstoppable.
        self.homepage_hero_unlock_potential_email_input = ".homepage-hero-content .homepage-hero-content-form input"
        self.homepage_hero_unlock_potential_email_label = ".homepage-hero-content .homepage-hero-content-form label p" ## Text : Unlock your peak potential
        self.homepage_hero_unlock_potential_get_a_demo_btn = ".homepage-hero-content .homepage-hero-content-form .redirect-button" ## Text : Get a demo
        self.homepage_hero_trusted_by_heading = ".homepage-hero-content .homepage-logo-reel-heading" ## Text : TRUSTED BY 2,000+ CUSTOMERS (It may have linebreaks in it)
        ### Can save 5 customers to a temp list and make sure the reel-logos does not loop over same customers again and again. UX tests, for later.
        self.homepage_hero_social_proof_wrapper_title = ".homepage-social-proof-wrapper .title.opacity-scroll.visible" ## It has 20+ customer logos in it, and it is auto-scrolling horizontally.
        ## HOMEPAGE - Capabilities ?
        self.homepage_capabilities_title = ".homepage-capabilities-head .title h2" ## Text : One platform,  every channel, infinite possibilities. (It has linebreaks in it)
        ## Capabilities - Buttons - STATIC LIST, AI, CDP, Personalization, Journey Orchestration, Reporting & Insights
        self.homepage_capabilities_ai_btn = ".homepage-capabilities-body-buttons .homepage-capabilities-body-buttons-item:nth-child(1)" ## Text : AI
        self.homepage_capabilities_cdp_btn = ".homepage-capabilities-body-buttons .homepage-capabilities-body-buttons-item:nth-child(2)" ## Text : CDP
        self.homepage_capabilities_personalization_btn = ".homepage-capabilities-body-buttons .homepage-capabilities-body-buttons-item:nth-child(3)" ## Text : Personalization
        self.homepage_capabilities_journey_orchestration_btn = ".homepage-capabilities-body-buttons .homepage-capabilities-body-buttons-item:nth-child(4)" ## Text : Journey Orchestration
        self.homepage_capabilities_reporting_and_insights_btn = ".homepage-capabilities-body-buttons .homepage-capabilities-body-buttons-item:nth-child(5)" ## Text : Reporting and Insights
        self.homepage_capabilities_active_slider_box = ".homepage-capabilities-body-slider.visible .swiper-slide-active a .slide-item-content-title span" ## Whichever button is active, this box slides to center in the main slider below. It has the same text as the button, Text : AI, CDP, Personalization, Journey Orchestration, Reporting & Insights (depending on which button is active)
        ## HOMEPAGE - One AI
        self.homepage_one_ai_title = ".homepage-insider-one-ai-head .title" ## Text : Meet Insider One AI™ The artificial intelligence that powers every one of our products (it has a shtton of line breaks)                                                                 
        self.homepage_one_ai_desc = ".homepage-insider-one-ai-head .description p" ## Text : Drive smarter, faster, more meaningful engagement powered by predictive, generative, and agentic intelligence.
        ## One AI Vertical List - UX : fluidity is non-existent if interacted. It is better to just check the presence of the list and the list items, and not interact with it. And progress bar behaves funky, 
        self.homepage_one_ai_body_agentic_ai_subtitle = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(1) .subtitle h4" ## Text : AGENTIC AI
        self.homepage_one_ai_body_agentic_ai_title = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(1) .title h3" ## Text : Autonomous agents for superior customer engagement
        self.homepage_one_ai_body_agentic_ai_description = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(1) .description p" ## Text : Agent One™ brings together purpose-built AI agents to help you deliver superior customer engagement through emotionally resonant conversations and autonomous decision-making.
        self.homepage_one_ai_body_generative_ai_subtitle = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(2) .subtitle h4" ## Text : GENERATIVE AI
        self.homepage_one_ai_body_generative_ai_title = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(2) .title h3" ## Text : Put your marketing on autopilot with Insider One AI
        self.homepage_one_ai_body_generative_ai_description = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(2) .description p" ## Text : Improve targeting precision using AI-powered predictive segments in real time to boost the relevance of every interaction
        self.homepage_one_ai_body_predictive_ai_subtitle = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(3) .subtitle h4" ## Text : PREDICTIVE AI
        self.homepage_one_ai_body_predictive_ai_title = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(3) .title h3" ## Text : Maximize impact with AI-powered precision
        self.homepage_one_ai_body_predictive_ai_description = ".homepage-insider-one-ai-body .homepage-insider-one-ai-body-content .homepage-insider-one-ai-body-content-item:nth-child(3) .description p" ## Text : Combine data from online and offline sources, like your CRM, POS, and contact centers, to segment users based on real-time events and rule-based triggers.
        ## HOMEPAGE - Channels
        self.homepage_channels_title = ".homepage-channels-head .title" ## Text : Unmatched channel breadth  for unstoppable reach (It has linebreaks in it)
        self.homepage_channels_desc = ".homepage-channels-head .description p" ## Text : From SMS to WhatsApp, Email to Search, engage your customers wherever and however they choose.
        self.homepage_channels_sms_and_rcs_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(1) .swiper-slide:nth-child(1) .slide-item-title" ## Text : SMS and RCS
        self.homepage_channels_email_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(2) .swiper-slide:nth-child(1) .slide-item-title" ## Text : Email
        self.homepage_channels_whatsapp_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(3) .swiper-slide:nth-child(1) .slide-item-title" ## Text : WhatsApp
        self.homepage_channels_web_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(1) .swiper-slide:nth-child(2) .slide-item-title" ## Text : Web
        self.homepage_channels_mobile_app_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(2) .swiper-slide:nth-child(2) .slide-item-title" ## Text : Mobile App
        self.homepage_channels_push_notifications_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(3) .swiper-slide:nth-child(2) .slide-item-title" ## Text : Push Notifications
        self.homepage_channels_site_search_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(1) .swiper-slide:nth-child(3) .slide-item-title" ## Text : Site Search
        self.homepage_channels_instory_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(2) .swiper-slide:nth-child(3) .slide-item-title" ## Text : InStory
        self.homepage_channels_conversational_cx_title = ".homepage-channels-body .homepage-channels-body-slider .slide-col:nth-child(3) .swiper-slide:nth-child(3) .slide-item-title" ## Text : Conversational CX

        ## Cookie Inform Dialog
        self.cookie_inform_dialog_box = "#cookie-law-info-bar.wt-cli-cookie-bar"
        self.cookie_inform_dialog_accept_all_btn = "#cookie-law-info-bar.wt-cli-cookie-bar #wt-cli-accept-all-btn"
        self.cookie_inform_dialog_only_necessary_btn = "#cookie-law-info-bar.wt-cli-cookie-bar #wt-cli-accept-btn"
        self.cookie_inform_dialog_decline_all_btn = "#cookie-law-info-bar.wt-cli-cookie-bar #wt-cli-reject-btn"

    def navigate(self):
        """Navigates to the homepage."""
        self.page.goto(self.url)

    def verify_page_loaded(self):
        """Quick readiness check before running full homepage assertions."""
        self.verify_element(self.page_complete_section)
        self.verify_element(self.header_top_menu)
        self.verify_element(self.header_menu_list)
        self.verify_element(self.homepage_hero_content_title)

    def verify_homepage_all_sections(self):
        """Centralized full homepage verification that calls grouped assertion blocks."""
        self._verify_general_and_top_menu_sections()
        self._verify_platform_dropdown_sections()
        self._verify_industries_dropdown_sections()
        self._verify_resources_dropdown_sections()
        ## Hover keeps the dropdown open, after this point there are no more dropdowns, so lets move the mouse away to avoid any hover related issues in the next assertions.
        self.page.mouse.move(0, 0)
        self._verify_homepage_content_sections()
        self._verify_homepage_capabilities_sections()
        self._verify_homepage_one_ai_sections()
        self._verify_homepage_channels_sections()
        self._verify_cookie_dialog_section()

    def _scroll_to_element(self, locator_string):
        """Scrolls an element into view before assertions."""
        self.page.locator(locator_string).scroll_into_view_if_needed()

    def _verify_general_and_top_menu_sections(self):
        # HOMEPAGE - General
        self.verify_element(self.page_complete_section, apply_bg=False) ## This is a big section, applying background color on it causes more harm than good for visual debugging, so skipping it here.

        # HOMEPAGE - Top most Menu
        self.verify_element(self.header_top_menu, apply_bg=False)
        self.verify_element(self.header_top_menu_actions, apply_bg=False)

        # HOMEPAGE - Top Menu
        self.verify_element(self.header_logo_img)
        self.verify_element(self.header_menu_list)
        self.verify_element(self.header_menu_platform_btn, "Platform")
        self.verify_element(self.header_menu_industries_btn, "Industries")
        self.verify_element(self.header_menu_customers_btn, "Customers")
        self.verify_element(self.header_menu_resources_btn, "Resources")
        self.verify_element(self.header_menu_platform_tour_btn)
        self.verify_element(self.header_menu_get_a_demo_btn)

    def _verify_platform_dropdown_sections(self):
        # Open Platform dropdown before verifying its content.
        self.page.locator(self.header_menu_platform_btn).hover()
        self.verify_element(self.header_menu_dropdown_general, apply_bg=False)

        # Dropdowns - Platform
        self.verify_element(self.platform_dropdown_platform_overview_link)
        self.verify_element(self.platform_dropdown_platform_overview_desc, "Explore Insider One, everything you need, nothing you don’t, all in one place")
        self.verify_element(self.platform_dropdown_integration_hub_link)
        self.verify_element(self.platform_dropdown_integration_hub_desc)

        # Dropdowns - Platform - Capabilities
        self.verify_element(self.platform_dropdown_capabilities_title, "CAPABILITIES")
        self.verify_element(self.platform_dropdown_capabilities_insider_one_ai, "Insider One AI™")
        self.verify_element(self.platform_dropdown_capabilities_customer_data_management, "Customer Data Management")
        self.verify_element(self.platform_dropdown_capabilities_personalization, "Personalization")
        self.verify_element(self.platform_dropdown_capabilities_journey_orchestration, "Journey Orchestration")
        self.verify_element(self.platform_dropdown_capabilities_reporting_and_data, "Reporting & Data")
        self.verify_element(self.platform_dropdown_capabilities_behavioral_analytics, "Behavioral Analytics")

        # Dropdowns - Platform - Channels
        self.verify_element(self.platform_dropdown_channels_title, "CHANNELS")
        self.verify_element(self.platform_dropdown_channels_web, "Web")
        self.verify_element(self.platform_dropdown_channels_email, "Email")
        self.verify_element(self.platform_dropdown_channels_site_search, "Site Search")
        self.verify_element(self.platform_dropdown_channels_conversational_cx, "Conversational CX")
        self.verify_element(self.platform_dropdown_channels_whatsapp, "WhatsApp")
        self.verify_element(self.platform_dropdown_channels_web_push, "Web Push")
        self.verify_element(self.platform_dropdown_channels_instory, "InStory")
        self.verify_element(self.platform_dropdown_channels_app, "App")
        self.verify_element(self.platform_dropdown_channels_sms_and_rcs, "SMS & RCS")

        # Dropdowns - Platform - Why Insider One
        self.verify_element(self.platform_dropdown_why_insider_one_title, "WHY INSIDER ONE")
        self.verify_element(self.platform_dropdown_why_insider_one_join_migration_movement, "Join the $0 Migration Movement™")
        self.verify_element(self.platform_dropdown_why_insider_one_join_migration_movement_desc, "Migration without fear, lock‑in, or hidden costs.")
        self.verify_element(self.platform_dropdown_why_insider_one_the_insider_one_difference, "The Insider One Difference")
        self.verify_element(self.platform_dropdown_why_insider_one_the_insider_one_difference_desc, "Discover what makes us different")
        self.verify_element(self.platform_dropdown_why_insider_one_compare_vendors, "Compare Vendors")
        self.verify_element(self.platform_dropdown_why_insider_one_compare_vendors_desc, "Find out how we compare to other industry players")
        self.verify_element(self.platform_dropdown_why_insider_one_switch_to_insider_one, "Switch to Insider One")
        self.verify_element(self.platform_dropdown_why_insider_one_switch_to_insider_one_desc, "Discover why world’s best-loved brands choose Insider One")

    def _verify_industries_dropdown_sections(self):
        # Open Industries dropdown before verifying its content.
        self.page.locator(self.header_menu_industries_btn).hover()
        self.verify_element(self.header_menu_dropdown_general, apply_bg=False)

        # Dropdowns - Industries - Success Story Box
        self.verify_element(self.industries_dropdown_success_story_box)

        # Dropdowns - Industries - Column 1
        self.verify_element(self.industries_dropdown_retail_and_ecommerce_link, "Retail & Ecommerce")
        self.verify_element(self.industries_dropdown_retail_and_ecommerce_desc, "From first click to repeat purchase, create experiences your customers will love")
        self.verify_element(self.industries_dropdown_financial_services_link, "Financial Services")
        self.verify_element(self.industries_dropdown_financial_services_desc, "Build trust and loyalty with personalized experiences that increase engagement and retention")
        self.verify_element(self.industries_dropdown_travel_and_hospitality_link, "Travel & Hospitality")
        self.verify_element(self.industries_dropdown_travel_and_hospitality_desc, "Inspire travelers, personalize the journey, boost bookings, and drive ancillary revenue")

        # Dropdowns - Industries - Column 2
        self.verify_element(self.industries_dropdown_beauty_and_cosmetics_link, "Beauty & Cosmetics")
        self.verify_element(self.industries_dropdown_beauty_and_cosmetics_desc, "From skincare to self-care, engage customers with personalization, precision and style")
        self.verify_element(self.industries_dropdown_automotive_link, "Automotive")
        self.verify_element(self.industries_dropdown_automotive_desc, "Connect the digital and showroom experience to accelerate engagement, leads, and retention")
        self.verify_element(self.industries_dropdown_telecommunications_link, "Telecommunications")
        self.verify_element(self.industries_dropdown_telecommunications_desc, "Reduce churn, boost loyalty, and personalize for every customer")

    def _verify_resources_dropdown_sections(self):
        # Open Resources dropdown before verifying its content.
        self.page.locator(self.header_menu_resources_btn).hover()
        self.verify_element(self.header_menu_dropdown_general, apply_bg=False)

        # Dropdowns - Resources - Interactive Platform Tour
        self.verify_element(self.resources_dropdown_interactive_platform_tour, "Interactive Platform Tour")

        # Dropdowns - Resources - Interactive Tools
        self.verify_element(self.resources_dropdown_interactive_tools_title, "INTERACTIVE TOOLS")
        self.verify_element(self.resources_dropdown_whatsapp_explorer_link, "WhatsApp Explorer")
        self.verify_element(self.resources_dropdown_whatsapp_explorer_desc, "Discover the power of WhatsApp for business")
        self.verify_element(self.resources_dropdown_sms_template_library_link, "SMS Template Library")
        self.verify_element(self.resources_dropdown_sms_template_library_desc, "60+ templates for seamless SMS marketing")
        self.verify_element(self.resources_dropdown_cdp_explorer_link, "CDP Explorer")
        self.verify_element(self.resources_dropdown_cdp_explorer_desc, "Learn how to put your customer data into action")

        # Dropdowns - Resources - Other Resources
        self.verify_element(self.resources_dropdown_other_resources_title, "OTHER RESOURCES")
        self.verify_element(self.resources_dropdown_case_studies_link, "Case Studies")
        self.verify_element(self.resources_dropdown_blog_link, "Blog")
        self.verify_element(self.resources_dropdown_ebooks_and_guides_link, "E-Books & Guides")
        self.verify_element(self.resources_dropdown_glossary_link, "Glossary")

    def _verify_homepage_content_sections(self):
        # HOMEPAGE - Contents
        self.verify_element(self.homepage_hero_content_title, "The leading Agentic Customer Engagement Platform")
        self.verify_element(self.homepage_hero_content_desc, "Move from campaign execution to continuous AI decisioning. Unlock autonomous end-to-end engagement and become unstoppable.")
        self.verify_element(self.homepage_hero_unlock_potential_email_input)
        self.verify_element(self.homepage_hero_unlock_potential_email_label, "Unlock your peak potential")
        self.verify_element(self.homepage_hero_unlock_potential_get_a_demo_btn, "Get a demo")
        self.verify_element(self.homepage_hero_trusted_by_heading, "TRUSTED BY 2,000+ CUSTOMERS")
        self.verify_element(self.homepage_hero_social_proof_wrapper_title)

    def _verify_homepage_capabilities_sections(self):
        # Scroll to capabilities section before verifying its content.
        self._scroll_to_element(self.homepage_capabilities_title)

        # HOMEPAGE - Capabilities
        self.verify_element(self.homepage_capabilities_title, "One platform")
        self.verify_element(self.homepage_capabilities_ai_btn, "AI")
        self.verify_element(self.homepage_capabilities_cdp_btn, "CDP")
        self.verify_element(self.homepage_capabilities_personalization_btn, "Personalization")
        self.verify_element(self.homepage_capabilities_journey_orchestration_btn, "Journey Orchestration")
        self.verify_element(self.homepage_capabilities_reporting_and_insights_btn, "Reporting and Insights")
        self.verify_element(self.homepage_capabilities_active_slider_box)

    def _verify_homepage_one_ai_sections(self):
        # Scroll to One AI section before verifying its content.
        self._scroll_to_element(self.homepage_one_ai_title)

        # HOMEPAGE - One AI
        self.verify_element(self.homepage_one_ai_title, "Meet Insider One AI™")
        self.verify_element(self.homepage_one_ai_desc, "Drive smarter, faster, more meaningful engagement powered by predictive, generative, and agentic intelligence.")
        self.verify_element(self.homepage_one_ai_body_agentic_ai_subtitle, "AGENTIC AI")
        self.verify_element(self.homepage_one_ai_body_agentic_ai_title, "Autonomous agents for superior customer engagement")
        self.verify_element(self.homepage_one_ai_body_agentic_ai_description, "Agent One™ brings together purpose-built AI agents to help you deliver superior customer engagement through emotionally resonant conversations and autonomous decision-making.")
        self.verify_element(self.homepage_one_ai_body_generative_ai_subtitle, "GENERATIVE AI")
        self.verify_element(self.homepage_one_ai_body_generative_ai_title, "Put your marketing on autopilot with Insider One AI")
        self.verify_element(self.homepage_one_ai_body_generative_ai_description, "Improve targeting precision using AI-powered predictive segments in real time to boost the relevance of every interaction")
        self.verify_element(self.homepage_one_ai_body_predictive_ai_subtitle, "PREDICTIVE AI")
        self.verify_element(self.homepage_one_ai_body_predictive_ai_title, "Maximize impact with AI-powered precision")
        self.verify_element(self.homepage_one_ai_body_predictive_ai_description, "Combine data from online and offline sources, like your CRM, POS, and contact centers, to segment users based on real-time events and rule-based triggers.")

    def _verify_homepage_channels_sections(self):
        # Scroll to Channels section before verifying its content.
        self._scroll_to_element(self.homepage_channels_title)

        # HOMEPAGE - Channels
        self.verify_element(self.homepage_channels_title, "Unmatched channel breadth")
        self.verify_element(self.homepage_channels_desc, "From SMS to WhatsApp, Email to Search, engage your customers wherever and however they choose.")
        self.verify_element(self.homepage_channels_sms_and_rcs_title, "SMS and RCS")
        self.verify_element(self.homepage_channels_email_title, "Email")
        self.verify_element(self.homepage_channels_whatsapp_title, "WhatsApp")
        self.verify_element(self.homepage_channels_web_title, "Web")
        self.verify_element(self.homepage_channels_mobile_app_title, "Mobile App")
        self.verify_element(self.homepage_channels_push_notifications_title, "Push Notifications")
        self.verify_element(self.homepage_channels_site_search_title, "Site Search")
        self.verify_element(self.homepage_channels_instory_title, "InStory")
        self.verify_element(self.homepage_channels_conversational_cx_title, "Conversational CX")

    def _verify_cookie_dialog_section(self):
        # Cookie Inform Dialog
        self.verify_element(self.cookie_inform_dialog_box)
        self.verify_element(self.cookie_inform_dialog_accept_all_btn)
        self.verify_element(self.cookie_inform_dialog_only_necessary_btn)
        self.verify_element(self.cookie_inform_dialog_decline_all_btn)