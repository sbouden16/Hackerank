json_list = {
    "quiz": {
        "history": {
            "q1": {
                "question": "Which one is a correct state for water?",
                "options": [
                    "Liquid",
                    "Solid",
                    "Gas",
                    "All above"
                ],
                "answer": "All above"
            },
            
            "q2":{"question":"In which year was america discover",
                "options":[
                    "1892",
                    "1492",
                    "1592",
                    "1495"
                ],
                "answer": "1492"
                }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}

if __name__ == "__main__":

    print(json_list["quiz"]["history"]["q1"])