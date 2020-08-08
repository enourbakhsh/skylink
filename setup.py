from setuptools import setup

setup(name='skylink',
      version=__version__,
      description='Using KDTree search and graphs to match sky catalogs.',
      url='https://github.com/skylink',
      author='Erfan Nourbakhsh',
      author_email='erfanyz@gmail.com',
      license='MIT',
      install_requires=[
          "numpy",
          "astropy",
          "networkx", 
          "networkit", 
          "igraph", 
          "pandas", #pandas>=0.25.3
          "busypal @ git+https://github.com/enourbakhsh/busypal", 
          "colored", 
          "tqdm",
      ],
      zip_safe=False)