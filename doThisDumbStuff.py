#!/usr/bin/env python3

import argparse
import os
import json

parser = argparse.ArgumentParser(description='Parse a JSON that contains certs in a stupidly complex chain of tasks.')
parser.add_argument('json', metavar='json', type=str, help='path to JSON')

args = parser.parse_args()

with open(args.json) as f:
    json_contents = f.read()

json_data = json.loads(json_contents)

ca = ''.join(json_data['caCert'].partition("-----END CERTIFICATE-----")[:-1])
client = ''.join(json_data['clientCert'].partition("-----END CERTIFICATE-----")[:-1])
privateKey = ''.join(json_data['privateKey'].partition("-----END RSA PRIVATE KEY-----")[:-1])

try:
    os.mkdir('keys')
except Exception as e:
    pass

with open('keys/ca.pem', 'w') as f:
    f.write(ca)

with open('keys/client-cert.pem', 'w') as f:
    f.write(client)

with open('keys/client-key.pem', 'w') as f:
    f.write(privateKey)

print("Successfully did dumb stuff!")
