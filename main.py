from github import Github

from constants import TOKEN, OWNER, REPO, LABELS


if __name__ == '__main__':

    g = Github(TOKEN)

    repo = g.get_repo(f"{OWNER}/{REPO}")
    for label in repo.get_labels():
        label.delete()
    for label in LABELS:
        repo.create_label(**label)

