# Installation de l'environnement ROS2 — Linux

Bon si vous avez Linux je me doute que ca va vous servir à rien, mais on sait jamais.

## 1. Vérifier les prérequis

- Une distribution Linux avec accès `sudo` (Ubuntu/Debian utilisé comme référence ci-dessous ; adaptez la commande d'installation si vous êtes sur une autre distro).

## 2. Installer Docker Engine

**[Dans un terminal]** :
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

Déconnectez-vous/reconnectez-vous (ou redémarrez) pour que l'ajout au groupe `docker` prenne effet.

Vérifiez que tout fonctionne :
```bash
docker --version
docker run hello-world
```
Si un message de bienvenue s'affiche, Docker fonctionne correctement.

## 3. Vérifier/installer Git

```bash
git --version
```
Si la commande n'est pas reconnue :
```bash
sudo apt update
sudo apt install -y git
```

## 4. Cloner le dépôt du projet

À l'endroit où vous voulez ranger le projet :
```bash
git clone <URL_DU_REPO>
cd ROS2_env
```

## 5. Lancer l'environnement

```bash
docker compose up -d
```

La première exécution va télécharger l'image (plusieurs Go, ça peut prendre quelques minutes selon la connexion). Les fois suivantes, le démarrage sera quasi instantané.

Vérifiez que le conteneur tourne bien :
```bash
docker ps
```
Vous devriez voir `ros2_humble_desktop` avec un statut "Up".