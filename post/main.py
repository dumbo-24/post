import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path, template_values))

    def post(self):
        pincode = self.request.get('pincode')
        url = "https://api.postalpincode.in/pincode/" + pincode
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        state = data[0]['PostOffice'][0]['State']
        name = data[0]['PostOffice'][0]['Name']
        block = data[0]['PostOffice'][0]['Block']
        district = data[0]['PostOffice'][0]['District']
        template_values = {
            "state": state,
            "name": name,
            "block": block,
            "district": district
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)