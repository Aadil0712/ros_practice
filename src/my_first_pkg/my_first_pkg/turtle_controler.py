import random

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class TurtleController(Node):
    def __init__(self):
        super().__init__("my_first_node")
        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.create_timer(1.0, self.callback)

    def callback(self):
        msg = Twist()
        msg.linear.x = random.uniform(-3, 2.0)
        msg.linear.y = random.uniform(-3, 1.0)
        msg.linear.z = random.uniform(-3, 3.0)
        msg.angular.x = random.uniform(-3, 1.0)
        msg.angular.y = random.uniform(-3, 1.0)
        msg.angular.z = random.uniform(-3, 3.0)
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()