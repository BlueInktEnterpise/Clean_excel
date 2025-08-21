import pandas as pd

def clean_excel(input_file, output_file):
    # Lees de Excel in
    df = pd.read_excel(input_file)

    # Print originele aantal rijen
    print(f"📄 Originele rijen: {len(df)}")

    # Verwijder lege rijen en dubbele rijen
    df = df.dropna(how="all").drop_duplicates()

    # Print aantal rijen na opschoning
    print(f"📄 Rijen na opschoning: {len(df)}")

    # Kolomnamen netjes maken
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # Exporteer naar een nieuw Excel bestand
    df.to_excel(output_file, index=False)
    print(f"✅ Bestand opgeschoond en opgeslagen als: {output_file}")

# Command-line functionaliteit
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Gebruik: python clean_excel.py <input_file.xlsx> <output_file.xlsx>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_excel(input_file, output_file)
