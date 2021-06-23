from setuptools import setup, find_namespace_packages

setup(
      name='cli_bot',
      version='1.0',
      description='Console bot for contact book managing',
      url='https://github.com/Andrew-1986/CLI_bot',
      author='Group_4',
      entry_points={'console_scripts': ['bot = main:main']},
      packages=['main']
      )
