# PyCache Remove

Un outil simple et efficace pour nettoyer les dossiers `__pycache__` de vos projets Python.

## Fonctionnalités

- Supprime récursivement tous les dossiers `__pycache__`
- Nécessite les privilèges administrateur
- Rapide et efficace
- Interface en ligne de commande

## Prérequis

- Python >= 3.11
- Droits administrateur
- Windows (actuellement optimisé pour Windows)

## Installation

```bash
poetry install
```

## Utilisation

Exécutez l'outil en mode administrateur :

```bash
poetry run remove
```

Puis entrez le chemin du répertoire à nettoyer :

```
Enter the directory path to remove __pycache__ folders from: C:\path\to\your\project
```

## Dépendances

- `pyinstaller` (>= 6.18.0, < 7.0.0)

## Auteur

**S29Ducky** - [nbarasraso@edenschool.fr](mailto:nbarasraso@edenschool.fr)


**Note** : Cet outil doit être exécuté avec les privilèges administrateur pour fonctionner correctement.