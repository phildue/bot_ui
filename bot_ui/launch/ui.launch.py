import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    launch_files = ['rosboard','rviz','teleop_joy']

    return launch.LaunchDescription([
        IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('bot_ui'), 'launch/'),
            f'{f}.launch.py'])) for f in launch_files]) 
