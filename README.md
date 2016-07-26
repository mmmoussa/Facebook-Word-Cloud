# Facebook Word Cloud

This project allows you to generate a word cloud based on all the Facebook
statuses that you have made. After cloning or downloading the project, go to
[Facebook's Graph API Explorer](https://developers.facebook.com/tools/explorer)
and click the button in the top-right corner that says "Get Token". From the
dropdown, choose "Get User Access Token". In the modal that pops up, select the
"user_posts" checkbox and then click the "Get Access Token" button at the
bottom. The modal should close and you should now see an "Access Token" field
with a long string of characters. Click the field to select the token, then
copy it.

In this project's files, rename the "example_config.yaml" file to "config.yaml".
Next, open "config.yaml" and replace the text "your-token-goes-here" with the
token you copied. Finally, run `pip install -r requirements.txt` in the project
directory followed by `python create_cloud.py`. The script should run for a
couple seconds and then your word cloud will open as an image for you to save.


## License

Facebook Word Cloud is available under the MIT license. See the LICENSE file
for more info.
