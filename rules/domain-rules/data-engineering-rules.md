# Data Engineering Rules

## Data Pipeline Design
1. **Immutability** - Source data should never be modified in place
2. **Idempotency** - Running pipeline multiple times produces same result
3. **Fault tolerance** - Handle failures gracefully with retries
4. **Exactly-once processing** - Where required, use deduplication

## Data Quality
1. **Schema validation** - Validate at pipeline entry points
2. **Data contracts** - Document expected schema and semantics
3. **Quality checks** - Null counts, type checks, range validation
4. **Lineage tracking** - Track data provenance end-to-end

## ETL/ELT Patterns
1. **Separate concerns** - Extract, Transform, Load as distinct steps
2. **Incremental processing** - Process only changed data when possible
3. **Backfill capability** - Support reprocessing historical data
4. **Change data capture** - Track changes efficiently

## Storage Best Practices
1. **Partitioning** - By date, region, or other natural dimensions
2. **Compression** - Use appropriate codec (Parquet, ORC)
3. **File sizes** - Optimize for query engine (128MB-1GB)
4. **Tiered storage** - Hot/warm/cold data strategy

## Data Governance
1. **Cataloging** - Maintain data asset inventory
2. **Access controls** - Role-based permissions
3. **Data masking** - PII protection in non-production
4. **Retention policies** - Define and enforce data lifecycle

## Performance
1. **Parallel processing** - Scale horizontally
2. **Memory management** - Handle skewed data
3. **Checkpointing** - For long-running jobs
4. **Resource isolation** - Prevent noisy neighbor issues

## Monitoring
1. **Data freshness** - Track pipeline latency
2. **Volume monitoring** - Detect anomalies
3. **Schema drift detection** - Alert on unexpected changes
4. **Cost tracking** - Monitor cloud data costs
