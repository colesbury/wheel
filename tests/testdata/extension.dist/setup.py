from setuptools import setup, Extension

setup(name='extension.dist',
      version='0.1',
      description='A testing distribution \N{SNOWMAN}',
      ext_modules=[
          Extension(name='extension',
                    sources=['extension.c'])
          ],
      )
