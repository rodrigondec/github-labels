from github import Github, GithubException

from constants import TOKEN, OWNER, REPO, LABELS


def create_or_update_labels(owner=OWNER, repo=REPO):
    g = Github(TOKEN)

    repo = g.get_repo(f"{owner}/{repo}")

    for label in LABELS:
        try:
            repo.create_label(**label)
        except GithubException:
            repo_label = repo.get_label(label.get('name'))
            repo_label.edit(
                name=repo_label.name,
                color=label.get('color'),
                description=label.get('description')
            )


if __name__ == '__main__':
    create_or_update_labels()
