from .base_page import BasePage
from .locators import ProjectsPageLocators, MainPageLocators
import random


class ProjectsPage(BasePage):
	tags_areas = {
		"Industry": 0,
		"Expertise": 1,
		"Technologies": 2
	}

	def pick_random_tag(self, amount=1, area=random.choice([*tags_areas.keys()])) -> list[
		str]:  # if no area has been passed - random one is picked
		chosen_tags = []
		for n in range(amount):
			tag_area = self.tags_areas[area]
			self.wait_for_elements(*ProjectsPageLocators.TAG_DROPDOWNS_LOCATOR)[
				tag_area].click()  # click on dropdown to show it
			tag = self.pick_random_element(*ProjectsPageLocators.LIST_OF_TAGS_IN_DROPDOWN_LOCATOR)
			chosen_tags.append(tag.text.casefold())
			tag.click()  # click on random tag
			self.wait_for_elements(*ProjectsPageLocators.TAG_DROPDOWNS_LOCATOR)[
				tag_area].click()  # click on dropdown to hide it
		return chosen_tags

	def deselect_tag(self):
		self.wait_for_element_and_click(*ProjectsPageLocators.TAGS_LOCATOR)
		self.wait_for_element_to_disappear(*ProjectsPageLocators.TAGS_LOCATOR)

	def clear_all_tags(self):
		self.wait_for_element_and_click(*ProjectsPageLocators.CLEAR_ALL_BUTTON_LOCATOR)
		self.wait_for_element_to_disappear(*ProjectsPageLocators.CLEAR_ALL_BUTTON_LOCATOR)
		self.wait_for_element_to_disappear(*ProjectsPageLocators.TAGS_LOCATOR)

	def pick_random_project(self, is_related=False) -> str:
		if is_related:
			project = self.pick_random_element(*ProjectsPageLocators.PROJECT_RELATED_PROJECTS_GRID_LOCATOR)
		else:
			project = self.pick_random_element(*ProjectsPageLocators.PROJECTS_GRID_LOCATOR)
		outer_text = project.get_property("outerText")
		if outer_text.find('\n')!= -1:
			project_name = outer_text[:outer_text.find('\n')]  # remove subtitle after \n if there is one
		else:
			project_name = outer_text
		if project_name[-3:] == "...":  # remove "..." in long project names in the end
			project_name = project_name[:-3]
		project.click()
		return project_name

	def compare_project_names(self, expected_project_name):
		project_name = self.wait_for_element(*ProjectsPageLocators.PROJECT_NAME_HEADING_LOCATOR).text
		self.logger.info(f'project name = {project_name}')
		self.logger.info(f' expected_name = {expected_project_name}')
		if project_name != expected_project_name and project_name.find(expected_project_name) == -1:
			raise AssertionError("Expected project name and current project doesnt match")


	#TODO load more loads additional projects