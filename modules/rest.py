# Restful api
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) 

# Api is a class provided by Flask-RESTful for creating a RESTful API instance
#  It sets up routing and request handling specifically tailored for building RESTful APIs.
api = Api(app) 

class ReturnJSON(Resource):
    def get(self):
        data = {
            "Name":"Ian",
            "Age": 30,
            "Gender": "Male"
        } 
        additional_info = {
            "Role": "Technical Mentor",
            "School": "Moringa School",
            "Subject": "Flask"
        }
        return {
            "data": data,
            "additional_info": additional_info
        }

# add resource is a method provided by Flask-RESTful's Api class for adding resources to the API.
# It is used to map a resource class to a specific URL endpoint.
api.add_resource(ReturnJSON, '/') 


if __name__=='__main__': 
	app.run(debug=True)
