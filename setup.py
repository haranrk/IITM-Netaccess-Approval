import os
import setuptools
import netaccess

setuptools.setup(
     name='netaccess',  
     version=netaccess.__version__,
     author="Haran Rajkumar",
     author_email="haranrajkumar97@gmail.com",
     description="CLI for IIT Madras netaccess",
     long_description=open("README.md").read(),
     long_description_content_type="text/markdown",
     url="https://github.com/haranrk/IITM-Netaccess-Approval",
     packages=setuptools.find_packages(),
     install_requires = [
         'mechanize',
         ],
     entry_points='''
         [console_scripts]
         netaccess=netaccess.netaccess:main
     ''',
     classifiers=[
         "Programming Language :: Python :: 3.5",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
