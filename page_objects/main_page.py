from .base_page import BasePage
from .locators import ProjectsPageLocators, MainPageLocators


class MainPage(BasePage):

	def navigate_to_projects_via_expertises(self, locator):
		expected_tag = self.navigate_to_projects(locator)
		self.check_tag(expected_tag)

	def navigate_to_projects_via_industries(self, locator):
		expected_tag = self.navigate_to_projects(locator)
		self.wait_for_element_and_click(*MainPageLocators.INDUSTRY_PROJECTS_LINK)
		self.check_tag(expected_tag)

	def navigate_to_projects(self, locator) -> list[str]:
		navigation_button = self.wait_for_element(*locator)
		outer_text = navigation_button.get_property("outerText")
		expected_tag = outer_text[:outer_text.find('\n')]
		if expected_tag == "CAD/CAM and BIM":  # kludge for this tag coz button and tag have different names
			expected_tag = expected_tag.replace(" and ", "/")
		self.wait_for_element_and_click(*locator)
		return [expected_tag.casefold()] #since check_tag method compares lists



	def check_button_name(self, locator, expected_text):
		expertise_link = self.wait_for_element(*locator)
		outer_text = expertise_link.get_property("outerText")
		expertise_text = outer_text[:outer_text.find('\n')]
		assert expertise_text == expected_text, f'Button text = {expertise_text} doesnt match with {expected_text}'

	def click_contact_us_button(self):
		self.wait_for_element_and_click(*MainPageLocators.MAIN_CONTACT_US_BUTTON)
		self.check_element_in_view(MainPageLocators.CONTACT_US_FORM_FIRST_FIELD)


	def click_navigation_button(self, locator, expected_url):
		self.wait_for_element_and_click(*locator)
		self.wait_for_ulr_change(expected_url)
