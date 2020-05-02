from flask import Flask, request, render_template, jsonify
import json
app = Flask('michal')


class data:
    def __init__(self, applicationId, sessionId, content, participants):
        self.applicationId = applicationId
        self.sessionId = sessionId
        self.content = content
        self.participants = participants

list = []

'''
    applicationId = '555'
    sessionId = ''
    messageId = ''
    participants = []
    content = 'none'
    count = 0
'''


#list.append(data(messagesList.applicationId, '2', 'messagesList.content', messagesList.participants))
#print(list[0].content)

myjson = '{"applicationId": "", "content": "","participants": ""}'

myjson = json.loads(myjson)
myjson["participants"] = ['very good', 'hgfd']
myjson["participants"].append('wer')
print(myjson["participants"])

@app.route('/')
def entry():
    return render_template('url.html')


@app.route('/AddMessage', methods=['POST', 'GET'])
def AddMessage():
    if 'applicationId' in request.values:
        myjson["applicationId"] = request.values['applicationId']
    if 'content' in request.values:
        myjson["content"] = request.values['content']
    myjson["participants"].clear()
    if 'participants1' in request.values:
        if request.values['participants1'] != '':
            myjson["participants"].append(request.values['participants1'])
    if 'participants2' in request.values:
        if request.values['participants2'] != '':
            myjson["participants"].append(request.values['participants2'])
    if 'participants3' in request.values:
        if request.values['participants3'] != '':
            myjson["participants"].append(request.values['participants3'])
    if 'participants4' in request.values:
        if request.values['participants4'] != '':
            myjson["participants"].append(request.values['participants4'])
    return render_template('AddMessage.html', data=myjson)


@app.route('/GetMessage', methods=['POST', 'GET'])
def GetMessage():
    return jsonify({'message': myjson})


@app.route('/DeleteMessage', methods=['POST', 'GET'])
def delete():
    return 'messagesList.content'


if __name__ == '__main__':
    app.run()

