import rclpy
from rclpy.node import Node
from mt_arm_interfaces.msg import ArmJoints

class ArmPublisher(Node):
    def __init__(self):
        super().__init__('arm_publisher')
        self.publisher_ = self.create_publisher(ArmJoints, 'arm_joints', 10)
        timer_period = 1  # Publish every 1 second
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = ArmJoints()
        msg.a = 1.0
        msg.b = 2.0
        msg.c = 3.0
        msg.d = 4.0
        msg.e = 5.0
        msg.f = 6.0
        msg.g = 7.0
        msg.h = 8.0

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg}')

def main(args=None):
    rclpy.init(args=args)
    arm_publisher = ArmPublisher()

    rclpy.spin(arm_publisher)

    arm_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

