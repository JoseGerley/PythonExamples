from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)
print("Bogota: {}".format(bogota_date.strftime("%d/%m/%Y, %H:%M:%S")))

caracas_timezone = pytz.timezone('America/Caracas')
caracas_date = datetime.now(caracas_timezone)
print("Caracas: {}".format(caracas_date.strftime("%d/%m/%Y, %H:%M:%S")))

mexicoCity_timezone = pytz.timezone('America/Mexico_City')
mexicoCity_date = datetime.now(mexicoCity_timezone)
print("Mexico City: {}".format(mexicoCity_date.strftime("%d/%m/%Y, %H:%M:%S")))

buenosaires_timezone = pytz.timezone('America/Argentina/Buenos_Aires')
buenosaires_date = datetime.now(buenosaires_timezone)
print("Buenos Aires: {}".format(buenosaires_date.strftime("%d/%m/%Y, %H:%M:%S")))