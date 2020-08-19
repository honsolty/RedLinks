from setuptools import setup, find_packages
 
 
setup(name='redlinks',
 
      version='0.0.3',

      url='https://github.com/honsolty/RedLinks',
 
      description='Work with links and redis',
 
      packages=["redlinks"],
 
      long_description=open('README.md').read(),

      install_requires=['aiohttp', "redis"],
    )
