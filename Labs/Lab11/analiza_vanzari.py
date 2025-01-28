import pandas as pd
df = pd.read_csv('vanzari.csv', delimiter='\t')

print("Primele rânduri din DataFrame:")
print(df.head())

df['Data'] = pd.to_datetime(df['Data'], format="%m/%d/%Y")

df['Luna'] = df['Data'].dt.to_period('M')
produse_luna = df.groupby(['Luna', 'Produs'])['Cantitate'].sum().reset_index()
cele_mai_vandute = produse_luna.loc[produse_luna.groupby('Luna')['Cantitate'].idxmax()]

df['Venit'] = df['Cantitate'] * df['Pret']
venit_pe_produs = df.groupby('Produs')['Venit'].sum().reset_index().sort_values(by='Venit', ascending=False)

start_date = pd.to_datetime("2023-01-01")
end_date = pd.to_datetime("2023-03-31")
vanzari_interval = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]

venit_mediu_lunar = df.groupby('Luna')['Venit'].mean().reset_index()

print("Cele mai vândute produse pe lună:")
print(cele_mai_vandute)

print("\nVenitul total pe fiecare produs:")
print(venit_pe_produs)

print("\nVânzările între 01.01.2023 și 31.03.2023:")
print(vanzari_interval)

print("\nVenitul mediu lunar:")
print(venit_mediu_lunar)