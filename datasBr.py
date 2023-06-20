from datetime import datetime, timezone

class Datetime:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def __str__(self):
        return self.format_data()
        

    def mes(self):
        meses = [
            'janeiro','fevereiro','março','abril','junho','julho','agosto','setembro','outubro', 'novembro', 'dezembro' ]
        mes_cadastro = self.momento_cadastro.month() - 1
        return meses[mes_cadastro]
        
    def dia_semana(self):
        dias = ['','segunda','terça','quarta','quinta','sexta','sábado','domingo']
        semana = self.momento_cadastro.weekday()
        return dias[semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
