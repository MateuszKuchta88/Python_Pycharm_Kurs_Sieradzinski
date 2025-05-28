animals =   [
                {
                    "name" : "chicken",
                    "legs" : 2
                },
                {
                    "name" : "dog",
                    "legs" : 4
                },
                {
                    "name" : "milipede",
                    "legs" : 100
                },
                {
                    "name" : "spider",
                    "legs" : 8
                }
            ]

out_dict =  {
                "name" : "animal",
                "legs" : 0
            }

for animal in animals:
    if animal["legs"] > out_dict["legs"]:
        out_dict.update(    {
                                "name" : animal["name"],
                                "legs" : animal["legs"]
                            })

print(out_dict)