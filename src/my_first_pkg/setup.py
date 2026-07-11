from setuptools import find_packages, setup

package_name = 'my_first_pkg'
# name of the executable file is the name of the package and the function to be called is main  
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
    maintainer='aadil',
    maintainer_email='mr.aadil0712@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node_example = my_first_pkg.node_example:main',
            'turtle_controler = my_first_pkg.turtle_controler:main',
        ],
    },
)
