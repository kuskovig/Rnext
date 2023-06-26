from page_objects.projects_page import ProjectsPage
from page_objects.locators import ProjectsPageLocators
import allure
import pytest
import time



@allure.title("Test can pick tags from dropdown")
@pytest.mark.parametrize("tags_area", ["Industry", "Expertise", "Technologies"],
						 ids=["Industry", "Expertise", "Technologies"])
def test_can_pick_tags_from_dropdown(browser, url, tags_area):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	page.pick_random_tag(area=tags_area)


@allure.title("Test can deselect tags by  clicking")
def test_can_clear_tags_by_clicking(browser, url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	tags = page.pick_random_tag()
	page.check_tag(tags)
	page.deselect_tag()

@allure.title("Test can deselect tags by clear all")
def test_can_deselect_tags_by_clear_all(browser, url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	tags = page.pick_random_tag(amount = 3)
	page.check_tag(tags)
	page.clear_all_tags()


@allure.title("Test can navigate to project via project card from projects page")
def test_can_navigate_to_project(browser, url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	project_name = page.pick_random_project()
	page.compare_project_names(project_name)

@pytest.mark.xfail #many projects do not have related projects yet
@pytest.mark.debug
@allure.title("Test can navigate to related projects from project(case) page")
def test_can_navigate_to_related_project(browser,url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	project_name = page.pick_random_project() #open random project
	page.compare_project_names(project_name) #check that project is opened
	project_name = page.pick_random_project(is_related=True) #open random related project from this porject page
	page.compare_project_names(project_name)

@allure.title("Test tags are preserved after coming back from project page")
def test_navigate_back_from_project_preserve_tags(browser, url):
	page = ProjectsPage(browser, url)
	page.open("/projects")
	tags = page.pick_random_tag(amount = 3)
	page.check_tag(tags)
	project_name = page.pick_random_project()
	page.compare_project_names(project_name)
	page.wait_for_element_and_click(*ProjectsPageLocators.PROJECT_BACK_BUTTON_LOCATOR) #click back button
	page.check_tag(tags)
