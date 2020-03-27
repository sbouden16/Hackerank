def hello_world(request):
    var = ["message", "text", "try"]
    request_json = request.get_json()
    w = {}
    x = {"1": "test1", "2": "test2", "3": "test3"}
    if request.args:
        if [i in request.args for i in var].any():
            for i in var:
                if i in request.args:
                    w[i] = request.args.get(i)
                    # return reuest.args.get(i)

    elif request_json:
        if [i in request_json for i in var]:
            for i in var:
                if i in request_json:
                    w[i] = request_json[i]
                    # return request_json[i]

    else:
        return "Fuck world"
    return w








