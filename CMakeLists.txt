cmake_minimum_required(VERSION 3.0.2)
project(qt_action_executor)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslint
  migrave_ros_msgs
)

roslint_python()
catkin_python_setup()
catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
