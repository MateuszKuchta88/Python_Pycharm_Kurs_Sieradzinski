animals =   [
                {
                    "name" : "dog",
                    "race" : "German dog"
                },
                {
                    "name" : "dog",
                    "race" : "Hungarian dog"
                },
                {
                    "name" : "dog",
                    "race" : "Chow Chow"
                },
                {
                    "name" : "cat",
                    "race" : "House cat"
                }
            ]

out_dict =  {
                "name" : "animal",
                "race" : "race",
                "length" : 0
            }

for animal in animals:
    if len(animal["race"]) > out_dict["length"]:
        out_dict.update(    {
                                "name" : animal["name"],
                                "race" : animal["race"],
                                "length": len(animal["race"])
                            })

print(out_dict)