#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__('Robot_News')
        self.publisher_ = self.create_publisher(
         String ,
         'news',
         10   
        )
        self.timer = self.create_timer(0.5, self.publish)


    def publish(self):
            msg = String()
            msg.data = "Hello World"
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
       
    
def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
