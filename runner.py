from main import create_or_update_labels

owner = 'imobanco'
repos = ['income-back', 'zoop-wrapper', 'autoatendimento', 'pyCNAB240']

for repo in repos:
    print(f'Running for {repo}')
    create_or_update_labels(owner=owner, repo=repo)
