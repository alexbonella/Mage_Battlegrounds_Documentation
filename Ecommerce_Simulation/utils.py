
import random
import pandas as pd
import hashlib


bog_coords = [(4.651600960108946, -74.12628850377475),(4.661984763443271, -74.13466548843223),(4.647569693587232, -74.10186525959672)]
buc_coords = [(7.099917472863198, -73.10730617492302),(7.07243688331635, -73.10525936227518)]
cali_coords = [(3.4287786094866717, -76.53749228193497),(3.4148803158142966, -76.54041613631288),(3.4164091379805432, -76.54751692551635)]
bar_coords = [(11.014167139030025, -74.82747678131524),(11.004041676077495, -74.83545204769058),(10.990580146449894, -74.78876005521157)]
mede_coords = [(6.163315879042265, -75.6052691935286),(6.17784573272914, -75.59141059178306),(6.198053256721469, -75.5733524126965)]

def get_pay_method(source,status_purchase,payment_online,payment_store):
    
    if source == 'Organic':
        
        payment = random.choice(payment_store)
        status = 'COMPLETED'
        order_type = 'STORE'
        
    elif source != 'Organic':
        
        payment = random.choice(payment_online)
        status = random.choice(status_purchase)
        order_type = 'ONLINE'
    
    return payment, status,order_type
        


def get_coords(city):
    
    if city == 'Bogotá':
        coords = random.choice(bog_coords)
    elif city == 'Bucaramanga':
        coords = random.choice(buc_coords)
    elif city == 'Cali':
        coords = random.choice(cali_coords)
    elif city == 'Barranquilla':
        coords = random.choice(bar_coords)
    elif city == 'Medellín':
        coords = random.choice(mede_coords)
        
    return coords 

def create_masive_users(n_users):
        
    users_bank = []
    for i in range(n_users):

        date = pd.to_datetime('today').strftime("%Y-%m-%d %H:%M:%S")
        users_bank.append(str(hashlib.sha256(f"{i} {date}".encode('utf-8')).hexdigest())[:10])
    
    return users_bank