from .base_page import BasePage
from .locators import ProjectsPageLocators, MainPageLocators
import random

class ProjectsPage(BasePage):
	tags_areas = {
		"Industry":0,
		"Expertise": 1,
		"Technologies": 2
		}

	def pick_random_tag(self, area=random.choice([*tags_areas.keys()])): #if no area has been passed - random one is picked
		tag_area = self.tags_areas[area]
		self.wait_for_elements(*ProjectsPageLocators.TAG_DROPDOWNS_LOCATOR)[tag_area].click() #click on dropdown to show it
		tag = self.pick_random_element(*ProjectsPageLocators.LIST_OF_TAGS_IN_DROPDOWN_LOCATOR)
		tag_text = tag.text
		tag.click()#click on random tag
		self.wait_for_elements(*ProjectsPageLocators.TAG_DROPDOWNS_LOCATOR)[tag_area].click() #click on dropdown to hide it
		self.check_tag(tag_text)


	def deselect_tag(self):
		self.wait_for_element_and_click(*ProjectsPageLocators.TAGS_LOCATOR)
		self.wait_for_element_to_disappear(*ProjectsPageLocators.TAGS_LOCATOR)

	def clear_all_tags(self):
		self.wait_for_element_and_click(*ProjectsPageLocators.CLEAR_ALL_BUTTON_LOCATOR)
		self.wait_for_element_to_disappear(*ProjectsPageLocators.CLEAR_ALL_BUTTON_LOCATOR)
		self.wait_for_element_to_disappear(*ProjectsPageLocators.TAGS_LOCATOR)
