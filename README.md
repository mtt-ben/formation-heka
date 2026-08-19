# Robot Étudiant — Environnement & Mini-Projet de Sélection

Bienvenue ! Ce dépôt contient tout ce dont vous avez besoin pour l'étape de sélection logicielle : l'environnement de développement (Docker) et le mini-projet à réaliser.

## Par où commencer

1. **Installer l'environnement** → `docs/1-guide_installation_windows.md` ou `docs/1-guide_installation_linux.md`
2. **Valider que tout fonctionne** → `docs/2-test_validation_environnement.md`
3. **Lire le cahier des charges** → `docs/3-cahier_des_charges_mini_projet.md`
4. **Démarrer le mini-projet** → `docs/4-instructions_mini_projet.md`

## Structure du dépôt

```
.
├── docker-compose.yaml                        # Lance l'environnement (ROS2 Humble + bureau virtuel)
├── docs/
│   ├── guide_installation_windows.md           # Installation de l'environnement (Windows)
│   ├── test_validation_environnement.md        # Checklist pour vérifier que tout fonctionne
│   ├── cahier_des_charges_mini_projet.md       # Règles du mini-projet de sélection
│   └── instructions_mini_projet.md             # Instructions techniques (build, run, test)
└── ros2_ws/
    └── src/
        ├── env_check/                          # Package de test — vérifie que l'environnement marche
        ├── trajectory_interfaces/               # Message partagé entre les deux nodes du mini-projet
        ├── brain_commander/                     # Node C++ "cerveau" — À COMPLÉTER
        └── turtle_executor/                     # Node Python "tortue" — À COMPLÉTER
```

## Démarrage rapide

```bash
docker compose up -d
```

Puis ouvrez **http://localhost:6080** dans votre navigateur pour accéder au bureau virtuel contenant ROS2.

Votre code doit être écrit dans `ros2_ws/src/` — ce dossier est synchronisé entre votre machine et le conteneur, donc rien n'est perdu si le conteneur est supprimé.
