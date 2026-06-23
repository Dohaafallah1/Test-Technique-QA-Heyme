from playwright.sync_api import Page, expect

from pages.contracts_page import ContractsPage
from pages.login_page import LoginPage


def test_connexion_et_liste_contrats(page: Page, perf) -> None:
    login_page = LoginPage(page)
    contracts_page = ContractsPage(page)

    perf.start()
    login_page.goto()
    perf.stop("Chargement page login")

    perf.start()
    login_page.login()
    page.wait_for_url("**/onboarding**", timeout=60_000)
    perf.stop("Authentification (soumission formulaire)")

    perf.start()
    login_page.skip_onboarding_if_present()
    login_page.assert_logged_in()
    perf.stop("Contournement onboarding + session active")

    perf.start()
    contracts_page.goto()
    contracts_page.assert_loaded()
    perf.stop("Chargement page Mes contrats")

    perf.start()
    contracts = contracts_page.get_contracts()
    perf.stop("Extraction liste des contrats")

    assert len(contracts) > 0, "Aucun contrat trouvé pour l'utilisateur de test"

    contract_numbers = [contract["numero"] for contract in contracts]
    assert all(numero.startswith("CT") for numero in contract_numbers)

    print(f"\n{perf.summary()}")
    print(f"\nContrats récupérés ({len(contracts)}) :")
    for contract in contracts:
        numero = contract["numero"]
        nom = contract.get("nom", "")
        statut = contract.get("statut", "")
        extra = f" — {nom} ({statut})" if nom else ""
        print(f"  • {numero}{extra}")

    expect(page.get_by_role("link", name="Voir le détail").first).to_be_visible()
