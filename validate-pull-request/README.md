# Validate Pull Request Git Slack Integration

If you have set up Multibranch Pipeline in your project then this would be helpfull for the developers if there are multiple pull request in a repo. This would notify us wether our branch is outdated or it has conflicts.

#### To Test It Locally

Activate your virtual environment

```bash
source venv/bin/activate
```

In terminal run the following command

```bash
make validate-pr GITHUB_TOKEN=XXXX SLACK_HOOK=XXXXX PR_NUMBER=12 GIT_REPO=https://github.com/parithiban/jenkins-git-integration.git
```

Replace your git with git token and slack with webhook url respectively. In slack Webhook `https://hooks.slack.com/services/` part is common so that is given in [config.json](../config/config.json) the succeding url can be replaced in the above command

#### Output Example

Ex: ![Alt text](../assests/validate-pull-request.png?raw=true "output")

### Integrate with jenkins

You might already have a Jenkinsfile for multibranch pipeline ammend the script in [Jenkinsfile](Jenkinsfile).

Add the following credentials with the mentioned id in jenkins

`git_token` - Username & Password

`slack_hook` - Secret Text (Add only the succeding url part after the common path as mentioned above)

Ex:![Alt text](../assests/jenkins-credentials.png?raw=true "jenkins-credentials")
