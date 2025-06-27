from launch import LaunchDescription
from launch_ros.actions import Node
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_path = get_package_share_directory('anymal_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'anymal.urdf.xacro')

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            output='screen',
            arguments=['-entity', 'anymal', '-file', urdf_file]
        )
    ])
