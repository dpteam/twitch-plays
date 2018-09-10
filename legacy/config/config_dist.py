config = {
    
    # URL to connect to Twitch IRC
    # Leave these values as-is
    'irc': {
        'server': 'irc.twitch.tv',
        'port': 6667
    },

    # Replace default values with your Twitch username and OAuth
    # Go to this page to get your OAuth token:
    # http://twitchapps.com/tmi/
    'account': {
        'username': 'username',
        'password': 'oauth:1234567890abcdefghijklmnopqrst'
    },

    # Set button throttles here
    # By default, the Start button is throttled for 10s
    'throttled_buttons': {
        'start': 10
    },

    # Set chat height here
    # By defualt, the chat height is 13 lines
    'misc': {
        'chat_height': 13
    }

}