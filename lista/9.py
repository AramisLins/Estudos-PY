def converte(hora,minuto,segundo):
    res = (hora * 3600) + (minuto * 60) + segundo
    print(res)
    
    
    
    
horas = int(input('Digite as horas: '))
minutos= int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
converte(horas,minutos,segundos)
