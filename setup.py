import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='HybridCodex',  
     version='0.1',
     scripts=['HybridCodex'] ,
     author="AhmedElkhateeb",
     author_email="ahmedelkhateeb.asu@gmail.com",
     description="A test package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ftkhateeb/HybridCodex_pckg",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
