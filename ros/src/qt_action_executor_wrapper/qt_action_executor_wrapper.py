import rospy

from std_msgs.msg import String
from qt_action_executor.qt_action_executor import QtActionExecutor
from migrave_ros_msgs.msg import RobotAction, AffectiveState

class QtActionExecutorWrapper(object):
    def __init__(self):
        speech_topic = rospy.get_param('~speech_topic', '/qt_robot/speech/say')
        gesture_topic = rospy.get_param('~gesture_topic', '/qt_robot/emotion/show')
        face_expression_topic = rospy.get_param('~face_expression_topic', '/qt_robot/gesture/play')        
        action_topic = rospy.get_param('~action_topic', '/robot_action')

        self.current_robot_action = None
        
        # Should be ros action in the future
        self.action_sub = rospy.Subscriber(action_topic,
                                          RobotAction,
                                          self.robot_action_cb)

        # Publishers for low level actions
        self.speech_pub = rospy.Publisher(speech_topic, String, queue_size=1)
        self.gesture_pub = rospy.Publisher(gesture_topic, String, queue_size=1)
        self.face_expression_pub = rospy.Publisher(face_expression_topic, String, queue_size=1)

        self.qt_action_executor = QtActionExecutor()

    def act(self) -> None:
        """Retrieves an appropriate action for the robot and
        converts into the low level actions.
        """
        if self.current_robot_action:
            sentence = self.current_robot_action.sentence
            gesture = self.current_robot_action.gesture_type
            face_expression = self.current_robot_action.face_expression

            rospy.loginfo('Performing action: {}'.format(self.current_robot_action.action_name))

            self.speech_pub.publish(sentence)
            self.gesture_pub.publish('QT/{}'.format(gesture))
            self.face_expression_pub.publish('QT/{}'.format(face_expression))
            
            self.current_robot_action = None

    def robot_action_cb(self, robot_action_msg: RobotAction) -> None:
        if not self.current_robot_action:
            self.current_robot_action = robot_action_msg
            rospy.loginfo('Received action: \n {}'.format(self.current_robot_action.action_name))
        
        else:
            rospy.logwarn('Received action {}, but the previous one is still being executed. Ignoring ...'.
            format(self.current_robot_action.action_name))