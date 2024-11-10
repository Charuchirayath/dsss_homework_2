from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Name of the package
    version='0.1',  # Initial version
    packages=find_packages(),  # Automatically find all packages in the project
    install_requires=[],  # Add dependencies here if any
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',  # Entry point for the command line tool
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Update with your license
        'Operating System :: OS Independent',
    ],
)