from flask import Flask, request, jsonify, after_this_request
from main import return_to_user
app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
# "Avatar (2009)"
    rating = request.args.get("rating")
    movie_name = request.args.get("movie")
    jsonResp = {'movie_reccomend':return_to_user(movie_name,float(rating))}
    print(rating)
    # print(jsonResp)
    return jsonResp #jsonify(jsonResp)

if __name__ == '__main__':
    app.run(host='localhost', port=8989)