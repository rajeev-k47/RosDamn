from setuptools import find_packages, setup

package_name = 'runner'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rajeev',
    maintainer_email='rajeevkumawat2007@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={  # <-- Use this to specify extra dependencies for testing
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            "runner = runner.noobnode:main",
            'Robot_news = runner.robot_news:main',
        ],
    },
)
