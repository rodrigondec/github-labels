from main import create_or_update_labels


repos = ['income-back', 'zoop-wrapper', 'autoatendimento', 'pyCNAB240']

for repo in repos:
    print(f'Running for {repo}')
    create_or_update_labels(repo=repo)
