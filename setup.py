from setuptools import setup

setup(
    name='openai-linda',
    version='1.0',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'openai-linda=main:main'
        ]
    }
)
