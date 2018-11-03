# CI


## Coverage

Execute HTML report:
```bash
coverage html -d coverage_html
```


## Documentation

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