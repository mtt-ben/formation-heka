# Installation de l'environnement ROS2 — Windows

## 1. Vérifier les prérequis

- Windows 10 (version 2004 ou plus récente) ou Windows 11.

## 2. Installer WSL2

Docker Desktop a besoin de WSL2 comme moteur sous-jacent sur Windows.

**[Dans PowerShell, en tant qu'administrateur]** (clic droit sur PowerShell → "Exécuter en tant qu'administrateur) :
```powershell
wsl --install
```
Redémarrez l'ordinateur si demandé.

> Si WSL est déjà installé, assurez-vous qu'il est en version 2 :
> **[PowerShell]**
> ```powershell
> wsl --set-default-version 2
> ```

⚠️ **Point important :** au tout premier démarrage après l'installation, Windows va **automatiquement ouvrir une fenêtre "Ubuntu"** et vous demander de créer un nom d'utilisateur et un mot de passe pour cette distribution Linux. C'est normal, faites-le — mais c'est la **seule et unique fois** où vous interagissez avec ce terminal Ubuntu. Il sert uniquement de moteur interne à Docker Desktop. **Toutes les commandes du reste de ce guide se tapent dans PowerShell, jamais dans cette fenêtre Ubuntu.**

## 3. Installer Docker Desktop

1. Téléchargez Docker Desktop depuis [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
2. Lancez l'installateur (double-clic sur le `.exe` téléchargé — pas de terminal pour cette étape). Sur l'écran de configuration, assurez-vous que l'option **"Use WSL 2 instead of Hyper-V"** est cochée (c'est le choix par défaut).
3. Redémarrez si demandé.
4. Lancez Docker Desktop (icône sur le bureau ou menu Démarrer) et attendez que l'icône dans la barre des tâches indique qu'il est prêt (généralement quelques dizaines de secondes au premier démarrage).
5. Vérifiez que tout fonctionne.
**[Dans PowerShell]** (une fenêtre normale, pas besoin d'admin, pas la fenêtre Ubuntu) :
```powershell
docker --version
docker run hello-world
```
Si un message de bienvenue s'affiche, Docker fonctionne correctement.

## 4. Vérifier/installer Git

**[Dans PowerShell]** :
```powershell
git --version
```
Si la commande n'est pas reconnue, installez Git depuis [git-scm.com/download/win](https://git-scm.com/download/win) (double-clic sur l'installateur, cliquer "Next" jusqu'au bout — installation par défaut, pas de terminal requis).

## 5. Cloner le dépôt du projet puis créer votre propre branche

**[Dans PowerShell]**, à l'endroit où vous voulez ranger le projet :
```powershell
git clone https://github.com/mtt-ben/formation-heka.git
git branch <votre_nom>
cd ROS2_env
```

## 6. Lancer l'environnement

**[Dans PowerShell, même dossier]** :
```powershell
docker compose up -d
```

La première exécution va télécharger l'image (plusieurs Go, ça peut prendre quelques minutes selon la connexion). Les fois suivantes, le démarrage sera quasi instantané.

Vérifiez que le conteneur tourne bien :
```powershell
docker ps
```
Vous devriez voir `ros2_humble_desktop` avec un statut "Up".

---
