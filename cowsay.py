from flask import Flask
from flask import request, abort
app = Flask(__name__)

import subprocess
import urlparse

_template = """
     | %s |

          ^__^
          (oo)\\_______
          (__)\\       )\\/\\
              ||----w |
              ||     ||
"""


@app.route('/', methods=['POST'])
def say_it():
    text = urlparse.unquote(request.form['text'])
    token = request.form['token']
    if token != 'YOUR TOKEN':
        abort('Invalid team token', 403)

    parts = text.split(':')
    if parts[0] == 'base':
        # only return the cow
        return _template % parts[1]

    s = subprocess.Popen(
        'cowsay "{0}"'.format(text),
        shell=False,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = s.communicate()
    return stdout


if __name__ == "__main__":
    app.run(host='0.0.0.0')
