from setuptools import setup

setup(
    name='pyOfferUp',  # How you named your package folder (MyLib)
    packages=['pyOfferUp'],  # Chose the same as "name"
    version='0.1',  # Start with a small number and increase it with every change you make
    license='apache-2.0',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Scrape data from offerup.com',  # Give a short description about your library
    author='Oscar R. Torres',  # Type in your name
    author_email='oscar0812torres@gmail.com',  # Type in your E-Mail
    url='https://github.com/oscar0812/pyOfferUp',  # Provide either the link to your github or to your website
    download_url='https://github.com/oscar0812/pyOfferUp/archive/refs/tags/v_01.tar.gz',  # I explain this later on
    keywords=['OFFERUP', 'BUYING', 'SCRAPER', 'BITTLE'],  # Keywords that define your package best
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
