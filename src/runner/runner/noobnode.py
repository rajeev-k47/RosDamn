#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class noob(Node):
    def __init__(self):
        super().__init__('noobnode')
        self.get_logger().info('Hello ROS2 World!')
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Timer event')

def main(args=None):
    rclpy.init(args=args)

    node = noob()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()