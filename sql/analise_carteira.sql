SELECT
    status,
    COUNT(*) AS quantidade,
    SUM(valor) AS total_valor,
    AVG(dias_atraso) AS media_atraso
FROM carteira
GROUP BY status;
