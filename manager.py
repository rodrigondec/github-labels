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


class LabelAPIError(Exception):
    '''Base exception for errors'''
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'API Error: {}'.format(self.message)


class LabelManager(object):
    ''' Handles Github Label API '''
    def __init__(self, u, p, r, o):
        self.auth = (u, p)

        self.apiURL = API_TEMPLATE_URL.format(user=o if o else u, repo=r)
        self.repoURL = REPO_TEMPLATE_URL.format(user=o if o else u, repo=r)

    def getAllLabels(self):
        r = requests.get(self.apiURL, auth=self.auth)
        if r.status_code != 200:
            raise LabelAPIError(r.json()['message'])

        return r.json()

    def createLabel(self, labelObject):
        r = requests.post(self.apiURL, data=json.dumps(labelObject),
                          auth=self.auth)

        if r.status_code != 201:
            raise LabelAPIError(r.json()['message'])

    def deleteLabel(self, labelURL):
        r = requests.delete(labelURL, auth=self.auth)
        if r.status_code != 204:
            raise LabelAPIError(r.json()['message'])


def main(user, password, repo, organization=None):
    manager = LabelManager(user, password, repo, organization)

    print
    print 'Deleting current Labels'
    for label in manager.getAllLabels():
        manager.deleteLabel(label['url'])

    print 'Creating new labels'

    newLabels = json.loads(open(LABELS_FILE).read())

    for label in newLabels:
        manager.createLabel(label)

    print
    print '---'
    print 'All OK. Check your labels here: {}'.format(manager.repoURL)

if __name__ == '__main__':
    user = raw_input('Please enter your github username: ')
    password = getpass.getpass('Please enter your github password: ')
    repo = raw_input('Please enter the repo name: ')
    organization = raw_input('If this is a repo from a organization please enter the organization name, if not just press enter: ')

    sure = raw_input('\nPlease enter the word CHANGE to continue. This will delete all your current labels and create a new ones: ')

    if sure.upper() != 'CHANGE':
        sys.exit('Bye')

    if user == '' or password == '' or repo == '':
        sys.exit('Invalid input')

    main(user, password, repo, organization)
