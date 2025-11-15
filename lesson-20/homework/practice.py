import pandas as pd
import sqlite3

# ============================================================
# Homework 20 — Chinook Database Analysis
# ============================================================

# Connect to Chinook SQLite database
conn = sqlite3.connect("task\\chinook.db")

# ---------------- 1. Customer Purchases Analysis ----------------

# Read necessary tables
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice", conn)
invoice_items = pd.read_sql("SELECT InvoiceId, UnitPrice, Quantity FROM InvoiceLine", conn)

# Merge invoices with invoice_items
invoice_details = pd.merge(invoice_items, invoices, on='InvoiceId', how='left')

# Calculate total amount per invoice line
invoice_details['Total'] = invoice_details['UnitPrice'] * invoice_details['Quantity']

# Total spent per customer
customer_total = invoice_details.groupby('CustomerId')['Total'].sum().reset_index()

# Merge with customer info
customer_total = pd.merge(customer_total, customers, on='CustomerId', how='left')

# Top 5 customers by total purchase
top5_customers = customer_total.sort_values(by='Total', ascending=False).head(5)
print("Top 5 customers by total purchase:\n", top5_customers[['CustomerId','FirstName','LastName','Total']], "\n")


# ---------------- 2. Album vs Individual Track Purchases ----------------

# Read Tracks and InvoiceLines
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)
invoice_lines = pd.read_sql("SELECT InvoiceId, TrackId FROM InvoiceLine", conn)
invoices_customers = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoice", conn)

# Merge invoice_lines with invoice_customer info
invoice_tracks = pd.merge(invoice_lines, invoices_customers, on='InvoiceId', how='left')

# Total tracks per album
album_tracks_count = tracks.groupby('AlbumId')['TrackId'].count().reset_index().rename(columns={'TrackId':'TotalTracks'})

# Tracks purchased by each customer per album
customer_album = pd.merge(invoice_tracks, tracks, on='TrackId', how='left')
customer_album_count = customer_album.groupby(['CustomerId','AlbumId'])['TrackId'].count().reset_index().rename(columns={'TrackId':'PurchasedTracks'})

# Merge with total tracks per album
customer_album_count = pd.merge(customer_album_count, album_tracks_count, on='AlbumId', how='left')

# Determine preference: full album vs individual tracks
customer_album_count['PrefersFullAlbum'] = customer_album_count['PurchasedTracks'] >= customer_album_count['TotalTracks']

# Count customers preferring individual tracks vs full albums
pref_summary = customer_album_count.groupby('CustomerId')['PrefersFullAlbum'].all().reset_index()
pref_summary['Preference'] = pref_summary['PrefersFullAlbum'].apply(lambda x: 'Full Album' if x else 'Individual Tracks')

# Calculate percentage
pref_percentage = pref_summary['Preference'].value_counts(normalize=True) * 100
print("Customer preference percentages:\n", pref_percentage, "\n")

# Close connection
conn.close()
