from datetime import datetime
with open('./work_log.txt', mode='a') as fisier:
    fisier.writelines('\n' + datetime.now().strftime('Data: %d/%m/%Y | Ora: %H:%M'))