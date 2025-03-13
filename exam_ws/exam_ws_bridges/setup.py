from setuptools import setup

package_name = 'exam_ws_bridges'

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
    zip_safe=True,
    maintainer='Boon Han',
    maintainer_email='cnboonhan@openrobotics.org',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            (
                'fleet_socketio_bridge='
                'exam_ws_bridges.fleet_socketio_bridge:main',
                'fleet_robotmanager_mqtt_bridge='
                'exam_ws_bridges.fleet_robotmanager_mqtt_bridge:main',
            ),
        ],
    },
)
