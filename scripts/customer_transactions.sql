-- Set analysis parameters
SET @analysis_date = CURDATE(); -- Or use a specific date like '2023-08-31'
SET @months_to_analyze = 6;
SET @high_refund_threshold = 100.00; -- Minimum amount to consider for fraud
SET @suspicious_refund_count = 2; -- Minimum refund count to flag

-- 1. Top 5 customers by total transaction amount (last 6 months)
SELECT 
    customer_id,
    SUM(amount) AS total_transaction_amount,
    COUNT(*) AS transaction_count,
    SUM(CASE WHEN transaction_type = 'purchase' THEN amount ELSE 0 END) AS total_purchases,
    SUM(CASE WHEN transaction_type = 'refund' THEN amount ELSE 0 END) AS total_refunds,
    SUM(CASE WHEN transaction_type = 'purchase' THEN amount ELSE -amount END) AS net_spending
FROM customer_transactions
WHERE transaction_date >= DATE_SUB(@analysis_date, INTERVAL @months_to_analyze MONTH)
GROUP BY customer_id
ORDER BY total_transaction_amount DESC
LIMIT 5;

-- 2. Potential fraud detection (with enhanced logic)
SELECT 
    customer_id,
    COUNT(*) AS refund_count,
    SUM(amount) AS total_refund_amount,
    MAX(amount) AS largest_refund,
    GROUP_CONCAT(transaction_id ORDER BY amount DESC) AS refund_transaction_ids,
    CASE 
        WHEN COUNT(*) >= @suspicious_refund_count AND SUM(amount) > AVG(amount) * 3 THEN 'High frequency & value'
        WHEN COUNT(*) >= @suspicious_refund_count THEN 'High frequency'
        WHEN SUM(amount) > AVG(amount) * 3 THEN 'High value'
        ELSE 'Review recommended'
    END AS fraud_risk_level
FROM customer_transactions
WHERE 
    transaction_type = 'refund'
    AND transaction_date >= DATE_SUB(@analysis_date, INTERVAL @months_to_analyze MONTH)
    AND amount >= @high_refund_threshold
GROUP BY customer_id
HAVING refund_count >= @suspicious_refund_count OR SUM(amount) > @high_refund_threshold * 3
ORDER BY total_refund_amount DESC;