# AI Collaboration Iteration 1: Software Engineering Scenario

**Goal:** Generate an additional UI test scenario to verify "Software Engineering" job listings, utilizing the existing Page Object Model to demonstrate framework scalability and code reusability.

**Context provided:** I utilized a Meta-Prompting/Chained AI approach. I used a reasoning LLM (Gemini) to architect a strict, context-rich prompt that adhered to my `FRAMEWORK_RULES.md`. I then fed this engineered prompt, along with the active workspace context (`careers_page.py` and `test_careers.py`), to GitHub Copilot. For reasoning LLM, I just explained that there is a similar flow for Software Development just like what I have created with Quality Assurance and I would like Copilot to mimic the behavior, adhere to the rules and follow best-practices if possible. 

**Prompt:**
    Goal: I need to add a second UI test scenario to verify "Software Engineering" job listings, proving the reusability of our POM architecture.

    Context: > We are using Python, Pytest, and Playwright with a strict Page Object Model. You can see the existing structure in src/pages/careers_page.py and tests/ui/test_careers.py.

    Task 1: Update CareersPage

        Add new locators in __init__ for the "Software Engineering" team filter (similar to qa_team_link).

        Create a new method filter_software_engineering_jobs(self) that clicks "See all teams" and then clicks the Software Engineering filter. Use our custom self.scroll_to_and_highlight() method before clicking.

        Create a new method verify_software_engineering_jobs_details(self). It should loop through the job_item locators. Inside the loop, assert that the Department contains "Software Engineering". (Do not check location or title for this specific test, just the department).

    Task 2: Update TestCareersFlow
    Add a new test method test_software_engineering_jobs_filtering(self, page_context) in test_careers.py that navigates to the page, filters for Software Engineering, verifies the list is present, and verifies the job details.

    Constraints:

        Strictly follow the rules in FRAMEWORK_RULES.md.

        Only use Playwright's expect module.

        Do not alter the existing QA test methods.



**Output evaluation:** - **Accepted:** I accepted the modification of `careers_page.py` file and `test_careers.py` file because the `test_software_development_jobs_filtering` test was created in the same manner of the test I manually created and followed the same principles without any underlying issues.  It successfully created locators inside `careers_page.py` as well. 
**Refinement Note:** After accepting the initial code, I ran the test to validate the output. The AI understandably hallucinated the exact DOM locator for the job listing assertions.

**Iteration notes:** The zero-shot prompt with strict constraints was highly effective because the framework architecture was already firmly established. Framework-wide rules and a creating locators in a systematic manner increase the effectiveness of AI usage in the codebase recognizably. 