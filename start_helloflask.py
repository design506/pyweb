from helloflask import app

#app.run(host='0.0.0.0', port=80 )  # 127.0.0.1 == localhost
app.run(debug=True, port=80, host='0.0.0.0')