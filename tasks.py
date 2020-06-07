from invoke import task
import re

@task
def test(c):
    c.run("coverage run -m unittest discover")

@task(test)
def cov(c):
    c.run("coverage report")
    c.run("coverage html")

@task
def xinstall(c):
    c.run("pip uninstall -y aed-ds")
    c.run("rm -rf dist/ build/ *.egg-info/")
    c.run("python setup.py bdist_wheel")
    c.run("pip install --find-links=./dist aed_ds")
