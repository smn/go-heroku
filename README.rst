go-heroku
=========

Sample Django app that interfaces with the Vumi Go HTTP API

::

	$ heroku login
	$ heroku create
	$ git push heroku master
	$ heroku config:add GO_ACCESS_TOKEN=<access-token> \
		GO_ACCOUNT_KEY=<account-key> \
		GO_CONVERSATION_KEY=<conv-key>
	$ heroku ps:scale web=1
	$ heroku open

Pass along the URL to your Vumi Go account administrator to set up the 
messages URL and you're good to go.
