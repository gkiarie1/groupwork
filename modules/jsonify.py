# Returning Json response using jsonify
# Import flask 
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ReturnJSON():
    if request.method == 'GET':
        # input data to be displayed
        data = {
            "Name": "Jane",
            "Age": 18,
            "Gender": "Female"
        }
        additional_info={
            "Role":"Student",
            "School": "Moringa School",
            "Subject": "Flask",
        }
        # output the data
        # set your own response codes
        return jsonify(data,additional_info),201

if __name__ == '__main__':
    app.run(debug=True)
