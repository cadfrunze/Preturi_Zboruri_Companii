from datetime import datetime

mesaj_actualizare_zi: str = datetime.now().strftime('Data: %d/%m/%Y | Ora: %H:%M')
print(mesaj_actualizare_zi)

with open('./work_log.txt', 'w') as fisier:
    fisier.writelines(mesaj_actualizare_zi)