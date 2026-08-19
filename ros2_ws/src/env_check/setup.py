from setuptools import setup

package_name = 'env_check'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='votre-nom',
    maintainer_email='you@example.com',
    description='Node minimal pour valider que l\'environnement ROS2 fonctionne',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'circle_mover = env_check.circle_mover:main',
        ],
    },
)
