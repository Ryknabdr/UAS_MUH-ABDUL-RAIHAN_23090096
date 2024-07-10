import pandas as pd
data = {
    'Nama': ['Suaib', 'Wirjo', 'Maryam'],
    'Algoritma dan Struktur Data': [90, 50, 65],
    'Matematika Numerik': [80, 60, 70]
}
df = pd.DataFrame(data)

print("Data Mahasiswa:")
print(df.to_string(index=False))

average_subjects = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean()
print("\nRata-rata nilai setiap mata kuliah:")
for subject, average in average_subjects.items():
    print(f"{subject}: {average:.2f}")

df['Rata-rata'] = df[['Algoritma dan Struktur Data', 'Matematika Numerik']].mean(axis=1)
print("\nData Mahasiswa dengan Rata-rata:")
print(df[['Nama', 'Rata-rata']].to_string(index=False))