# Pending Pull Reviews Git Slack Integration

This is to integrate git jenkins and slack to notify slack users about the pending pull reviews for the repos that is configured in [config.json](config/config.json)

In [config.json](config/config.json) you can ammend your additional repos to `PR_REVIEW_REPOS` key and update the `organisation` key also

#### To Test It Locally

Activate your virtual environment

```bash
source venv/bin/activate
```

In terminal run the following command

```bash
make pending-pull-reviews GITHUB_TOKEN=XXXX SLACK_HOOK=XXXX
```

Replace your git with git token and slack with webhook url respectively. In slack Webhook `https://hooks.slack.com/services/` part is common so that is given in [config.json](config/config.json) the succeding url can be replaced in the above command

#### Output Example

Ex: ![Alt text](../assests/pending-pull-review.png?raw=true "output")

#### Integrate with jenkins

In your jenkins server add the credentials with the following id as mentioned in [Jenkinsfile](Jenkinsfile).

`git_token` - Username & Password

`slack_hook` - Secret Text (Add only the succeding url part after the common path as mentioned above)

Ex:![Alt text](../assests/jenkins-credentials.png?raw=true "jenkins-credentials")

Create a pipeline script job that runs at regular intervals in jenkins and add the [Jenkinsfile](pending-pull-reviews/Jenkinsfile) as below example

Ex:![Alt text](../assests/jenkins-job.png?raw=true "jenkins-credentials")
