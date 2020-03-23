from setuptools import setup, find_packages

setup(
    name='mkdocs-localsearch',
    version='0.6.0',
    description='A MkDocs plugin to replace the native "search" plugin with a search plugin that also works locally (file:// protocol). Only works with the Material theme.',
    long_description='',
    keywords='mkdocs local search',
    url='https://github.com/wilhelmer/mkdocs-localsearch',
    author='Lars Wilhelmer',
    author_email='lars@wilhelmer.de',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=1.1',
        'mkdocs-material>=5.0.0rc3'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'localsearch = mkdocs_localsearch_plugin.plugin:LocalSearchPlugin'
        ]
    }
)
