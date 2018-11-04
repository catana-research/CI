# CI


Demonstrates autoamted build and testing with Travis and code coverage with Coveralls. 

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