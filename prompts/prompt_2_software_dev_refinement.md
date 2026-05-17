# AI Collaboration Iteration 2: Software Development Test Refinement

**Goal:** Refine the AI-generated "Software Development" test to add a missing location filter step, remove hallucinated DOM elements, remove flaky string assertions, and add the missing Lever redirect validation.

**Context provided:** After reviewing Iteration 1, I realized the AI missed a crucial logical step: it did not filter the job list by location prior to verifying the job cards. Furthermore, the AI hallucinated a "department" field inside the job card that does not exist in the live DOM, and I recognized that "Software Development" titles are too varied to safely assert without creating test flakiness. I reverted the code and engineered a secondary prompt to enforce the correct test flow and strip out the AI's hallucinations.

**Prompt:** 
    Goal: Refine the "Software Development" test scenario to correctly filter by location, remove hallucinated DOM elements, remove flaky string assertions, and add the missing Lever redirect validation.

    Context: The previous AI generation missed the crucial step of filtering the jobs by location ("Istanbul, Turkey") before verifying the list. It also hallucinated a job_item_position_department locator. Finally, "Software Development" position names are too varied to reliably assert with a simple string check.

    Task 1: Update CareersPage (careers_page.py)

        Ensure locators exist in __init__ for the Location filter dropdown and the "Istanbul, Turkey" dropdown option.

        Update the filter_software_development_jobs method (or create a new filter_by_location method) to interact with the location dropdown and select "Istanbul, Turkey". Use our custom self.scroll_to_and_highlight() method before clicking.

        Update verify_software_engineering_jobs_details: Remove the department and position assertions entirely. Keep the loop, but assert ONLY that the job card's location contains "Istanbul, Turkey" using self.verify_element(location, "Istanbul, Turkey").

    Task 2: Update TestCareersFlow (test_careers.py)

        Ensure the test logic flows correctly: Navigate -> Filter by Team -> Filter by Location -> Check List Presence -> Verify Details.

        After the details verification, add a step to call our existing careers_page.click_apply_and_verify_redirect() method to ensure the first job card redirects to Lever.

    Constraints: Maintain the FRAMEWORK_RULES.md and only use the existing BasePage methods.

**Output evaluation:** - **Accepted:** I accepted the addition of the location filtering logic and the Lever redirect step. I also accepted the removal of the department and position assertions, stripping the loop down to strictly validate the "Istanbul, Turkey" location. 
- **Rejected:** I have fixed the location filtering setting manually because both AI and assesment file mentions Istanbul, Turkey but lever lists as "Istanbul, Turkiye". I also copied and stripped click_apply_and_verify_redirect_without_posting_content method because job postings does not have the same structure apparently. 

**Iteration notes:** This iteration and the test itself perfectly highlights the limitations of LLM coding assistants. AI is often focused on the *code syntax* rather than the *business logic* of a test case. It hallucinated a DOM element because it lacked live DOM access, and it also had no idea about filtering beforehand to make sure assertions in the loop would hit. Creating the prompts via Reasoning LLM before feeding it to an LLM and a human-in-the-loop is strictly required to review the logical flow of the generated test and cross-reference the live DOM to ensure the test is both accurate and robust.