"""A set of scripts to issue tasks to Open-RMF from the command line."""
from setuptools import setup

package_name = 'rmf_ws_tasks'

setup(
    name=package_name,
    version='2.5.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    author='Grey',
    author_email='grey@openrobotics.org',
    zip_safe=True,
    maintainer='yadu',
    maintainer_email='yadunund@openrobotics.org',
    description='A package containing scripts for demos',
    license='Apache License Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'request_loop = rmf_ws_tasks.request_loop:main',
            'request_lift = rmf_ws_tasks.request_lift:main',
            'cancel_task = rmf_ws_tasks.cancel_task:main',
            'dispatch_loop = rmf_ws_tasks.dispatch_loop:main',
            'dispatch_action = rmf_ws_tasks.dispatch_action:main',
            'dispatch_patrol = rmf_ws_tasks.dispatch_patrol:main',
            'dispatch_delivery = rmf_ws_tasks.dispatch_delivery:main',
            'dispatch_cart_delivery = '
                'rmf_ws_tasks.dispatch_cart_delivery:main',
            'dispatch_clean = rmf_ws_tasks.dispatch_clean:main',
            'dispatch_go_to_place = rmf_ws_tasks.dispatch_go_to_place:main',
            'dispatch_teleop = rmf_ws_tasks.dispatch_teleop:main',
            'get_robot_location = rmf_ws_tasks.get_robot_location:main',
            'mock_docker = rmf_ws_tasks.mock_docker:main',
            'teleop_robot = rmf_ws_tasks.teleop_robot:main',
            'dispatch_json = rmf_ws_tasks.dispatch_json:main',
            'api_request = rmf_ws_tasks.api_request:main',
            'wait_for_task_complete = \
                rmf_ws_tasks.wait_for_task_complete:main'
        ],
    },
)
