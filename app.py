#!/usr/bin/python
from __future__ import division
from jira import JIRA
import urllib, urlparse, json, csv, sys, bottle
from bottle import run, route, static_file, view, template, post, request

# For summing, interpret NoneType errors as "0"
def intit(i):
    try: 
        x = int(i)
    except TypeError:
        x = 0    
    return x
    
# try to get a filter parameter
def filter():
        try:
            query = "filter=" + request.query['filter']
        except KeyError:
            query = "filter=60456"
        return query
    
# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

def connect_to_jira():
   jira_options = { 'server': 'https://jira.cengage.com/'}

   try:
       jira = JIRA(options=jira_options, basic_auth=('jfishwick', 'VirileAgitur!'))
   except Exception as e:
       jira = None

   return jira

jira = connect_to_jira()
#issue = jira.issue('DIG-15865')
meta = jira.editmeta( 'DIG-15865' )
dig = jira.project('DIG')

components = [ c.name for c in jira.project_components(dig) ]
portfolios = [ portfolio[u'value'] for portfolio in meta['fields']['customfield_21331']['allowedValues'] ]
disciplines = [ discipline[u'value'] for discipline in meta['fields']['customfield_10030']['allowedValues'] ]



app = application = bottle.Bottle()

@app.route('/')
def home():
    redirect('/criteria')

@app.route('/critera')
def critera():
    return template('choose')

@app.route('/critera/<name>')
def critera(name):
    selections =  request.query.getall('val[]')
    query = filter()
    points = []
    if selections:
        for index, selection in enumerate(selections):
            selection = urllib.unquote_plus(selection)
            if selection == "kindergarten":
                return "<img src='http://25.media.tumblr.com/tumblr_m7e23tzscj1rvcjd7o3_250.gif' />"
            if name == "users":
                filter1 = jira.search_issues(query + ' AND "Media Producer" in (' + selection + ')', maxResults=9999)
            else:
                filter1 = jira.search_issues(query + ' AND ' + name[:-1] + '="' + selection + '"', maxResults=9999)
            points.append ( sum([intit(issue.fields.customfield_10792) for issue in filter1]) )

        return template('selection', selections = [urllib.unquote_plus(selection) for selection in selections], criteron = name[ :-1], points = points)
    elif name == "users":
        return template('users')
    else:
        return template('critera', vars = eval(name))   

@app.route('/critera/<name>/<sub>')
def sub(name, sub):
    selection = urllib.unquote_plus(sub)
    criteron = name[ :-1]
    query = filter()

    filter2 = jira.search_issues(query + ' AND ' + criteron + '="' + selection + '"', maxResults=9999)

    points2 = [intit(issue.fields.customfield_10792) for issue in filter2]
    return selection + ": " + str(sum(points2))

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')

class StripPathMiddleware(object):
    '''
    Get that slash out of the request
    '''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(app),
        server='paste',
        host='10.160.22.212',
        reloader=True,
        port=8080)
