# Instructions techniques — Mini-projet

## Ce qui vous est fourni

Trois packages ROS2 sont déjà présents dans `ros2_ws/src/` :

```
src/
├── trajectory_interfaces/     # Le message partagé entre les deux nodes — NE PAS MODIFIER
│   └── msg/TrajectoryCommand.msg
├── brain_commander/           # Le node "cerveau" (C++) — À COMPLÉTER
│   └── src/commander_node.cpp
└── turtle_executor/           # Le node "tortue" (Python) — À COMPLÉTER
    └── turtle_executor/executor_node.py
```

**Comment ça communique :**

```
brain_commander (C++)  --/trajectory_cmd-->  turtle_executor (Python)  --/turtle1/cmd_vel-->  turtlesim
   (calcule la trajectoire)                    (transmet à turtlesim)
```

Le node C++ décide **quoi faire** (trajectoire, réaction aux événements). Le node Python se contente de **transmettre** cette décision à turtlesim. C'est volontairement organisé ainsi : l'essentiel de la difficulté du projet est côté C++.

---

## Ce que vous devez faire

**Côté C++ (`brain_commander`) — l'essentiel du projet :**
- `TODO 1` : implémenter une trajectoire non triviale pour la tortue (carré, cercle, suite de points... libre à vous)
- `TODO 2` : faire réagir la tortue à un événement externe (simulé via `/obstacle_alert`, voir plus bas)

**Côté Python (`turtle_executor`) — plomberie :**
- `TODO 1` : convertir la commande reçue en message `Twist`
- `TODO 2` : afficher quand un obstacle est signalé

Vous êtes libres d'ajouter des membres, fonctions, ou fichiers si votre logique le demande — les squelettes fournis sont un point de départ, pas une contrainte stricte.

---

## Compiler et lancer

Dans le bureau virtuel (`http://localhost:6080`), terminal :

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

Il vous faudra **3 terminaux** (pensez à `source /opt/ros/humble/setup.bash` puis `source ~/ros2_ws/install/setup.bash` dans chacun) :

**Terminal 1 — turtlesim :**
```bash
ros2 run turtlesim turtlesim_node
```

**Terminal 2 — votre node cerveau (C++) :**
```bash
ros2 run brain_commander commander_node
```

**Terminal 3 — votre node tortue (Python) :**
```bash
ros2 run turtle_executor executor_node
```

Si tout fonctionne, la tortue doit bouger selon la trajectoire que vous avez implémentée.

---

## Tester la réaction à un obstacle

Dans un 4e terminal, simulez la détection d'un obstacle :

```bash
ros2 topic pub /obstacle_alert std_msgs/msg/Bool "{data: true}"
```

Le node `commander_node` doit réagir selon ce que vous avez implémenté au `TODO 2`.

Pour vérifier ce qui circule sur le topic entre vos deux nodes :
```bash
ros2 topic echo /trajectory_cmd
```

---

## Livrables attendus

Voir le cahier des charges pour le détail complet, mais pour rappel :
- Dépôt Git personnel avec **plus d'un commit**, échelonnés dans le temps
- Un `README.md` expliquant vite fait ce que fait le code, vous pouvez virer le mien
- Vous devez être capable d'expliquer chaque partie de votre code en entretien, même si vous avez utilisé de l'IA pour vous aider à l'écrire
