from page_objects.projects_page import ProjectsPage
import allure
import pytest
from page_objects.locators import MainPageLocators, ProjectsPageLocators, AboutUsLocators, NewsLocators
import time

@allure.title("Test can pick tags from dropdown")
@pytest.mark.parametrize("tags_area", ["Industry", "Expertise","Technologies"],
                         ids=["Industry", "Expertise", "Technologies"])
def test_can_pick_tags_from_dropdown(browser, url, tags_area):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	page.pick_random_tag(tags_area)


@allure.title("Test can deselect tags by  clicking")
def test_can_clear_tags_by_clicking(browser, url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	page.pick_random_tag()
	page.deselect_tag()

@pytest.mark.debug
@allure.title("Test can deselect tags by clear all")
def test_can_deselect_tags_by_clear_all(browser, url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	for i in range(3): #choosing 3 random tags
		page.pick_random_tag()
	page.clear_all_tags()