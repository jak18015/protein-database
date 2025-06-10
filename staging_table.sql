-- 1. Create a staging table
CREATE TABLE tmp_proteins (
  name TEXT,
  accession TEXT,
  function TEXT,
  domains TEXT,
  crispr_score REAL,
  reference TEXT
);

-- 2. Import into the staging table
.mode csv
.import dense-granule-review.csv tmp_proteins

-- 3. Insert into the real table, letting SQLite assign id
INSERT INTO proteins (name, accession, function, domains, crispr_score, reference)
SELECT name, accession, function, domains, crispr_score, reference
FROM tmp_proteins;

-- 4. Drop the staging table
DROP TABLE tmp_proteins;
