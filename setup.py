import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='netaccess',  
     version='1.0.1',
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
     entry_points={
         'console_scripts':['netaccess=netaccess.netaccess:main']
     },
     classifiers=[
         "Programming Language :: Python :: 3.5",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     # include_package_data=True,
     # zip_safe=False,
 )
