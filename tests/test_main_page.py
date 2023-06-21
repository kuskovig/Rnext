from page_objects.main_page import MainPage
import allure
import pytest
from page_objects.locators import MainPageLocators, ProjectsPageLocators, AboutUsLocators, NewsLocators


@allure.title("Test user can navigate via expertise buttons")
@pytest.mark.parametrize("expertise_links", [MainPageLocators.EXPERTISES_LINKS_DICT["ENTERPRISE"],
                                             MainPageLocators.EXPERTISES_LINKS_DICT["CADCAMBIM"],
                                             MainPageLocators.EXPERTISES_LINKS_DICT["AI"],
                                             MainPageLocators.EXPERTISES_LINKS_DICT["VR/AR"]],
                         ids=["Expertise", "CAD/CAM/BIM", "AI", "VR/AR"])
def test_expertise_buttons_do_navigate(browser, url, expertise_links):
	page = MainPage(browser, url)
	page.open()
	page.navigate_to_projects_via_expertises(expertise_links)


@allure.title("Test buttons have correct names")
@pytest.mark.parametrize("expertise_links, expected_text",
                         [(MainPageLocators.EXPERTISES_LINKS_DICT["ENTERPRISE"], "Enterprise software"),
                          (MainPageLocators.EXPERTISES_LINKS_DICT["CADCAMBIM"], "CAD/CAM and BIM"),
                          (MainPageLocators.EXPERTISES_LINKS_DICT["AI"], "Artificial intelligence"),
                          (MainPageLocators.EXPERTISES_LINKS_DICT["VR/AR"], "VR/AR")],
                         ids=["Expertise", "CAD/CAM/BIM", "AI", "VR/AR"])
def test_buttons_have_correct_names(browser, url, expertise_links, expected_text):
	page = MainPage(browser, url)
	page.open()
	page.check_button_name(expertise_links, expected_text)


@allure.title("Test user can navigate via industries buttons")
@pytest.mark.parametrize("industry_links", [MainPageLocators.INDUSTRIES_LINKS_DICT["Manufacturing"],
                                            MainPageLocators.INDUSTRIES_LINKS_DICT["Construction"],
                                            MainPageLocators.INDUSTRIES_LINKS_DICT["Oil_and_gas"],
                                            MainPageLocators.INDUSTRIES_LINKS_DICT["Retail"],
                                            MainPageLocators.INDUSTRIES_LINKS_DICT["Logistics"],
                                            MainPageLocators.INDUSTRIES_LINKS_DICT["Education"]],
                         ids=["Manufacturing", "Construction", "Oil_and_gas", "Retail", "Logistics", "Education"])
def test_industries_links_do_navigate(browser, url, industry_links):
	page = MainPage(browser, url)
	page.open()
	page.navigate_to_projects_via_industries(industry_links)



@allure.title("Contact us scrolls to form")
def test_contact_us_scrolls_to_form(browser, url):
	page = MainPage(browser, url)
	page.open()
	page.click_contact_us_button()



@allure.title("More projects lead to projects page")
def test_more_projects_button_navigate_to_projects(browser, url):
	page = MainPage(browser, url)
	page.open()
	page.click_navigation_button(MainPageLocators.MORE_PROJECTS_LINK, ProjectsPageLocators.PROJECTS_PAGE_URL)


@allure.title("More projects lead to projects page")
def test_see_more_button_navigate_to_projects(browser, url):
	page = MainPage(browser, url)
	page.open()
	page.click_navigation_button(MainPageLocators.SEE_MORE_BUTTON, ProjectsPageLocators.PROJECTS_PAGE_URL)

@allure.title("About Us lead to About page")
def test_about_us_navigates_to_about(browser, url):
	page = MainPage(browser, url)
	page.open()
	page.click_navigation_button(MainPageLocators.ABOUT_US_BUTTON, AboutUsLocators.ABOUT_US_PAGE_URL)


@allure.title("More news lead to News page")
def test_more_news_navigates_to_news(browser, url):
	page = MainPage(browser, url)
	page.open()
	page.click_navigation_button(MainPageLocators.MORE_NEWS_BUTTON, NewsLocators.NEWS_PAGE_URL)


