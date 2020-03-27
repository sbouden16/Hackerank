from flask import jsonify,Flask,request
app = Flask(__name__)
from temp_json_list import json_list

@app.route("/test",methods = ["GET"])
def findItem():
    return jsonify({"quiz_list":json_list["quiz"]})

@app.route("/test/<string:item_name>", methods=["GET"])
def findItems(item_name):
    itemFound = [item for item in json_list["quiz"] if item == item_name.lower()]
    if len(itemFound) > 0:
        return jsonify({"answer":json_list["quiz"][itemFound[0]]})
    else:
        return jsonify({"Problem":"There is no daa to be display"})

@app.route("/test/<string:type_name>/<string:question_name>", methods = ["POST"])
def add_to(type_name,question_name):
    #go = request
    #go2 = request.get_data()
    #go3 = request.get_json()
    if type_name in json_list["quiz"]:
        if question_name not in json_list["quiz"][type_name]:
            new_adding = {question_name: {
                question_name: request.json[question_name],
                "options": [request.json["options"]],
                "answer": request.json["answer"]
            }
            }
            json_list["quiz"][type_name].update(new_adding)
        else:
            return jsonify({"Problem": "The question name is repeated"})

    return  jsonify({f"This items were added in the list {type_name}":new_adding})
    
@app.route("/test/<string:original_name>/<string:changed_name>", methods=["PUT"])
def modify_of_type(original_name,changed_name):
    itemfound_type = [item for item in json_list["quiz"] if item == original_name.lower() or item == changed_name.lower()]
    print(itemfound_type)
    if len(itemfound_type) > 0:
        if changed_name in itemfound_type[0]:
            print("test enter this mode")
            try:
                jsl = json_list["quiz"][original_name]
            except KeyError:
                jsl = json_list["quiz"][changed_name]

            json_list["quiz"][changed_name] = jsl
            del json_list["quiz"][original_name]
            #print(json_list["quiz"])
            return jsonify({f"The following items were updated from {original_name} to {changed_name} and the full new list is": json_list})
        else:
            return jsonify({"answer":"No type found"})
    else:
        return jsonify({"answer": "No type found"})

@app.route("/test/<string:type_name>/<string:orginal_name>/<string:changed_name>", methods=["PUT"])
def modify_of(type_name,original_name, changed_name):
    #missing still to finish
    jsl = json_list["quiz"][type_name][original_name]
    itemfound_type = [item for item in json_list["quiz"]
                      if item == original_name.lower()]
    #print(itemfound_type)
    if len(itemfound_type) > 0:
        json_list["quiz"][changed_name] = jsl
        del json_list["quiz"][original_name]
        #print(json_list["quiz"])
        return jsonify({f"The following items were updated from {original_name} to {changed_name} and the full new list is": json_list})
    else:
        return jsonify({"answer": "No type found"})

@app.route("/test/<string:type_name>/<string:question_name>", methods=["DELETE"])
def delete_From(type_name,question_name):
    itemFound_type = [item for item in json_list["quiz"] if item == type_name.lower()]
    itemFound_question = [item for item in json_list["quiz"][type_name] if item == question_name.lower()]
    print(itemFound_question)
    if len(itemFound_type) > 0:
        if len(itemFound_question) > 0:
            del json_list["quiz"][itemFound_type[0]][itemFound_question[0]]
            return jsonify({f"The {itemFound_question[0]} item were erased. This is the questions remaining":json_list["quiz"][itemFound_type[0]]})
        else:
            return jsonify({"Problem":"No item match"})
    else:
        return jsonify({"Problem": "No item match"})


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)


"""
 {"q3": "Who was Nicola Tesla",
            "options": [
                "Scientist",
                "Doctor",
                "Police Officer",
                "Astrophisics"
						],
            "answer": "Scientist"
}
"""   
