import os
import flask
import files as fls
app = flask.Flask(__name__)


@app.route('/index.html')
def home():
    return flask.render_template('index.html')
@app.route('/hi')
def fetch():
    #print('what in the fuckng world')
    return 'his this is reponse'
@app.route('/index2.html')
def index2():
    return flask.render_template('index2.html')

@app.route('/files')
def sendNumber():
    current_dir = flask.request.args.get('dir', os.getcwd())
    command= flask.request.args.get('command')
    if command=='back':
        print('going backkk')
        return flask.jsonify(fls.up_dir(current_dir,'\\'))
        
        
    else:
        if current_dir=='default':                #if the page is just initialized
            return flask.jsonify(os.getcwd())
        else:
            return flask.jsonify(fls.list_folders(current_dir))
    #print(current_dir,'hellooooo')
    return 'hi'
    

@app.route('/')
def main():
    return flask.render_template('index.html')

if __name__ == '__main__':
    extra_files = [
        os.path.join(app.root_path, 'templates/index.html'),  # Single file
        os.path.join(app.root_path, 'static/style/style.css'), 
        os.path.join(app.root_path, 'static\scripts\index.js'),                                                        # Another file
    ]

    # Optionally, watch an entire directory
    
    app.run(debug=True, extra_files=extra_files)