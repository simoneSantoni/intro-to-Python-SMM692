import pandas as pd

df = pd.DataFrame.from_dict(
    {
        "timestamp": [
            "2017-10-08 12:03:05",
            "2020-09-07 08:09:45",
            "2021-04-11 10:12:13",
        ],
        "product": ["Darth Vader plush", "Obi-Wan Kenobi lightsaber", "Yoda pijamas"],
        "reviewer": ["Sheldon", "Sheldon", "Leonard"],
        "rating": [1, 2, 5],
    }
)
