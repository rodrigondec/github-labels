This repo was originally a fork from https://github.com/anavallasuiza/github-labels

# Install
> It's recommended to create a python virtual env [see more at the docs](https://docs.python.org/3/tutorial/venv.html)
```shell script
pip install -r requirements.txt
```

# Env
Create a `.env` file with the following content
>Token is a personal github token [see more at the docs](https://github.com/settings/tokens).
```shell script
TOKEN=random
```

## Variables
Edit the file `runner.py` setting with the desired configs
```python
owner = 'github_owner_username'
repos = [
    'some_repo_name', 'other_repo_name' 
]
```

# Running
just run
```shell script
python runner.py
```

# Ref
## articles
- [sane-github-labels](https://medium.com/@dave_lunny/sane-github-labels-c5d2e6004b63)
## github labels
- https://github.com/Relequestual/sensible-github-labels
- https://github.com/azu/github-label-setup
- https://github.com/abdonrd/github-labels
- https://github.com/yoshuawuyts/github-standard-labels
- https://github.com/himynameisdave/git-labelmaker
## tools
- https://pygithub.readthedocs.io/en/latest/introduction.html
- https://github.com/dwyl/labels
