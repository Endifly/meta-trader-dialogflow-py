import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    try :
        req = request.get_json(silent=True, force=True)
        res = processRequest(req)
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r
    except :
        r = make_response("something went wrong")
        r.headers['Content-Type'] = 'application/json'
        return r

def processRequest(req):
    # Parsing the POST request body into a dictionary for easy access.
    req_dict = json.loads(request.data)
    print(req_dict)
    # Accessing the fields on the POST request boduy of API.ai invocation of the webhook
    intent = req_dict["queryResult"]["intent"]["displayName"]

    if intent == 'หุ้นน่าสนใจ':

        speech = "Tesla !"

    else:

        speech = "อะไรนะ"

    res = makeWebhookResult(speech)

    return res


def makeWebhookResult(speech):

    return {
  "fulfillmentText": speech
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 443))
    context = ('/opt/certs/ec2-122-248-219-21.ap-southeast-1.compute.amazonaws.com.crt', '/opt/certs/ec2-122-248-219-21.ap-southeast-1.compute.amazonaws.com.key')

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
