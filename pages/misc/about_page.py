from pages.base_page import BasePage
from config.config import Config

class AboutPage(BasePage):

    # locators for about page
    heading = "h1"
    welcome_text = "h2:has-text('Welcome to our Practice WebApp!')"
    author_name = "a[href*='linkedin.com']"
    email = "a[href^='mailto:']"
    breadcrumb = ".breadcrumb"

    def open(self):
        self.navigate(f"{Config.base_url}/about")

    def get_heading_text(self):
        return self.get_text(self.heading)

    def is_welcome_text_visible(self):
        return self.is_visible(self.welcome_text)

    def get_author_name(self):
        return self.get_text(self.author_name)

    def get_email(self):
        return self.page.locator(self.email).get_attribute("href")

    def is_breadcrumb_visible(self):
        return self.is_visible(self.breadcrumb)