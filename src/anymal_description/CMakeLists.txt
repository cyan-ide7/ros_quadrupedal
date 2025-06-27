cmake_minimum_required(VERSION 3.8)
project(anymal_description)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(xacro REQUIRED)

install(DIRECTORY launch urdf config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()