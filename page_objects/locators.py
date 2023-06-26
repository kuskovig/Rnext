from selenium.webdriver.common.by import By


class HeaderLocators:
	FEATURES_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(1)")
	SOLUTIONS_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(2)")
	RESOURCES_DROPDOWN = (By.CSS_SELECTOR, ".page-header__navigation--desktop ul li:nth-child(3)")
	DROPDOWN_LINKS = (By.CSS_SELECTOR, "dropdown a")
	GO_TO_APP_BUTTON = (By.CSS_SELECTOR, "header app-button")


class MainPageLocators:
	MAIN_CONTACT_US_BUTTON = (By.CSS_SELECTOR, ".main-summary__content button")
	CONTACT_US_FORM_FIRST_FIELD = (By.CSS_SELECTOR, "app-project-form mat-form-field:nth-child(1)")

	EXPERTISES_LINKS_DICT = {"ENTERPRISE": (By.CSS_SELECTOR, "a.skills__card:nth-child(1)"),
							 "CADCAMBIM": (By.CSS_SELECTOR, "a.skills__card:nth-child(2)"),
							 "AI": (By.CSS_SELECTOR, "a.skills__card:nth-child(3)"),
							 "VR/AR": (By.CSS_SELECTOR, "a.skills__card:nth-child(4)")}

	INDUSTRIES_LINKS_DICT = {"Manufacturing": (By.CSS_SELECTOR, "app-industries .industry:nth-child(1)"),
							 "Construction": (By.CSS_SELECTOR, "app-industries .industry:nth-child(2)"),
							 "Oil_and_gas": (By.CSS_SELECTOR, "app-industries .industry:nth-child(3)"),
							 "Retail": (By.CSS_SELECTOR, "app-industries .industry:nth-child(4)"),
							 "Logistics": (By.CSS_SELECTOR, "app-industries .industry:nth-child(5)"),
							 "Education": (By.CSS_SELECTOR, "app-industries .industry:nth-child(6)")}


	INDUSTRY_PROJECTS_LINK = (By.CSS_SELECTOR, "app-industries a")

	MORE_PROJECTS_LINK = (By.CSS_SELECTOR, "a.projects-nav__more")
	SEE_MORE_BUTTON = (By.CSS_SELECTOR, ".projects~.projects-content button")

	INDUSTRIES_LINKS = (By.CSS_SELECTOR, "app-industries .industry")
	ABOUT_US_BUTTON = (By.CSS_SELECTOR, "app-rubius-team app-button")
	MORE_NEWS_BUTTON = (By.CSS_SELECTOR, "app-news-main app-button")


class ProjectsPageLocators:
	PROJECTS_PAGE_URL = "https://rubius.com/projects"
	TAGS_LOCATOR = (By.CSS_SELECTOR, ".projects-page__tags app-filter-tag:not(.projects-page__tags-clear)")
	TAG_DROPDOWNS_LOCATOR = (By.CSS_SELECTOR, ".projects-page__categories app-dropdown") #All 3 dropdowns
	LIST_OF_TAGS_IN_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, ".projects-page__categories app-dropdown .ng-option:not(.ng-option-selected)") #all available tags
	CLEAR_ALL_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".projects-page__tags app-filter-tag.projects-page__tags-clear")
	PROJECTS_GRID_LOCATOR = (By.CSS_SELECTOR, ".projects-page__projects app-project") #all projects currently visible on a page
	MORE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "app-projects .projects-page__more button")
	PROJECT_NAME_HEADING_LOCATOR = (By.CSS_SELECTOR, "app-summary h1")
	PROJECT_RELATED_PROJECTS_GRID_LOCATOR = (By.CSS_SELECTOR, "app-cards app-project") #all 2 related projects on project page
	PROJECT_BACK_BUTTON_LOCATOR = (By.CSS_SELECTOR, "app-summary button")


class AboutUsLocators:
	ABOUT_US_PAGE_URL = "https://rubius.com/company/about"

class NewsLocators:
	NEWS_PAGE_URL = "https://rubius.com/company/news"