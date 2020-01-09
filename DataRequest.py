import requests

url = "https://erp.isskindiss.de"
test_endpoint = "/api/method/frappe.auth.get_logged_user"

endpoints = {
    'Quotation': "/api/resource/Quotation/",
    'User': "api/resource/User/"
}

headers = {
    'Authorization': "token 35b5f4cf0c882cb:a0c9b073da51a8f"
}


def set_token(token):
    headers['Authorization'] = "token {token}".format(token=token)


def get_data(endpoint, docid):
    target = endpoints[endpoint]
    response = requests.request("GET", url + target + docid, headers=headers)
    return response


def get_ids(endpoint):
    target = endpoints[endpoint]
    response = requests.request("Get", url + target, headers=headers)
    return response
