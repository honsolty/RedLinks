from setuptools import setup, find_packages
 
 
setup(name='redlinks',
 
      version='0.0.5',

      url='https://github.com/honsolty/RedLinks',
 
      description='Work with links and redis',
 
      packages=["redlinks"],

      install_requires=['aiohttp', "redis"],
    )
