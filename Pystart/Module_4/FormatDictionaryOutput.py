# Dictionary declaration
programmers =   [
                    {   "id":1,
                        "job_title":"junior developer",
                        "name":"John",
                        "programming_language": ["python"]
                    },
                    {   "id": 2,
                        "job_title": "senior developer",
                        "name": "Mark",
                        "programming_language": ["python", "php"]
                     },
                    {   "id":3,
                        "job_title":"stuff developer",
                        "name":"Alex",
                        "programming_language": ["php", "python"]
                    },
                    {   "id": 4,
                        "job_title": "junior developer",
                        "name": "Bart",
                        "programming_language": ["javascript", "php"]
                     },
                    {   "id":5,
                        "job_title":"senior developer",
                        "name":"Carl",
                        "programming_language": ["python", "javascript", "php"]
                    },
                    {   "id": 6,
                        "job_title": "junior developer",
                        "name": "Martha",
                        "programming_language": ["php", "javascript"]
                     }
                ]

# Empty list and dictionary declaration
out_dict = {}
lans = []

# Loop for insering data into properly structurized output
for programmer in programmers:
    for language in programmer["programming_language"]:
        if language not in lans: #if there is no such key as this language, insert one
            out_dict[language] = {"quantity":0, "names": []}
            lans.append(language)

        # Appending new values to dictionary
        out_dict[language]["quantity"] += 1
        out_dict[language]["names"].append(programmer["name"])
        
# Printing output
print(out_dict)
