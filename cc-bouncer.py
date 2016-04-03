import requests as re
from flask import Flask, jsonify
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/<comp>/<my_filter>')
def rankings_bouncer(comp, my_filter):
	x = re.get('https://www.codechef.com/api/rankings/'+comp+'?sortBy=rank&order=asc&page=1&itemsPerPage=25&filterBy='+my_filter).json()
	#print x.text
	return jsonify(result=x)

@app.route("/")
def helloWorld():
  return "Hello, world! <a href='https://github.com/rhnvrm/codechef-api-bouncer'>Fork me on GitHub!</a>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


