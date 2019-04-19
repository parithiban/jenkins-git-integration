#!/usr/bin/env bash
set +x
echo "Github User Name"
echo $GITHUB_USERNAME
echo "Github Password"
echo $GITHUB_PASSWORD
echo "Slack Token"
echo $SLACK_TOKEN

echo $GITHUB_USERNAME $GITHUB_PASSWORD $SLACK_TOKEN >> fileName