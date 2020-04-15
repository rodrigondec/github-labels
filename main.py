from github import Github, GithubException

from constants import TOKEN, OWNER, REPO, LABELS


if __name__ == '__main__':

    g = Github(TOKEN)

    repo = g.get_repo(f"{OWNER}/{REPO}")

    for label in LABELS:
        try:
            repo.create_label(**label)
        except GithubException as e:
            print(e)
            repo_label = repo.get_label(label.get('name'))
            repo_label.edit(
                name=repo_label.name,
                color=label.get('color'),
                description=label.get('description')
            )
