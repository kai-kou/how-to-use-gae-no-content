from flask import Flask, jsonify, make_response

app = Flask(__name__)

# GAEでも動作する
@app.route('/good_no_content', methods=['GET'])
def good_no_content():
  response = make_response('', 204)
  response.mimetype = app.config['JSONIFY_MIMETYPE']
  return response
  # or
  # return jsonify(''), 204

# GAEでエラーになる
@app.route('/bad_no_content', methods=['GET'])
def bad_no_content():
  response = make_response(jsonify(None), 204)
  return response
  # or
  # return jsonify(None), 204


if __name__ == '__main__':
  app.run()
