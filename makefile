VENV = .venv
PYTHON = $(CURDIR)/$(VENV)/bin/python
PIP = $(PYTHON) -m pip

.PHONY: all install clean run debug lint lint-strict

all: install

install:
	@set -eu; \
	python3 -m venv "$(CURDIR)/$(VENV)"; \
	echo ".venv créé !"; \
	$(PIP) install -q flake8 > /dev/null; \
	$(PIP) install -q mypy > /dev/null; \
	echo; \
	printf "\033[32mDépendances installées avec succès.\033[0m\n"

run:
	$(PYTHON) pac-man.py config.json

debug:
	$(PYTHON) -m pdb pac-man.py config.json

lint:
	$(PYTHON) -m flake8 . --exclude=.venv,.mlx_CLXV_tmp
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores 
		--ignore-missing-imports --disallow-untyped-defs 
		--check-untyped-defs --exclude "(^|/)(\.venv|\.mlx_CLXV_tmp)/"

lint-strict:
	$(PYTHON) -m flake8 . --exclude=.venv,.mlx_CLXV_tmp
	$(PYTHON) -m mypy . --strict --exclude "(^|/)(\.venv)/"

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf */__pycache__
	rm -rf "$(VENV)"
