explain:
	### Welcome
	#
	# Makefile for automation with any Hosted Servers that Group Internal Business Systems manage
	#
	### Check jenkins version
	#
	# Check jenkins version is up to date
	#  -> $$ make jenkins-version-check
	#
	#
	###

.PHONY: jenkins-version-check
jenkins-version-check:
	@python scripts/jenkins-version.py

check-token:
ifeq ($(GITHUB_TOKEN),)
	@echo "[Error] Please specify GITHUB_TOKEN"
	@exit 1;
endif

ifeq ($(SLACK_TOKEN),)
	@echo "[Error] Please specify SLACK_TOKEN"
	@exit 1;
endif

# .PHONY: pending-pull-reviews
# branch-check: check-token
# 	@python scripts/pending-pull-reviews.py --git $(GITHUB_TOKEN) --slack $(SLACK_TOKEN)

.PHONY: branch-check
branch-check: 
	echo "false"

.PHONY: install-python-deps
install-python-deps:
	pip install -r requirements.txt
