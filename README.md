# Test-Technique-QA-Heyme
## 1. Matrice des Cas de Test
### A. Cas Passants (Happy Path)
| ID | Fonctionnalité ciblée | Titre du Cas de Test | Conditions initiales | Étapes de test | Résultat attendu (Statut attendu : PASS) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP_01** | Interface Calendrier | Intégration du calendrier ergonomique | Être sur un tunnel d'adhésion `worldpass.heyme.care`. | 1. Cliquer sur le champ de saisie de la date de début ou de fin. | Le calendrier s'ouvre de manière fluide et ergonomique. Il affiche une vue double mois **sans sélection d'heures** (affichage épuré des dates uniquement). |
| **CP_02** | Moteur de recherche Pays | Reconnaissance automatique du mot-clé "USA" | Être sur le champ "Pays de destination". | 1. Saisir la chaîne exacte `"USA"` (en majuscules). | Le système fait correspondre automatiquement la saisie et sélectionne l'option **"États-Unis"**. |
| **CP_03** | Règle de gestion des durées | Suppression du blocage pour un séjour de 7 jours | Calendrier ouvert, aucune date sélectionnée. | 1. Sélectionner une date de départ (ex: 27/07/2024).<br>2. Sélectionner une date de retour à +7 jours (ex: 03/08/2024).<br>3. Valider le formulaire. | Le système accepte la saisie. Aucun message de blocage lié à une restriction de durée ne s'affiche. |
| **CP_04** | Règle de gestion des durées | Suppression du blocage pour un séjour de 15 jours | Calendrier ouvert, aucune date sélectionnée. | 1. Sélectionner une date de départ (ex: 27/07/2024).<br>2. Sélectionner une date de retour à +15 jours (ex: 11/08/2024).<br>3. Valider le formulaire. | Le système accepte la saisie. Le calcul se déroule normalement sans erreur de restriction. |

---
### B. Cas Non-Passants (Edge Cases & Limites)
| ID | Fonctionnalité ciblée | Titre du Cas de Test | Conditions initiales | Étapes de test | Résultat attendu (Statut attendu : PASS) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CNP_01** | Moteur de recherche Pays | Tolérance aux casses et variantes pour "USA" | Être sur le champ "Pays de destination". | 1. Saisir la chaîne `"usa"` (en minuscules).<br>2. Effacer et saisir la chaîne `"U.S.A."` (avec points). | Le système doit être tolérant : l'auto-suggestion propose et valide **"États-Unis"** dans les deux cas. |
| **CNP_02** | Cohérence Calendrier | Inversion chronologique des dates | Être sur l'interface du calendrier. | 1. Sélectionner une date de départ (ex: 02/08/2024).<br>2. Tenter de forcer une date de retour antérieure (ex: 27/07/2024). | L'application bloque la sélection de la date de retour ou affiche un message d'erreur bloquant explicite (ex: *"La date de retour doit être postérieure à la date de départ"*). |
| **CNP_03** | Saisie Manuelle | Format de date invalide | Champ de saisie actif. | 1. Tenter de saisir manuellement une date textuelle ou mal formatée (ex: `"27 juillet 2024"` ou `"2024/07/27"`). | Le champ rejette la saisie, applique un masque de saisie automatique `JJ/MM/AAAA` ou lève une alerte de format. |

---
### C. Tests de Non-Régression (TNR)

| ID | Fonctionnalité ciblée | Titre du Cas de Test | Conditions initiales | Étapes de test | Résultat attendu (Statut attendu : PASS) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CNR_01** | Liste des pays | Préservation des autres pays de la base | Être sur le champ "Pays de destination". | 1. Saisir un pays tiers existant (ex: `"France"`, `"Canada"`). | Les pays s'affichent correctement dans la liste déroulante et restent sélectionnables sans régression. |
| **CNR_02** | Limites des durées | Maintien des autres règles de durées standard | Calendrier ouvert. | 1. Tester une durée très courte (ex: 1 jour).<br>2. Tester une durée longue standard (ex: 30 jours, 90 jours). | Le système traite ces durées conformément aux anciennes règles métier toujours en vigueur (pas d'effet de bord suite au correctif des 7/15 jours). |

---
## 2. Environnement de Test & Données de Test
* **URL du tunnel d'adhésion (Test fonctionnel manuel) :** `worldpass.heyme.care`
* **Format des dates requis :** `JJ/MM/AAAA`
  
## 2.Workflow (WF) de Gestion et d'Intégration de la QA
### 1. Réception de la demande & Analyse (Statut : Backlog / To Do)
* **Ce qui se passe :** Le Product Owner (PO) ou le Chef de Projet reçoit le besoin client (ex: l'évolution du calendrier et des pays pour Worldpass) et crée un ticket dans l'outil de gestion (ex: Jira).
* **Rôle de la QA :** Le testeur participe aux réunions de cadrage (Amélioration continue) pour analyser le ticket, s'assurer que les critères d'acceptation sont clairs, non ambigus et testables.
### 2. Conception des Tests (Statut : En cours de spécification)
* **Ce qui se passe :** Avant même que le développeur ne commence à coder, le processus de test est préparé.
* **Rôle de la QA :** Rédaction de la matrice des cas de test (Cas Passants, Non-Passants, Non-Régression) sous forme de fiches de test (idéalement sur un outil comme Jira avec le plugin Xray).
### 3. Phase de Développement & Tests Unitaires (Statut : In Progress)
* **Ce qui se passe :** Le développeur prend le ticket et écrit le code pour répondre au besoin.
* **Rôle de la QA :** Le testeur prépare ses jeux de données de test et commence à écrire la structure de son script d'automatisation. Le développeur réalise ses tests unitaires de son côté.
### 4. Déploiement en Environnement de Test (Statut : Ready for QA)
* **Ce qui se passe :** Le code est poussé sur l'environnement de préproduction ou de recette (ex: `heyme-ep.dev.btc-web.fr`).
* **Rôle de la QA :** C'est le départ pour le testeur.
### 5. Exécution des Tests & Gestion des Anomalies (Statut : In QA / Testing)
* **Ce qui se passe :** Le testeur exécute la stratégie planifiée.
* **Rôle de la QA :**
  * **Étape A :** Exécution des tests fonctionnels manuels (Vérification visuelle du calendrier, saisie du mot "USA").
  * **Étape B :** Lancement du script automatique (Playwright) pour s'assurer que la connexion et la liste des contrats fonctionnent toujours sans perte de performance.
  * **Étape C (Si Bug trouvé) :** Le testeur ouvre un ticket d'anomalie (Bug), le lie au ticket principal, et le renvoie au développeur (Statut : *Reopened / Redev*).
  * **Étape D (Si Tout est OK) :** Les tests passent au statut **PASS**. Le testeur donne son "Go QA".
### 6. Mise en Production & Test de Fumée (Statut : Done / Released)
* **Ce qui se passe :** Le projet est déployé sur l'environnement réel pour les clients de Heyme.
* **Rôle de la QA :** Juste après le déploiement, le testeur réalise un **Smoke Test** (Test de fumée). C'est une vérification rapide (en moins de 5 minutes) des fonctionnalités critiques directement en production pour s'assurer que la livraison s'est bien passée et que le site ne s'est pas crashé.
  
