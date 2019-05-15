import github
import json
from tabulate import tabulate
from collections import OrderedDict


class GithubApi(object):
    """Github Api to communicate with the git repo"""

    def __init__(self, token):
        self.git_token = token
        self.git_instance = github.Github(token)

    def get_configs(self):
        """Get configurations """
        with open('scripts/config.json', 'r') as f:
            config = json.load(f)
        return config

    def get_required_pull_request_reviews_count(self, repo):
        """
        Get required approving pull request review count

        # get-branch-protection>`
        :calls: `POST /gists <https://developer.github.com/v3/repos/branches/
        :param repo: string
        :rtype: bool
        """
        configs = self.get_configs()
        protected_branch = configs['DEFAULT']["PROTECTED_BRANCH"]
        total_review_count = (self.git_instance
                              .get_repo(repo)
                              .get_branch(protected_branch)
                              .get_required_pull_request_reviews()
                              )
        return total_review_count.required_approving_review_count

    def get_open_pull_request(self, repo):
        """
        Get open pull request for repos

        :calls: `POST /gists <https://developer.github.com/v3/pulls/#list-pull-requests>`
        :param repo: string
        :rtype: bool
        """
        required_review_count = self.get_required_pull_request_reviews_count(
            repo)
        open_pull_request = (self.git_instance
                             .get_repo(repo)
                             .get_pulls(
                                 state='all'
                             )
                             )
        if open_pull_request.totalCount == 0:
            return False

        data = []
        for pr in open_pull_request:
            reviews = pr.get_reviews()
            filtered = (filter
                        (lambda x:
                         x.state == "APPROVED",
                         reviews
                         )
                        )

            data.append(OrderedDict([
                ("branch_name", pr.html_url),
                ("created_by", pr.user.name),
                ("required_reviews", required_review_count),
                ("approved_reviews", len(filtered)),
                ("pending_reviews", required_review_count - len(filtered)),
            ]))
        return data

    def pull_request_data(self):
        """Get formatted pull request detailed"""

        configs = self.get_configs()
        organisation = configs['DEFAULT']["ORGANISATION"]
        protected_branch = configs['DEFAULT']["PROTECTED_BRANCH"]
        message = ''
        for repo in configs['DEFAULT']['PR_REVIEW_REPOS']:
            pull_requests = self.get_open_pull_request(
                organisation+"/"+repo)
            if pull_requests:
                message += "*Pending Pull request in " + repo + "*\n"
                message += "```\n" + tabulate(
                    pull_requests,
                    headers="keys",
                    tablefmt="fancy_grid") + "```\n"

        return message
