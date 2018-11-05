# CI

[![Build Status](https://travis-ci.org/catana-research/CI.svg?branch=master)](https://travis-ci.org/catana-research/CI)
[![Coverage Status](https://coveralls.io/repos/github/catana-research/CI/badge.svg?branch=master)](https://coveralls.io/github/catana-research/CI?branch=master)

## Coverage

Execute HTML report:
```bash
coverage html -d coverage_html
```


## Documentation


### Setup

Guide here: https://daler.github.io/sphinxdoc-test/includeme.html


- checkout a new document branch called 'gh-pages' (Not required)

- Add .nojekyll to /docs

- Enable GitHub pages in the repo settings page: https://github.com/catana-research/CI/settings , with the source as master branch /docs folder

Autodocumentation is provided by Sphinx, with the numpydoc plugin.

Use the Makefile to build the docs, for bash:
```bash
make builder
```
and Windows CMD:
```commandline
make.bat builder
```
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


If necessary, edit the docs/conf.py file to add all project directories to the Python path.

### Access

Documenation can be found here:

```https://catana-research.github.io/CI/index```

Which redirects to:

```https://catana-research.github.io/CI/build/html/```
