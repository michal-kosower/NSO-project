from flask import Flask, request, render_template, jsonify
import json
app = Flask('ApiFlask')


msgJson = '{"message": [{"applicationId": "", "sessionId": "", "messageId": "", "content": "", "participants": ""}]}'
msgJson = json.loads(msgJson)


@app.route('/')
def entry():
    return render_template('url.html')


@app.route('/AddMessage', methods=['POST', 'GET'])
def AddMessage():
    if 'applicationId' in request.values:
        applicationid = request.values['applicationId']
    if 'sessionId' in request.values:
        sessionid = request.values['sessionId']
    if 'messageId' in request.values:
        messageid = request.values['messageId']
    if 'content' in request.values:
        content = request.values['content']
    participants = []
    if 'participants1' in request.values:
        if request.values['participants1'] != '':
            participants.append(request.values['participants1'])
    if 'participants2' in request.values:
        if request.values['participants2'] != '':
            participants.append(request.values['participants2'])
    if 'participants3' in request.values:
        if request.values['participants3'] != '':
            participants.append(request.values['participants3'])
    if 'participants4' in request.values:
        if request.values['participants4'] != '':
            participants.append(request.values['participants4'])
    if 'messageId' in request.values:
        msgJson["message"].append(dict(applicationId=applicationid, sessionId=sessionid, messageId=messageid, content=content, participants=participants))
    return render_template('AddMessage.html', data=msgJson["message"][-1])


@app.route('/GetMessage', methods=['POST', 'GET'])
def GetMessage():
    getJson = '{"message": [{"applicationId": "", "sessionId": "", "messageId": "", "content": "", "participants": ""}]}'
    for x in msgJson["message"]:
        if x["applicationId"] == "124":
            getJson["message"].append(dict(x))
    for x in msgJson["message"]:
        if x["sessionId"] == "124":
            getJson["message"].append(dict(x))
    for x in msgJson["message"]:
        if x["messageId"] == "124":
            getJson["message"].append(dict(x))
    return jsonify({'message': getJson})


@app.route('/DeleteMessage', methods=['POST', 'GET'])
def delete():
    return 'delete'


if __name__ == '__main__':
    app.run()
