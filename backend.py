from flask import Flask, request, jsonify
import requests
import re

app = Flask(__name__)

# Replace with actual Instagram API endpoint and access token
INSTAGRAM_API_URL = 'https://graph.instagram.com'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

@app.route('/fetch_comments', methods=['GET'])
def fetch_comments():
    post_id = request.args.get('post_id')
    if not post_id:
        return jsonify({'error': 'post_id is required'}), 400
    
    url = f"{INSTAGRAM_API_URL}/{post_id}/comments"
    params = {
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch comments'}), response.status_code
    
    comments = response.json().get('data', [])
    return jsonify(comments)

@app.route('/fetch_hashtags', methods=['GET'])
def fetch_hashtags():
    post_id = request.args.get('post_id')
    if not post_id:
        return jsonify({'error': 'post_id is required'}), 400
    
    url = f"{INSTAGRAM_API_URL}/{post_id}/comments"
    params = {
        'access_token': ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch comments'}), response.status_code
    
    comments = response.json().get('data', [])
    hashtags = []
    for comment in comments:
        hashtags.extend(re.findall(r'#\w+', comment.get('text', '')))
    
    return jsonify(list(set(hashtags)))

if __name__ == '__main__':
    app.run(debug=True)
