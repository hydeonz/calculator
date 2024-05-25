from setuptools import setup, find_packages

setup(
    name='calculator',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'calculator = calc:main',  
        ],
    },
    install_requires=[

    ],
    description='Простое приложение-калькулятор',
    license='MIT',
    keywords='calculator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
