from flask import Flask , jsonify , request
from pdfdrive import searchBook, getDownLoadLink, downloadBook

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def api():
    Query = str(request.args.get('Query'))
    f_new = searchBook(Query)
    l_new = getDownLoadLink(f_new[0])
    downloadBook(l_new)


if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
