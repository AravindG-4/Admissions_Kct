from flask import Flask, request, jsonify
import main 

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'}), 200


@app.route('/process', methods=['POST'])
def process_files():
    if 'files' not in request.files:
        resp =  jsonify({'error': 'No files found in request'})
        resp.status_code = 400
        print("not found")
        return resp
    files = request.files.getlist('files')  

    print(files)
    try:
        output = main.start_processing(files)  
        return jsonify({'output': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
