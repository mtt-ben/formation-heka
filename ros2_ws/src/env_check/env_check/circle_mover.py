"""
Node minimal de validation d'environnement.

Publie en boucle sur /turtle1/cmd_vel pour faire tourner la tortue
de turtlesim en cercle. Sert uniquement a verifier que ROS2, rclpy,
et la communication avec turtlesim fonctionnent correctement.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleMover(Node):

    def __init__(self):
        super().__init__('circle_mover')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.1  # secondes
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('circle_mover demarre : la tortue devrait tourner en cercle.')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0     # vitesse d'avancement
        msg.angular.z = 1.0    # vitesse de rotation -> donne un mouvement circulaire
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CircleMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
