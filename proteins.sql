-- =====================================
-- selects.sql — View data
-- =====================================

-- View all protein entries
SELECT * FROM proteins;

-- Find by accession
SELECT * FROM proteins WHERE accession = 'TGME49_222170';

-- Filter by protein name
SELECT * FROM proteins WHERE name LIKE '%GRA%';

-- Filter by function keyword
SELECT * FROM proteins WHERE function LIKE '%phosphatase%';

-- Distinct conserved domains
SELECT DISTINCT domains FROM proteins;

-- Order by CRISPR score
SELECT * FROM proteins ORDER BY crispr_score DESC;

-- Filter for GRA proteins with low CRISPR score, sorted by name
SELECT * FROM proteins 
WHERE name LIKE '%GRA%' AND crispr_score <= 2
ORDER BY name;

-- =====================================
-- inserts.sql — Add data
-- =====================================

-- Insert new protein entry (id auto-increments)
INSERT INTO proteins (
  name, accession, function, domains, crispr_score, reference
) VALUES (
  'GRA17', 
  'TGME49_222170', 
  'Regulates bradyzoite viability', 
  'NULL', 
  NULL, 
  'PMID:12345678'
);


-- Add to existing protein entry
UPDATE proteins
SET 
  function = COALESCE(function, '') || '; ' || 'Regulates bradyzoite viability',
  reference = COALESCE(reference, '') || '; ' || '(Paredes-Santos et al., 2019)'
WHERE accession = 'TGME49_222170';


-- =====================================
-- updates.sql — Modify data
-- =====================================

-- Trim whitespace from accession
UPDATE proteins
SET accession = TRIM(accession);



-- Update function by accession
UPDATE proteins
SET accession = 'TGME49_208830'
WHERE accession = '208830';

SELECT * FROM proteins;
-- Update CRISPR score
UPDATE proteins
SET crispr_score = 98.0
WHERE accession = 'P67890';

-- Update domain list
UPDATE proteins
SET domains = 'newDomain1,newDomain2'
WHERE accession = 'P67890';


-- =====================================
-- deletes.sql — Remove data
-- =====================================

-- Delete protein by accession
DELETE FROM proteins WHERE accession = 'P67890';
SELECT * FROM proteins;

-- Delete all proteins with CRISPR score below threshold
DELETE FROM proteins WHERE crispr_score > 50;


-- =====================================
-- schema.sql — Table info
-- =====================================

-- Show the structure of the table
PRAGMA table_info(proteins);

-- View first row (for column headers)
SELECT * FROM proteins LIMIT 1;