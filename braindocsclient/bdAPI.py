#!/usr/bin/env python
""" Copyright (c) 2015 ai-one inc., La Jolla CA. All rights reserved.
"""

import requests
import json

# turn off warnings
requests.packages.urllib3.disable_warnings()

class BraindocsApi(object):
    def __init__(self, username, password, baseURL):
        """ Post request to login page. Set the "verify" option to false, as the
            ai-one SSL Certificates are not presently verified. """
        self.baseURL = baseURL
        self.session = requests.Session()
        loginData = {'username':username, 'password':password}
        r = self.session.post(baseURL + '/login', data=loginData, verify=False)

    def getLibraries(self):
        r = self.session.get(self.baseURL + '/getLibraries', verify=False)
        libraries = r.json()
        return json.dumps(libraries)

    def getLibraryStatus(self, id):
        r = self.session.get(self.baseURL + '/getLibraryStatus?libraryId=' + id, verify=False);
        libraryStatus = r.json()
        return libraryStatus

    def getAnalysisResults(self):
        r = self.session.get(self.baseURL + '/getAnalysisResults', verify=False)
        analysisResults = r.json()
        return analysisResults

    def getAnalysisDetailsTextUnits(self, id):
        r = self.session.get(self.baseURL + '/getAnalysisDetailsTextUnits?analysisId=' + id, verify=False)
        analysisResults = r.json()
        return analysisResults

    def getAgents(self):
        r = self.session.get(self.baseURL + '/getAgents', verify=False)
        agents = r.json()
        return agents

    def createLibrary(self, libraryContent):
        # WARN(erh): This doesn't seem to be working
        """
        libraryContent = {
            "name":"Name of new library",
            "description":"Description of new library",
            "docs": [
                {
                    "id":"123",
                    "filename":"doc123",
                    "doc":"This is the text for document 123."
                },
                {
                    "id":"abc",
                    "filename":"docabc",
                    "doc":"This is the text for document abc."
                }
            ]
        }
        """
        r = self.session.post(self.baseURL + '/library', data=libraryContent, verify=False)
        return r.json()
