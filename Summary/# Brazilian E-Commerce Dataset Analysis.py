# Brazilian E-Commerce Dataset Analysis

#import libraries
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime

#  jupyter notebook

# Import datasets 
path = r'E:\ZiAd\Data Analysis Projects\Brazilian E-Commerce Dataset\Data'
geolocations = pd.read_csv(f'{path}/olist_geolocation_dataset.csv')
orders = pd.read_csv(f'{path}/olist_orders_dataset.csv')
order_items = pd.read_csv(f'{path}/olist_order_items_dataset.csv')
orders_payments = pd.read_csv(f'{path}/olist_order_payments_dataset.csv')
products = pd.read_csv(f'{path}/olist_products_dataset.csv')
customers = pd.read_csv(f'{path}/olist_customers_dataset.csv')
reviews = pd.read_csv(f'{path}/olist_order_reviews_dataset.csv')
category_name_translation = pd.read_csv(f'{path}/product_category_name_translation.csv') 

