# Marocain Name Generator 🇲🇦

names = [
    "ziyad", "ziad", "youssef", "mohamed", "hamza",
    "karim", "ayoub", "mehdi", "soufiane", "omar",
    "amine", "rachid", "bilal", "zakaria", "hicham"
    "riyad", "riad", "yassir", "mohammedamin", "yassin",
    "anis", "anass", "marwan", "samir", "ahmed",
    "abdo", "abdlah", "abdrahmen", "alae", "alaedinn"
    "nourdinn", "abdwahed", "walid", "haytam", "adam",
    "akram", "abdilah", "aziza", "abdaziz", "taha",
    "mohammedtaha", "khalid", "oussama", "montasser", "ismail"
    "iyad", "issam", "yasser", "yousri", "ilyass",
    "safwan", "salim", "kamal", "alal", "imran",
    "abdmoghit", "rayan", "younes", "aymen", "amjad"
]


years = range(2000, 2027)

output_file = "marocain_names.list"

with open(output_file, "w") as f:
    for name in names:
        for year in years:
            variations = [
                f"{name}{year}",
                f"{name.capitalize()}{year}",
                f"{name}_{year}",
                f"{name}-{year}",
                f"{name}@{year}",
                f"{name.capitalize()}@{year}"
            ]
            
            for v in variations:
                f.write(v + "\n")

print(f"[+] File '{output_file}' generated successfully!")
