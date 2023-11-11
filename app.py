from flask import Flask, render_template, jsonify
import extra.helpers as helpers
import requests

app = Flask(__name__)


# Patient ID: 392648 for testing
# Azalea Judges, your auth.json should be formatted like so:
'''
{
  "Authorization": String,
  "FhirServer": String
}
'''

@app.route('/patient/<int:patient_id>')
def patient(patient_id):
    fhir_server = helpers.load_fhir_server()
    auth_token = helpers.load_auth_token()
    headers = {'Authorization': auth_token}

    response = requests.get(f'{fhir_server}/Patient/{patient_id}', headers=headers)

    if response.status_code == 200:
        patient_data = response.json()
        return jsonify(patient_data)
    else:
        return jsonify({'error ' + str(response.status_code) + ': ': 'Patient not found!'})


@app.route('/Observation/<int:patient_id>')
def observation(patient_id):
    fhir_server = helpers.load_fhir_server()
    auth_token = helpers.load_auth_token()
    headers = {'Authorization': auth_token}

    response = requests.get(f'{fhir_server}/Observation?patient={patient_id}', headers=headers)

    if response.status_code == 200:
        observation_data = response.json()
        return jsonify(observation_data)
    else:
        return jsonify({'error ' + str(response.status_code) + ': ': response.text}), response.status_code


@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/get_patient_data/<patient_id>')
def get_patient_data(patient_id):
    fhir_server = helpers.load_fhir_server()
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
