from setuptools import setup

setup(
      name='cli_bot',
      version='1.2',
      description='Console bot for contact book managing',
      url='https://github.com/Andrew-1986/CLI_bot',
      author='Group_4',
      entry_points={'console_scripts': ['cli_bot = cli_bot.bot:main']},
      packages=['cli_bot']
      )
