import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_home_urls",
    version="0.0.1",
    author="Yuji Koseki",
    author_email="pxquuqjm0k62new7q4@gmail.com",
    description="Django home urlconf.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuji-koseki/django-home-urls",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Framework :: Django',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
