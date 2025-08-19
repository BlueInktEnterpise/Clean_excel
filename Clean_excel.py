import pandas as pd

def clean_excel(input_file, output_file):
    # Lees de Excel in
    df = pd.read_excel(input_file)

    # Verwijder lege rijen
    df = df.dropna(how="all")

    # Kolomnamen netjes maken
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # Dubbele rijen verwijderen
    df = df.drop_duplicates()

    # Exporteer naar een nieuw Excel bestand
    df.to_excel(output_file, index=False)

    print(f"✅ Bestand opgeschoond en opgeslagen als: {output_file}")



