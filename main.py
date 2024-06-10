import requests

# # cat/

# print(dir(requests))
# url = "https://cataas.com/cat"
# response = requests.get(url)

# if response.status_code == 200:
#     content = response.content
#     with open("cat.png", "wb") as file:
#         file.write(content)

# # cat/tage

# color = input("Mushuk rangini kiriting: ")

# url = f"https://cataas.com/cat/{color}"
# response = requests.get(url)

# if response.status_code == 200:
#     content = response.content
#     with open("cat.png", "wb") as file:
#         file.write(content)

# # cat/gif



url = f"https://cataas.com/cat/gif"
response = requests.get(url)

if response.status_code == 200:
    content = response.content
    with open("cat.gif", "wb") as file:
        file.write(content)
