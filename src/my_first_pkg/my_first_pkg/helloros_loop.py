import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class turtle_controller(Node):
    def __init__(self, name):
        super().__init__(name)
        
        self.create_timer(1.0, self.callback)

    def callback(self):
        self.get_logger().info("hello ros")


def main(args=None):
  rclpy.init(args=args)
  node = turtle_controller("my_first_node")
  rclpy.spin(node)
  rclpy.shutdown()
if __name__=="__main__":
  main()