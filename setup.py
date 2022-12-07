from distutils.core import setup

setup(name='metastock',
      version='1.0.2',
      description='Metastock file reader',
      packages=['metastock',],
      install_requires=[
          'pandas',
      ]
     )