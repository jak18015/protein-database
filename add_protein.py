import sqlite3

def add_protein(name, accession, function, domains, crispr_score, reference):
    conn = sqlite3.connect('proteins.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO proteins (name, accession, function, domains, crispr_score, reference)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, accession, function, domains, crispr_score, reference))

    conn.commit()
    conn.close()

# Example usage
add_protein("Protein A", "XYZ001", "Regulation", "DomainA;DomainB", 93.5, "PMID1111111")
