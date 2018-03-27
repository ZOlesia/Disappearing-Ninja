from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def no_ninjas():
	return render_template('index.html')

@app.route('/ninja')
def show_ninjas():
	return render_template('ninjas.html')

@app.route('/ninja/<color>')
def show_ninjas_by_color(color):
	print color
	return render_template('colors.html', colors = color)





app.run(debug=True)