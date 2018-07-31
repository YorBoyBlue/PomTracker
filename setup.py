from setuptools import setup

setup(
    name='pom_tracker',
    version='1.0.0',
    description='Used to track time and tasks using the Pomodoro concept',
    long_description=open('README').read(),
    license='LICENSE',
    author='Arin Blue',
    author_email='arin.a.h.blue@gmail.com',
    packages=['pom_tracker'],
    install_requires=[],
    test_suite='falcon_v_app.tests.run_tests.suite',
    zip_safe=False  # Zipped eggs don't play well with name spacing
)
