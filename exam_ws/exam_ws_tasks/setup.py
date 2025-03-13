"""A set of scripts to issue tasks to Open-RMF from the command line."""
from setuptools import setup

package_name = 'exam_ws_tasks'

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
            'request_loop = exam_ws_tasks.request_loop:main',
            'request_lift = exam_ws_tasks.request_lift:main',
            'cancel_task = exam_ws_tasks.cancel_task:main',
            'dispatch_loop = exam_ws_tasks.dispatch_loop:main',
            'dispatch_action = exam_ws_tasks.dispatch_action:main',
            'dispatch_patrol = exam_ws_tasks.dispatch_patrol:main',
            'dispatch_delivery = exam_ws_tasks.dispatch_delivery:main',
            'dispatch_cart_delivery = '
                'exam_ws_tasks.dispatch_cart_delivery:main',
            'dispatch_clean = exam_ws_tasks.dispatch_clean:main',
            'dispatch_go_to_place = exam_ws_tasks.dispatch_go_to_place:main',
            'dispatch_teleop = exam_ws_tasks.dispatch_teleop:main',
            'get_robot_location = exam_ws_tasks.get_robot_location:main',
            'mock_docker = exam_ws_tasks.mock_docker:main',
            'teleop_robot = exam_ws_tasks.teleop_robot:main',
            'dispatch_json = exam_ws_tasks.dispatch_json:main',
            'api_request = exam_ws_tasks.api_request:main',
            'wait_for_task_complete = \
                exam_ws_tasks.wait_for_task_complete:main'
        ],
    },
)
