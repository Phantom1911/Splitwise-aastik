def sanitise_response(response):
    if 'err_msg' in response.keys():
        return response['err_msg']
    if 'success':
        pass
