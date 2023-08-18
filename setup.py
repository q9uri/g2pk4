import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

required_packages = [
            'jamo',
            'nltk',
        ]


setuptools.setup(
    name="g2pk2",
    version="0.0.3",
    author="tenebo",
    author_email="tenebo@naver.com",
    description="g2pk2: updated folk of g2pk module",
    install_requires=required_packages,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tenebo/g2pk2",
    packages=setuptools.find_packages(),
    package_data={'g2pk2': ['g2pk2/idioms.txt', 'g2pk2/rules.txt', 'g2pk2/table.csv']},
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
