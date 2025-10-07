# Install dependencies
# pip install kagglehub pandas matplotlib seaborn

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import datetime

# Download the dataset (first time only)
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print(f"Dataset downloaded to: {path}")

# Load each CSV file
# The dataset contains multiple files
orders = pd.read_csv(f"{path}/olist_orders_dataset.csv")
order_items = pd.read_csv(f"{path}/olist_order_items_dataset.csv")
products = pd.read_csv(f"{path}/olist_products_dataset.csv")
customers = pd.read_csv(f"{path}/olist_customers_dataset.csv")
reviews = pd.read_csv(f"{path}/olist_order_reviews_dataset.csv")

print("=== Dataset Overview ===")
print(f"Orders: {orders.shape}")
print(f"Order Items: {order_items.shape}")
print(f"Products: {products.shape}")
print(f"Customers: {customers.shape}")
print(f"Reviews: {reviews.shape}")

print("\n=== Orders Data Sample ===")
print(orders.head())

print("\n=== Order Items Data Sample ===")
print(order_items.head())

print("\n=== Orders Info ===")
print(orders.info())


# Basic statistics
print("\n=== Basic Statistics ===")
print(f"Total Orders: {orders['order_id'].nunique()}")
print(f"Total Customers: {customers['customer_id'].nunique()}")
print(f"Date Range: {orders['order_purchase_timestamp'].min()} to {orders['order_purchase_timestamp'].max()}")

# Check for missing values
print("\n=== Missing Values in Orders ===")
print(orders.isnull().sum())


#  jupyter notebook



import kagglehub
import shutil
import os

# 1. تحديد المسارات
# المسار الذي ستُنزَّل فيه الملفات تلقائيًا
try:
    source_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
except Exception as e:
    print(f"حدث خطأ أثناء تحميل قاعدة البيانات: {e}")
    exit() # إيقاف الكود لو التحميل فشل

# المسار الذي تريد نقل الملفات إليه
destination_path = r"E:\ZiAd\Data Analysis Projects\Brazilian E-Commerce Dataset\New folder"

# 2. التأكد من وجود المسار الوجهة وإنشاؤه لو مش موجود
os.makedirs(destination_path, exist_ok=True)

# 3. نقل محتويات الفولدر المصدر إلى الفولدر الهدف
# Get a list of all files in the source directory
files_to_move = os.listdir(source_path)

for file_name in files_to_move:
    # Create the full path for the source file
    source_file = os.path.join(source_path, file_name)
    # Create the full path for the destination file
    destination_file = os.path.join(destination_path, file_name)
    
    # Move the file
    try:
        shutil.move(source_file, destination_file)
    except shutil.Error as e:
        # This might happen if the file already exists at the destination
        print(f"لم يتم نقل الملف {file_name} لأنه موجود بالفعل أو حدث خطأ: {e}")

print(f"تم نقل {len(files_to_move)} ملف بنجاح إلى: {destination_path}")

# 4. (خطوة اختيارية) حذف الفولدر المصدر بعد أن أصبح فارغًا
try:
    # shutil.rmtree is safer as it removes the directory and its contents (if any left)
    shutil.rmtree(source_path)
    print(f"تم حذف الفولدر المصدر المؤقت: {source_path}")
except OSError as e:
    print(f"حدث خطأ أثناء حذف الفولدر المصدر: {e}")