from setuptools import setup, find_packages

setup(
    name='pshelf',
    version='0.5',
    description='A shelf-like pythonic structure',
    author='transhap',
    author_email='fet.prashantsingh@gmail.com',
    license='None',
    packages=find_packages(),
    python_requires='~=3.5',
    install_requires=[
        'Click',
    ],
    entry_points = '''
        [console_scripts]
        pshelf=pshelf.shell:shelf
    ''',
    zip_safe=False
    )
