try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='CI',
    version='1.0',
    author='Author',
    author_email='author_email@email.com',
    packages=['core'],
    url='https://github.com/catana-research/CI',
    license='LICENSE.txt',
    description='Useful package-test-related stuff.',
    test_suite='test.test_complex'
)