import os, datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# -------- Prepair -----------------------------------------
os.makedirs('templates', exist_ok=True)
s = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FlaskApp</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h2>Welcome to FlaskApp!</h2>
    <h3>{{ utc_dt }}</h3>

    <form action="{{ url_for('handle_data') }}" method="post">
    <input type="text" name="txtName">
    <input type="submit">
</form>
</body>
</html>
"""
with open('templates/index.html', 'w') as ff:
    ff.write(s)


# ----------------------------------------------------------

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['txtName']
    # your code
    # return a response
    print(projectpath)
    return f'<h1>Send: {projectpath}</h1>'


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer

    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
