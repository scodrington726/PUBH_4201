

SELECT
    s.patient_id,
    m.gene_symbol,
    COUNT(*) AS mutation_count
FROM mutations AS m
JOIN samples AS s
    ON m.sample_id = s.sample_id
WHERE m.gene_symbol IN (
    'TP53', 'KRAS', 'EGFR', 'STK11', 'KEAP1'
)
AND m.variant_classification != 'Silent'
GROUP BY
    s.patient_id,
    m.gene_symbol
ORDER BY
    s.patient_id,
    m.gene_symbol;

-- Task 2B:

SELECT
    s.tissue_source_site,
    p.stage,
    COUNT(DISTINCT p.patient_id) AS patient_count
FROM patients AS p
LEFT JOIN samples AS s
    ON p.patient_id = s.patient_id
GROUP BY
    s.tissue_source_site,
    p.stage
ORDER BY
    s.tissue_source_site,
    p.stage;
