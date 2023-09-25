from data_base import END_POINT_SHEETY, AUTHORIZATION_SHEETY
import requests
header: dict = {
    'Content-Type': 'application/json',
    'Authorization': AUTHORIZATION_SHEETY
}

# cerere_SHEETY_get = requests.get(url=str(END_POINT_SHEETY), headers=headers)
# print(cerere_SHEETY_get.text)
# editare: dict = {
#     'price': {
#         'city': 'Nuremberg',
#         'lowestPrice': '120'
#     }
# }
# editare_SHEETY_editare = requests.post(url=str(END_POINT_SHEETY), headers=header, json=editare)
# # editare_SHEETY_editare.raise_for_status()
# print(editare_SHEETY_editare.text)
cerere = requests.get(url=str(END_POINT_SHEETY), headers=header)
print(cerere.text)