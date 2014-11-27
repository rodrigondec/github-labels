#!/usr/bin/env python

import sys
import getpass

try:
    import requests
except:
    sys.exit('Please install requests module: pip install requests')

import json

API_TEMPLATE_URL = 'https://api.github.com/repos/{user}/{repo}/labels'
REPO_TEMPLATE_URL = 'https://github.com/{user}/{repo}/labels'
LABELS_FILE = 'labels.json'


class LabelManager(object):
    ''' Handles Github Label API '''
    def __init__(self, u, p, r, o):
        self.labels = json.loads(open(LABELS_FILE).read())
        self.auth = (u, p)
        self.baseUrl = API_TEMPLATE_URL.format(user=o if o else u, repo=r)

    def getLabels(self):
        r = requests.get(self.baseUrl, auth=self.auth)
        if r.status_code != 200:
            error = 'Error getting labels: {0}'.format(r.text)
            sys.exit(error)

        return r.json()

    def setLabels(self):
        for label in self.labels:
            r = requests.post(self.baseUrl, data=json.dumps(label),
                              auth=self.auth)

            if r.status_code != 201:
                error = 'Error creating label: {0}'.format(r.text)
                sys.exit(error)

    def deleteLabels(self):
        for label in self.getLabels():
            r = requests.delete(label['url'], auth=self.auth)
            if r.status_code != 204:
                error = 'Error deleting label: {0}'.format(r.text)
                sys.exit(error)


def main(user, password, repo, organization=None):
    manager = LabelManager(user, password, repo, organization)
    manager.deleteLabels()
    manager.setLabels()

    repo_url = REPO_TEMPLATE_URL.format(user=organization if organization
                                        else user, repo=repo)

    print
    print '---'
    print 'Everything OK. Check your new repo labels here: {}'.format(repo_url)

if __name__ == '__main__':
    user = raw_input('Please enter your github username: ')
    password = getpass.getpass('Please enter your github password: ')
    repo = raw_input('Please enter the repo name: ')
    organization = raw_input('If this is a repo from a organization please \
                              enter the organization name, if not just press \
                              enter: ')

    sure = raw_input('\nPlease enter the word CHANGE to continue. This will \
                      delete all your current labels and create a new ones: ')

    if sure.upper() != 'CHANGE':
        sys.exit('Bye')

    if user == '' or password == '' or repo == '':
        sys.exit('Invalid input')

    main(user, password, repo, organization)
