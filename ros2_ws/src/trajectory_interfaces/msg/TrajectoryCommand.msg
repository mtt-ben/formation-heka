# Commande de haut niveau envoyee par le node "commande" (C++, brain_commander)
# au node "tortue" (Python, turtle_executor), qui se charge de la traduire
# en commande de vitesse (Twist) pour turtlesim.
#
# Ne PAS modifier ce fichier : il est commun aux deux nodes.

float32 linear_speed        # vitesse d'avancement souhaitee (m/s)
float32 angular_speed       # vitesse de rotation souhaitee (rad/s)
bool avoid_obstacle         # true si le node "commande" a detecte un obstacle a eviter
