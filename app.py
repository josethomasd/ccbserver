import os

from flask import Flask
from flask import render_template
from flask import jsonify

from chat import talk, session_talk
from chat.base import kernel

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("documentation.html",title="Documentation")

@app.route("/website/api/msg/",methods=['GET'])
@app.route("/website/api/msg/sessionid/<int:sessionid>/",methods=['GET'])
@app.route("/website/api/msg/sessionid/<int:sessionid>/un/",methods=['GET'])
@app.route("/website/api/msg/<msg>/sessionid/<int:sessionid>/un/<uname>",methods=['GET'])
def website(msg="no input",sessionid=None,uname=None):
	message = ' '.join(msg.split("+"))
	# message = "what are you"

	if not sessionid:
		error = "No session id provided"
		rsp_list = [{'output':error}]
		return jsonify({'response':rsp_list})

	if not uname:
		error = "No username was provided"
		rsp_list = [{'output':error}]
		return jsonify({'response':rsp_list})
	
	kernel.setPredicate("uname", uname, sessionid)
	bot_response = session_talk(message,sessionid)
	
	# checking if a matched response is found.
	if not bot_response:
		bot_response = "error"
	
	rsp_list = [{'output':bot_response}]
	return jsonify({'response':rsp_list})


@app.route("/api/msg/",methods=['GET'])
@app.route("/api/msg/<msg>",methods=['GET'])
def api(msg="no input",sessionId=None):
	message = ' '.join(msg.split("+"))
	# message = "what are you"
	
	bot_response = talk(message)
	
	# checking if a matched response is found.
	if not bot_response:
		bot_response = "error"
	
	rsp_list = [{'output':bot_response}]
	return jsonify({'response':rsp_list})

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
