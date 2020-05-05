import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='jinja-reverse',  
    version='0.1',
    author="Gabriel Hodoroaga",
    author_email="gabihodoroaga@gmail.com",
    description="Reverse a jinja tempalate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabihodoroaga/jinja-reverse",
    package_dir={'': '.'},
    packages=['.'],
    include_package_data=True,
    entry_points={'console_scripts': [
        'jinja-reverse = reverse:main',
        'jinja-generate = generate:main',
    ]},
    install_requires=[
        'Jinja2>=2.10.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
