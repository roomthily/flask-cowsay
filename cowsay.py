from flask import Flask
from flask_slack import Slack
app = Flask(__name__)

slack = Slack(app)

import subprocess


@slack.command('/cowsay', token="", team_id="", methods=['POST'])
def say_it(**kwargs):
    text = kwargs.get('text')

    s = subprocess.Popen(
        'cowsay "{0}"'.format(text),
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = s.communicate()
    return slack.response(stdout)


app.add_url_rule('/', view_func=slack.dispatch)


if __name__ == "__main__":
    app.debug = True
    # app.run(host='0.0.0.0')
    app.run()
