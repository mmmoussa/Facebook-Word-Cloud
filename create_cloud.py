import requests
import json
import yaml
from wordcloud import WordCloud

with open('config.yaml', 'r') as stream:
	config = yaml.load(stream)

posts = []
def getPosts(url):
	r = requests.get(url)
	result = r.json()
	for post in result['data']:
		if 'message' in post:
			posts.append(post['message'])
	if 'paging' in result:
		getPosts(result['paging']['next'])

getPosts('https://graph.facebook.com/v2.6/me/posts?access_token='
	+ config['token'] + '&limit=100')
text = ' '.join(posts)
wordcloud = WordCloud(width=800, height=400, scale=2).generate(text)
image = wordcloud.to_image()
image.show()
