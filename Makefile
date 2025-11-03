# Local run of pytest and flake8 (but not coverage of pytest) and write badges.
#
# This Makefile presumes an activated virtual environment of Python.  By flag
# `-l`, the badges are created locally, independent of genbadge's default to
# reach out to external resources by shields.io.
#
# genbadge:   https://github.com/smarie/python-genbadge and
#             https://pypi.org/project/genbadge/
# shields.io: https://shields.io/

default:
	@echo "Tap the tabulator key twice to display the options available."

analysis_setup:
	pip install flake8
	pip install genbadge[tests,flake8]
	pip install pyclean
	pip install pytest

flake8_analysis:
	-rm -r reports
	-rm flake8stats.txt

	flake8 src/app/greeter.py --exit-zero --statistics --count \
		--tee --output-file flake8stats.txt \
		--max-line-length 79

flake8_badge:
	genbadge flake8 -i flake8stats.txt -lv && \
		mkdir -p badges && mv flake8-badge.svg ./badges

pytest_analysis:
	pytest --rootdir=src --cache-clear --junitxml=junit.xml -v

pytest_badge:
	genbadge tests -i junit.xml -lv && \
		mkdir -p badges && mv tests-badge.svg ./badges

remove_all_but_the_badges:
	pyclean . --debris

	-rm flake8stats.txt
	-rm junit.xml

