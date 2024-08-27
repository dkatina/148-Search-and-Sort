from flask import Flask, request, jsonify

#http://127.0.0.1:5000/search?title=some-movie

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    print(title)
    return jsonify('success'), 200

if __name__ == '__main__':
    app.run(debug=True)