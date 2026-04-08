# CLAUDE.md — préférences globales

## Langue
Toujours répondre en français. Le code, les identifiants, les noms de fichiers et les messages de commit restent en anglais.

## Système (Arch Linux)
- Gestionnaire de paquets Python : `uv` — jamais `pip install` directement
- Installer un outil CLI Python : `uv tool install -e .` (symlink dans `~/.local/bin`)
- Lancer sans installer : `uv run <script>`
- Dépendances de dev : `[dependency-groups] dev = [...]` dans pyproject.toml

## Git
- Branches stables : `main` (releases taguées semver)
- Développement : `dev/<feature>` → merge sur `main` quand les tests passent
- Format de tag : `vX.Y.Z` avec message annotated (`-a`)
- Ne jamais committer `README.md` vide ni fichiers stub inutiles

## Style de code (Python)
- Préférer stdlib plutôt que dépendances tierces quand c'est raisonnable
- Zero subprocess Python secondaire si possible (pas de wrappers CLI comme `llm`)
- Type hints sur toutes les signatures publiques
- Pas de docstrings si la logique est évidente

## Tests
- Framework : `pytest`
- `uv run pytest tests/ -v` pour lancer
- Mocker `http.client` pour les tests HTTP, pas de vraies requêtes réseau
