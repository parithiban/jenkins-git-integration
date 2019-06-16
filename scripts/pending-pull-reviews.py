import argparse
from helpers.gitapi import GitApi
from helpers.slack import Slack


class PendingPullReviews(object):
    """Show the pending pull request for the git hub repos"""

    def get_args(self):
        parser = argparse.ArgumentParser()

        parser.add_argument('--git', action='store',
                            required=True,
                            dest='github_token',
                            help='Github token to access git repos')

        parser.add_argument('--slack', action='store',
                            required=True,
                            dest='slack_url',
                            help='Communication with slack to send message')

        arguments = parser.parse_args()

        return arguments


if __name__ == '__main__':
    ppr = PendingPullReviews()
    args = ppr.get_args()
    git = GitApi(args.github_token)
    pull_request_detail = git.pull_request_data()
    if pull_request_detail:
        post_slack_message = '<!here> \n' + pull_request_detail
        send_slack_message = Slack(args.slack_url)
        send_slack_message.send_message(post_slack_message)
