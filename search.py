import requests
import json
from flask import Flask, request, session
from flask import jsonify
from flask_cors import CORS

def getGzhJson(url, myCookie):
	# cookie need change!
	# myCookie = ''''''
	headers = {
	'cookie': myCookie,
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
	}
	try:
		r=requests.get(url, headers = headers)
		r.raise_for_status()
		r.encoding='utf-8'
		return json.loads(r.text)
	except Exception as e:
		print(e)
		return []

app = Flask(__name__)
cors = CORS(app, resources={
	r"/bizlist": {"origins": "*"},
	r"/articlelist": {"origins": "*"},
	})

@app.route('/bizlist',methods=['GET'])
def bizList():
	cookie = request.headers.get('Cookies')
	token = request.headers.get('Token')
	if not (cookie):
		return ""
	queryKey = request.args.get('query')
	if not (queryKey):
		return ""
	url = "https://mp.weixin.qq.com/cgi-bin/searchbiz?lang=zh_CN&action=search_biz&begin=0&count=5&query=%s&token=%s&f=json"%(queryKey, token)
	rst = getGzhJson(url, cookie)
	jsonList = rst['list']
	return jsonify(jsonList)

@app.route('/articlelist',methods=['GET'])
def articleList():
	cookie = request.headers.get('Cookies')
	token = request.headers.get('Token')
	if not (cookie):
		return ""
	fakeid = request.args.get('fakeid')
	if not (fakeid):
		return ""
	queryKey = request.args.get('query')
	if not (queryKey):
		queryKey = ""
	url = "https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=10&fakeid=%s&type=9&query=%s&token=%s&lang=zh_CN&f=json"%(fakeid, queryKey, token)
	jsonList = getGzhJson(url, cookie)['app_msg_list']
	return jsonify(jsonList)

if __name__ == '__main__':
	 app.run(host='localhost', port = 10845)

