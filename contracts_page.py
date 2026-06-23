import re

from playwright.sync_api import Page, expect

from config.settings import BASE_URL


class ContractsPage:
    CONTRACT_NUMBER_PATTERN = re.compile(r"CT\d+")

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self) -> None:
        self.page.goto(
            f"{BASE_URL.rstrip('/')}/contract/list",
            wait_until="domcontentloaded",
        )

    def assert_loaded(self) -> None:
        expect(self.page).to_have_title(re.compile(r"Mes contrats", re.IGNORECASE))
        expect(self.page.get_by_role("heading", name="Mes contrats")).to_be_visible()

    def get_contracts(self) -> list[dict[str, str]]:
        expect(self.page.get_by_role("link", name="Voir le détail").first).to_be_visible(
            timeout=30_000
        )

        numbers = self.page.locator(".col3 .text span").all_inner_texts()
        names = self.page.locator(".col2 .type").all_inner_texts()
        statuses = self.page.locator(".col4 .text span").all_inner_texts()

        contracts: list[dict[str, str]] = []
        for index, numero in enumerate(numbers):
            contracts.append(
                {
                    "numero": numero.strip(),
                    "nom": names[index].strip() if index < len(names) else "",
                    "statut": statuses[index].strip() if index < len(statuses) else "",
                }
            )

        return contracts
