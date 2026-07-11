import rclpy
from rclpy.node import Node

class CustomNode(Node):
    def __init__(self, name):
        super().__init__(name)
        
        self.create_timer(1.0, self.callback)
        self.get_logger().info("Node has been started")
        self.get_logger().info("Node name is: " + self.get_name())
        
    def callback(self):
        self.get_logger().info("hello ros")


def main(args=None):
  rclpy.init(args=args)
  node = CustomNode("my_first_node")
  rclpy.spin(node)
  rclpy.shutdown()
if __name__=="__main__":
  main()