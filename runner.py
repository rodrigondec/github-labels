from main import create_or_update_labels, delete_existing_labels

owner = 'rodrigondec'
repos = [
    'github-labels',
]

for repo in repos:
    print(f'Running for {repo}')
    delete_existing_labels(owner=owner, repo=repo)
    create_or_update_labels(owner=owner, repo=repo)
