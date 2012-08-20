import flexslider
from setuptools import setup, find_packages

setup(
    name='django-flexslider',
    version=flexslider.__version__,
    description='TODO',
    long_description=open('README.rst').read(),
    author='Co-Capacity BV',
    author_email='django+flexslider@co-capacity.org',
    url='https://bitbucket.org/cocapacity/django-flexslider',
    download_url='https://bitbucket.org/cocapacity/django-flexslider/downloads',
    license='BSD',
    packages=find_packages(exclude=('tests', 'project')),
    include_package_data=True,
    zip_safe=False, # because we're including static files that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        "sorl-thumbnail>=11.12",
    ],    
)