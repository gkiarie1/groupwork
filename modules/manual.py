from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/')
def get_data():
    data = {
        "Name":"Peter",
        "Age": 25,
        "Gender": "Male"
    }
    additional_info = {
            "Role": "Student",
            "School": "Moringa School",
            "Subject": "Flask"
    }    
# json.dumps takes in one argument which is why there's a need to create the dictionary
    combined_data = {
        'data': data,
        'additional_info': additional_info
    }
    # Manually encoding data into JSON format
    json_data = json.dumps(combined_data)
    
      # Calculate the content length
    content_length = len(json_data)
    
    # Setting cache control headers (no-cache, no-store)
    #'no-cache, no-store',instructs clients and intermediary caches not to cache the response at all and not to store it in any cache. 
    #This is often used for sensitive data or for responses that should always be freshly fetched from the server
    cache_control_header = 'no-cache, no-store'
    
    # Creating a Response object with JSON data and custom headers
    response = Response(json_data, status=200, content_type='application/json')
    
    # Adding additional headers
    response.headers['Content-Length'] = content_length
    response.headers['Cache-Control'] = cache_control_header
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
