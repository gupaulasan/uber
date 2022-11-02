import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#Organizando dados
uber = pd.read_csv("trips_data.csv")
uber = uber.dropna()
#Transformar códigos de cidade presente nos dados iniciais para obter a informação com nome da cidade
cidades = {797 : 'Florianopolis',458:'Sao Paulo',791:'Porto Alegre',34:'Amsterdam',1369:'Pres. Prudente',1359:'Balneario Camboriu',789:'Curitiba',1277:'Londrina',335:'Ottawa'}
uber['City Name'] = uber['City'].map(cidades)
uber = uber.drop(['City','Begin Trip Lat','Begin Trip Lng','Begin Trip Address','Dropoff Lat','Dropoff Lng','Trip or Order Status'],axis=1)
uber['Product Type'] = uber['Product Type'].str.lower()

#Deixar apenas serviços de transporte de pessoas
uber = uber.drop(uber[uber['Product Type'] == 'ubereats marketplace'].index)

#Limpando horários
uber['Request Time'] = uber['Request Time'].str.replace("UTC",'')
uber['Request Time'] = uber['Request Time'].str.replace('+','')
uber['Request Time'] = uber['Request Time'].str.replace(' 0000','')

uber['Dropoff Time'] = uber['Dropoff Time'].str.replace("UTC",'')
uber['Dropoff Time'] = uber['Dropoff Time'].str.replace('+','')
uber['Dropoff Time'] = uber['Dropoff Time'].str.replace(' 0000','')

uber['Begin Trip Time'] = uber['Begin Trip Time'].str.replace("UTC",'')
uber['Begin Trip Time'] = uber['Begin Trip Time'].str.replace('+','')
uber['Begin Trip Time'] = uber['Begin Trip Time'].str.replace(' 0000','')

#Arrumando horários
uber['Request Time'] = pd.to_datetime(uber['Request Time'],utc=True)
uber = uber.set_index('Request Time')
uber.index = uber.index.tz_convert('America/Sao_Paulo')
uber = uber.reset_index()

uber['Dropoff Time'] = pd.to_datetime(uber['Dropoff Time'],utc=True)
uber = uber.set_index('Dropoff Time')
uber.index = uber.index.tz_convert('America/Sao_Paulo')
uber = uber.reset_index()

uber['Begin Trip Time'] = pd.to_datetime(uber['Begin Trip Time'],utc=True)
uber = uber.set_index('Begin Trip Time')
uber.index = uber.index.tz_convert('America/Sao_Paulo')
uber = uber.reset_index()

#Criando novas colunas 'Tempo de Viagem', 'Tempo de Resposta', 'Weekday' e 'Hour'
uber['Tempo de Viagem'] = uber['Dropoff Time'] - uber['Begin Trip Time']
uber['Tempo de Resposta'] = uber['Begin Trip Time'] - uber['Request Time']
uber['Weekday'] = uber['Request Time'].dt.weekday
uber['Hour'] = uber['Request Time'].dt.hour

dias_da_semana = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
valores = [0,1,2,3,4,5,6]
uber['Weekday'] = pd.Categorical(uber['Weekday'],categories=valores,ordered=True)
uber_por_dia = uber['Weekday'].value_counts()
uber_por_dia = uber_por_dia.sort_index()

matplotlib.RcParams.update({'font.size':30})
uber_por_dia.plot(kind='bar',figsize=(20,10),title='Viagens por dia da semana')
plt.xlabel('Dias da Semana')
plt.ylabel('Viagens')
plt.xticks(ticks=valores,labels=dias_da_semana,rotation=0)
plt.show()
plt.clf()

uber['Hour'] = pd.Categorical(uber['Hour'],categories=range(0,24),ordered=True)
uber_por_hora = uber['Hour'].value_counts()
uber_por_hora = uber_por_hora.sort_index()


uber_por_hora.plot(kind='bar',figsize=(20,10),title = 'Viagens por hora do dia')
plt.xlabel('Hora de pedido')
plt.ylabel('Viagens')
plt.xticks(rotation=0)
plt.show()
plt.clf()

#Organizando cidades
uber_por_cidades = uber['City Name'].value_counts()
city_names = list(uber_por_cidades.index)
plt.pie(uber_por_cidades,labels=city_names,autopct='%1.0f%%',pctdistance=0.85)
circle = plt.Circle((0,0),0.7,fc='white')
fig = plt.gcf()
fig.gca().add_artist(circle)
plt.title('% de uber por cidade')
plt.show()
plt.clf()

#Alterando distância para km
uber['Distance (km)'] = uber['Distance (miles)'] * 1.609344
uber.drop(['Distance (miles)'],axis=1)
uber.plot.scatter(x='Distance (km)',y='Fare Amount')
plt.xlabel('Distância (km)')
plt.ylabel('Preço (R$)')
plt.show()
