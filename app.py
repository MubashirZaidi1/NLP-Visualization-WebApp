from flask import Flask, render_template, send_file, jsonify
import json

app = Flask(__name__ , static_folder='static' , template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/character_links')
def character_links():
    # fileReading 
    with open('templates/networkDataset.json', 'r') as file:
        data = json.load(file)

    return render_template('forceDirected.html', data=json.dumps(data))
#rerouting
@app.route('/tree_hierarchy')
def tree_hierarchy():
    return render_template('mubashir.html')

if __name__ == '__main__':
    app.run(debug=True)
