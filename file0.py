from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'input_data' not in data:
            raise ValueError('Input data is missing')
        input_data = data['input_data']
        # Perform prediction using DeepSeek-Coder V2 model
        prediction = deepseek_coder_v2_model.predict(input_data)
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()