import argparse
from helpers.gitapi import GitApi
from helpers.slack import Slack
from pathlib import Path


class ValidatePullRequest(object):
    """Check whether the pull request is valid one """

    def get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--git', action='store',
                            required=True,
                            dest='github_token',
                            help='Github token to access git repos')

        parser.add_argument('--pr', action='store',
                            required=True,
                            dest='pr_no',
                            help='Pull request number')

        parser.add_argument('--slack', action='store',
                            required=True,
                            dest='slack_url',
                            help='Communication with slack to send message')

        parser.add_argument('--repo', action='store',
                            required=True,
                            dest='repo_url',
                            help='Git repo url')

        arguments = parser.parse_args()

        return arguments


if __name__ == '__main__':
    vpr = ValidatePullRequest()
    args = vpr.get_args()
    git = GitApi(args.github_token)
    repo = Path(args.repo_url).resolve().stem
    pull_request_detail = git.get_pull_request_by_number(args.pr_no, repo)

    if pull_request_detail:
        send_slack_message = Slack(args.slack_url)
        send_slack_message.send_message(pull_request_detail)
