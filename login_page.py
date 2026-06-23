from playwright.sync_api import Page, expect

from config.settings import BASE_URL, EMAIL, PASSWORD


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self) -> None:
        self.page.goto(f"{BASE_URL.rstrip('/')}/login", wait_until="domcontentloaded")

    def login(self, email: str = EMAIL, password: str = PASSWORD) -> None:
        self.page.locator("#email").fill(email)
        self.page.locator("#password").fill(password)
        self.page.locator('input[type="submit"]').click()

    def skip_onboarding_if_present(self) -> None:
        skip_button = self.page.get_by_text("Je compléterai mon profil plus tard", exact=True)
        if skip_button.is_visible():
            skip_button.click()

    def assert_logged_in(self) -> None:
        expect(self.page.get_by_role("link", name="Déconnexion")).to_be_visible(timeout=30_000)
