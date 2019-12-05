.PHONY: man test up check dist

test:
	py.test -vv --doctest-modules --cov=econ --cov-report term-missing

man:
	pandoc README.rst -s -t man -o econ.1

check:
	restview --long-description --strict

dist: man
	sudo python setup.py bdist_wheel

up:
	twine upload dist/`ls dist -rt | tail -1`


