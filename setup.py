from setuptools import setup, find_packages

setup(
    name='django-pages',
    version='0.1a',
    author='Derugin Anton',
    author_email='anton.derugin@gmail.com',
    packages=['pages'],
    install_requires=[
        'django-helpers'
    ],
    dependency_links=[
        'git+git://github.com/aderugin/django-helpers.git#egg=django-helpers'
    ],
    include_package_data=True,
    url='https://github.com/aderugin/django-pages',
    license='MIT',
    description='Django application',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
