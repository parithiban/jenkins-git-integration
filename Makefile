.DEFAULT_GOAL := explain
.PHONY: explain
explain:
	### Welcome
	#
	# Makefile for automation with Jenkins
	#  
	#       ____.              __   .__               
	#      |    | ____   ____ |  | _|__| ____   ______
	#      |    |/ __ \ /    \|  |/ /  |/    \ /  ___/
	#  /\__|    \  ___/|   |  \    <|  |   |  \\___ \ 
	#  \________|\___  >___|  /__|_ \__|___|  /____  >
	#                \/     \/     \/       \/     \/ 
	#
	# 
	### Targets
	#
	@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	#
	#
	#
	### Check


.PHONY: clean
clean: ## clean the setup
	find . -type f -name '*.pyc*' -delete
	find . -type f -name '*.log' -delete

check-token:
ifeq ($(GITHUB_TOKEN),)
	@echo "[Error] Please specify GITHUB_TOKEN"
	@exit 1;
endif

ifeq ($(SLACK_HOOK),)
	@echo "[Error] Please specify SLACK_HOOK"
	@exit 1;
endif

validate-pr-input: check-token
ifeq ($(PR_NUMBER),)
	@echo "[Error] Please specify PR_NUMBER"
	@exit 1;
endif

ifeq ($(GIT_REPO),)
	@echo "[Error] Please specify REPO_URL"
	@exit 1;
endif


.PHONY: pending-pull-reviews 
pending-pull-reviews: check-token ## check pending pull reviews
	@python scripts/pending-pull-reviews.py --git $(GITHUB_TOKEN) --slack $(SLACK_HOOK)

.PHONY: validate-pr
validate-pr: validate-pr-input ## Validate whether the pr is up-to date
	@python scripts/validate-pull-request.py --git=$(GITHUB_TOKEN) --pr=$(PR_NUMBER) --slack=$(SLACK_HOOK) --repo=$(GIT_REPO)

.PHONY: system-packages
system-packages: ## install python dependency & activate virtual environment
	pip install virtualenv
	make venv

.PHONY: venv
venv: venv/bin/activate

venv/bin/activate:
	test -d venv || virtualenv -p python3 venv
	venv/bin/pip install -U setuptools
	venv/bin/pip install -r requirements.txt
	touch venv/bin/activate

.PHONY: install
install: system-packages

all: clean install