# Workflow Failure Case Example

This document demonstrates how to handle and debug workflow failures.

## Failed Workflow: Data Processing Pipeline

### Error Trace
```
[2024-01-22 14:00:00] 🚀 Workflow started: data-pipeline
[2024-01-22 14:00:01] ✓ extract-data: Completed (15.3s)
  └─ Records extracted: 1,000,000
[2024-01-22 14:00:17] ✓ validate-schema: Completed (2.1s)
  └─ Schema validation: PASSED
[2024-01-22 14:00:20] ✗ transform-data: FAILED
  └─ Error: OutOfMemoryError: Java heap space
  └─ Location: transformers/cleaning.py:127
  └─ Message: Cannot allocate 512MB for processing buffer

[2024-01-22 14:00:21] ⚠️ Workflow paused - waiting for intervention
```

### Root Cause Analysis

#### Error Details
```json
{
  "error_type": "OutOfMemoryError",
  "message": "Java heap space",
  "location": "transformers/cleaning.py:127",
  "stack_trace": [
    "at java.util.Arrays.copyOf(Arrays.java:3210)",
    "at java.util.ArrayList.grow(ArrayList.java:265)",
    "at java.util.ArrayList.addAll(ArrayList.java:426)",
    "at transformers.cleaning.CleaningTransformer.transform(CleaningTransformer.java:127)"
  ],
  "memory_stats": {
    "heap_used": "1.8GB",
    "heap_max": "2GB",
    "buffer_size": "512MB"
  }
}
```

#### Contributing Factors
1. Input data size: 1,000,000 records
2. Memory allocation: 2GB heap
3. Processing mode: In-memory transformation
4. No streaming: Loading all data at once

### Resolution

#### Option 1: Increase Memory
```yaml
# Increase container memory
resources:
  limits:
    memory: 4Gi
  requests:
    memory: 2Gi
```

#### Option 2: Streaming Processing (Recommended)
```python
# Use chunked processing
def transform_data(data_stream, chunk_size=10000):
    for chunk in chunks(data_stream, chunk_size):
        yield process_chunk(chunk)
```

#### Option 3: Optimize Data Structure
```python
# Use generators instead of lists
def get_records():
    for record in database.stream():
        yield clean_record(record)
```

### Fixed Workflow
```yaml
name: data-pipeline-optimized
version: 1.1.0
steps:
  - name: extract-data
    action: data.extract
    params:
      streaming: true

  - name: transform-data
    action: data.transform_streaming
    needs: [extract-data]
    params:
      chunk_size: 10000
      max_memory: "512MB"

  - name: load-data
    action: data.load
    needs: [transform-data]
```

### Retry Result
```
[2024-01-22 14:30:00] 🔄 Workflow restarted with fixes
[2024-01-22 14:30:01] ✓ extract-data: Completed (18.2s) - streaming
[2024-01-22 14:35:00] ✓ transform-data: Completed (4m 59s) - chunked processing
[2024-01-22 14:35:02] ✓ load-data: Completed (2.1s)
[2024-01-22 14:35:02] 🎉 Workflow completed successfully!
```

### Lessons Learned
1. Always use streaming for large datasets
2. Set appropriate memory limits
3. Monitor memory usage during processing
4. Implement chunked processing patterns
5. Test with production-scale data
