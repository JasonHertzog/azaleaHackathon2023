from flask import Flask, render_template, jsonify
import extra.helpers as helpers
import requests

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/get_patient_data/<patient_id>')
def get_patient_data(patient_id):
    fhir_server = 'https://app.azaleahealth.com/fhir/R4/sandbox'
    headers = {
        "Authorization": helpers.load_auth_token(),
    }

    response = requests.get(f'{fhir_server}/Patient/{patient_id}', headers=headers)

    if response.status_code == 200:
        patient_data = response.json()
        return jsonify(patient_data)
    else:
        return jsonify({'error ' + str(response.status_code) + ': ': 'Patient not found!'})


if __name__ == '__main__':
    app.run(debug=True)
