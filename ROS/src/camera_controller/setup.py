from setuptools import find_packages, setup

package_name = 'camera_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mohan',
    maintainer_email='mohan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "first_node = camera_controller.test_node:main", #Executable name for test_node
            "draw_circle = camera_controller.draw_circle:main", # Executable name for draw_circle
            "pose_subscriber = camera_controller.pose_subscriber:main", # Executable name for pose_subscriber
            "turtle_controller = camera_controller.turtle_controller:main" # Executable name for turtle_controller
        ],
    },
)
