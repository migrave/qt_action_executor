#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['qt_action_executor', 'qt_action_executor_wrapper'],
    package_dir={'qt_action_executor': 'common/src/qt_action_executor',
                 'qt_action_executor_wrapper': 'ros/src/qt_action_executor_wrapper'}
)

setup(**d)
