## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
## from: docs.ros.org/api/catkin/html/howto/installing_python.html
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['boat_goal_heading'],
    package_dir={'': 'src'})

setup(**setup_args)
