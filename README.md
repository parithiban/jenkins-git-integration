# Jenkins Git integration....

[![Pull-Requests](https://img.shields.io/github/issues-pr/parithiban/jenkins-git-integration.svg?color=blue&style=plastic)](https://github.com/parithiban/jenkins-git-integration/pulls/)
[![Issues](https://img.shields.io/github/issues-raw/parithiban/jenkins-git-integration.svg?style=plastic)](https://github.com/parithiban/jenkins-git-integration/issues)

[![GitHub contributors](https://img.shields.io/github/contributors/parithiban/jenkins-git-integration.svg?style=plastic&color=blue)](https://GitHub.com/parithiban/jenkins-git-integration/graphs/contributors/)
![Last Commit](https://img.shields.io/github/last-commit/parithiban/jenkins-git-integration.svg?style=plastic)

[![GitHub forks](https://img.shields.io/github/forks/parithiban/jenkins-git-integration.svg?style=social)](https://github.com/parithiban/jenkins-git-integration/network/)
[![GitHub stars](https://img.shields.io/github/stars/parithiban/jenkins-git-integration.svg?style=social)](https://github.com/parithiban/jenkins-git-integration/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/parithiban/jenkins-git-integration.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/parithiban/jenkins-git-integration/watchers/)
[![GitHub followers](https://img.shields.io/github/followers/parithiban.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/parithiban?tab=followers)

This is a repo that handles jenkins git integrations with slack to remind users about the pending actions to do

## Requirements

If you are wanting to build and develop this, you will need the following items installed.

- Python version 3.7+
- Pip
- Jenkins

## Installation Steps

To create a GitHub token refer [link](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)

To create a incoming webhook refer [link](https://api.slack.com/incoming-webhooks)

#### Clone the Repo

```bash
git clone https://github.com/parithiban/jenkins-git-integration.git
cd jenkins-git-integration
```

#### Install dependency

```bash
make all
```

#### Activate your virtual environment

```bash
source venv/bin/activate
```

#### Multibranch Pipeline Setup Reference

[Multibranch Setup](https://jenkins.io/doc/book/pipeline/multibranch/)

#### Pending Pull Reviews

[Setup for pending pull reviews](/pending-pull-reviews)

#### Validate Pull Request

[Setup for validate pull request](/validate-pull-request)
