from typing import Dict, List
from kafka import KafkaProducer
from random import random
import json

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(messages: List[Dict], *args, **kwargs):
    """
    Template code for a transformer block.

    Args:
        messages: List of messages in the stream.

    Returns:
        Transformed messages
    """
    # Specify your transformation logic here

    enrich_purchase = []

    for purchase_records in messages : 
        
        transform_records = {'purchase_ID': purchase_records['purchase_ID'], 
            'user_id' : purchase_records['user_id'] ,
            'Product_name' : purchase_records['Product_name'],
            'Pricing':purchase_records['Pricing'],
            'Comision':purchase_records['Comision'],
            'Revenue' : purchase_records['Revenue'],
            'Payment_Mehtod':purchase_records['Payment_Mehtod'],
            'Status' : purchase_records['Status'],
            'Order_Type' : purchase_records['Order_Type'],
            'City':purchase_records['City'],
            'Location': purchase_records['Location'],
            'Latitud' : purchase_records['Latitud'],
            'Longitud' :  purchase_records['Longitud'],
            'Source':purchase_records['Source'],
            'Brand' : purchase_records['Brand'],
            'Category': purchase_records['Category'],
            'Created_at': purchase_records['Created_at'],
            'Date' : purchase_records['Created_at'].split()[0],
            'Hour' : int(purchase_records['Created_at'].split()[1].split(':')[0])
            }
        
        enrich_purchase.append(transform_records)

    return enrich_purchase
