from setuptools import setup

setup(
    name="pytest-flask-sqlalchemy",
    packages = ['pytest_flask_sqlalchemy'],
    license='MIT',
    description='pytest plugin with sqlalchemy related fixtures',
    version='0.1.0',
    author='ESSS',
    author_email='igor@esss.co',
    url='http://github.com/ESSS/pytest-flask-sqlalchemy/',
    py_modules=['pytest_flask_sqlalchemy'],
    entry_points = {
        'pytest11': [
            'flask_sqlalchemy = pytest_flask_sqlalchemy',
        ]
    },
    classifiers=[
        "Framework :: Pytest",
    ],
)