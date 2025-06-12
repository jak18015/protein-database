import sqlite3
import pandas as pd


def print_protein_info(df):
    """Prints the protein information from the DataFrame."""
    if df.empty:
        print("No data found.")
        return
    
    for index, row in df.iterrows():
        print(f"Name: {row['name']}")
        print(f"Accession: {row['accession']}")
        print(f"Function: {row['function']}")
        print(f"Domains: {row['domains']}")
        print(f"CRISPR Score: {row['crispr_score']}")
        print(f"References: {row['reference']}")
        print("--------------------------------------------------\n")


def query(conn, field, value, match_type="exact"):
    """
    General-purpose query function for proteins table.

    Parameters:
        field (str): One of 'name', 'accession', 'function', 'domains', 'crispr_score', 'reference'.
        value (str or float): The value to search for.
        match_type (str): 'exact', 'like', or 'lt' (less than).

    Returns:
        pandas.DataFrame
    """
    valid_fields = ["name", "accession", "function", "domains", "crispr_score", "reference"]
    if field not in valid_fields:
        raise ValueError(f"Invalid field: {field}. Choose from: {', '.join(valid_fields)}")

    if match_type == "exact":
        query = f"SELECT * FROM proteins WHERE {field} = ?;"
        params = (value,)
    elif match_type == "like":
        query = f"SELECT * FROM proteins WHERE {field} LIKE ?;"
        params = (f"%{value}%",)
    elif match_type == "lt":
        query = f"SELECT * FROM proteins WHERE {field} < ?;"
        params = (value,)
    else:
        raise ValueError("match_type must be 'exact', 'like', or 'lt'")

    return pd.read_sql_query(query, conn, params=params)


def update_protein_by_name(cursor, name: str, updates: dict):
    """
    Updates one or more columns for a protein entry identified by its name.
    Args:
        cursor (sqlite3.Cursor): SQLite database cursor.
        name (str): The value of the 'name' field identifying the row to update.
        updates (dict): A dictionary mapping column names to new values.
        updates = {
            'accession':'',
            'function':'',
            'domains':'',
            'crispr_score':'',
            'reference':'',
        }
    """
    if not updates:
        raise ValueError("Nothing to update")

    set_clause = ", ".join(f"{col} = ?" for col in updates.keys())
    values = list(updates.values()) + [name]

    sql = f"UPDATE proteins SET {set_clause} WHERE name = ?"
    cursor.execute(sql, values)


def append_to_protein_by_name(cursor, name, updates: dict):
    """
    Appends new information to existing fields for a protein identified by its name.
    Does not commit the transaction — you must call conn.commit() manually.
    """
    # Fetch current values
    cursor.execute(f"SELECT {', '.join(updates.keys())} FROM proteins WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result is None:
        print(f"No protein found with name '{name}'")
        return

    # Prepare new values
    new_values = []
    for i, (column, new_data) in enumerate(updates.items()):
        current_data = result[i]
        if current_data is None:
            updated_data = str(new_data)
        else:
            current_str = str(current_data).strip()
            new_str = str(new_data).strip()
            if new_str not in current_str:
                updated_data = current_str + "; " + new_str
            else:
                updated_data = current_str
        new_values.append(updated_data)

    # Build update query (no commit)
    set_clause = ", ".join([f"{key} = ?" for key in updates])
    query = f"UPDATE proteins SET {set_clause} WHERE name = ?;"
    cursor.execute(query, (*new_values, name))
    print(f"Prepared update for protein '{name}' — run conn.commit() to save changes.")