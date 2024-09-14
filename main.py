# Write Python 3 code in this online editor and run it.
from datetime import date
import holidays
import pandas as pd
import numpy as np


def pu_ntnf_semestral(data_atual, data_vencimento, taxa):
    inicio = data_atual 
    final = data_vencimento 
    valor_cupom = 0.0488 * 1000
    valor_de_face = 1000
    taxa_efetiva = taxa/100
    feriados_brasil = holidays.Brazil()
    datas = []
    
    while data_atual.year <= data_vencimento.year:
        jan = date(data_atual.year, 1, 1)
        jul = date(data_atual.year, 7, 1)
        datas.append(jan)
        datas.append(jul)
        data_atual = data_atual.replace(year = data_atual.year + 1)
    
    datas = [i for i in datas if i >= inicio and i <= final ] 
    # Gera um range de datas entre a data inicial e final
    datas_range = pd.date_range(inicio, final, freq='B')

    # Filtra os feriados que estão dentro do intervalo de datas
    feriados_no_periodo = pd.to_datetime([i for i in datas_range if i in feriados_brasil]).date.tolist()

    dias_uteis = np.busday_count(begindates=inicio, enddates=datas, holidays = feriados_no_periodo).tolist()
    dus = int(np.busday_count(begindates=inicio, enddates=final, holidays = feriados_no_periodo))
    # calculando pu
    pu = sum(valor_cupom/(1+taxa_efetiva)**(i/252) for i in dias_uteis) + valor_de_face/(1+taxa_efetiva)**(dus/252)
    
    return pu
    
    
inicio = date(2020, 4, 30)
final = date(2021, 1, 1)
taxa = 2.96

pu_ntnf_semestral(data_atual=inicio, data_vencimento=final, taxa = taxa)

