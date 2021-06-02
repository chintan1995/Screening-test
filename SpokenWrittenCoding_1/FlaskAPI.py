from flask import Flask, jsonify
from SpokenWrittenCoding_1 import SpokenToWritten as sw


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/spokentowritten/<string:input_str>')
def convert(input_str):
    output_str = sw.convert(input_str)
    result = {"input": input_str,
              "output":output_str}
    return jsonify(result)

if __name__== '__main__':
    app.run(debug=True)
