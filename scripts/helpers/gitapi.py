import github
import json
from tabulate import tabulate
from collections import OrderedDict


class GitApi(object):
    """Github Api to communicate with the git repo"""

    def __init__(self, token):
        self.git_token = token
        self.git_instance = github.Github(token)

    def get_configs(self):
        """Get configurations """
        with open('config/config.json', 'r') as f:
            config = json.load(f)
        return config

    def get_required_pull_request_reviews_count(self, repo, branch):
        """
        Get required approving pull request review count
        :calls: `POST /gists <https://developer.github.com/v3/repos/branches/#get-branch-protection`
        :param repo: string
        :param branch: string
        :rtype: integer
        """
        total_review_count = (self.git_instance
                              .get_repo(repo)
                              .get_branch(branch)
                              .get_required_pull_request_reviews()
                              )
        return total_review_count.required_approving_review_count

    def get_open_pull_request(self, item, organisation):
        """
        Get open pull request for repos

        :calls: `POST /gists <https://developer.github.com/v3/pulls/#list-pull-requests>`
        :param item: string
        :param organisation: string
        :rtype: bool
        """
        repo_detail = organisation + "/" + item['REPO']
        required_review_count = (self.get_required_pull_request_reviews_count
                                 (repo_detail,
                                  item['PROTECTED_BRANCH'])
                                 )
        open_pull_request = (self.git_instance
                             .get_repo(repo_detail)
                             .get_pulls(
                                 state='open'
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
            filtered = len(filtered) if list(filtered) else 0

            data.append(OrderedDict([
                ("branch_name", pr.html_url),
                ("created_by", pr.user.name),
                ("required_reviews", required_review_count),
                ("approved_reviews", filtered)
            ]))
        return data

    def pull_request_data(self):
        """Get formatted pull request detailed"""

        configs = self.get_configs()
        organisation = configs['DEFAULT']["ORGANISATION"]
        message = ''
        for item in configs['DEFAULT']['PR_REVIEW_REPOS']:
            pull_requests = self.get_open_pull_request(item, organisation)
            if pull_requests:
                message += "*Pending Pull request in " + item['REPO'] + "*\n"
                message += "```\n" + tabulate(
                    pull_requests,
                    headers="keys",
                    tablefmt="psql") + "```\n"

        return message

    def get_pull_request_by_number(self, number, repo):
        """
        Get details of a single pull request

        :calls: `POST /gists <https://developer.github.com/v3/pulls/#get-a-single-pull-request>`
        :param number: string
        :rtype: string
        """
        configs = self.get_configs()
        organisation = configs['DEFAULT']["ORGANISATION"]
        pull_number = int(number)

        request_data = (self.git_instance
                        .get_repo(organisation+"/"+repo)
                        .get_pull(pull_number)
                        )
        pr_state = request_data.mergeable_state
        branch = "<"+request_data.html_url+"|"+request_data.head.ref+">"
        user = request_data.user.name
        base_branch = request_data.base.ref

        if pr_state == "dirty":
            return "Hey " + user + " your branch *" + branch + "* has conflicts that must be resolved"
        elif pr_state == "behind":
            return "Hey " + user + " your branch *" + branch + "* is out of date with base branch. Pull the latest changes from " + base_branch + " into this branch."
