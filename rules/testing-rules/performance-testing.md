# Performance Testing Rules

## Types of Tests
1. **Load Testing** - Normal expected load
2. **Stress Testing** - Beyond normal load
3. **Spike Testing** - Sudden load increases
4. **Endurance Testing** - Long-duration load

## Metrics to Measure
1. **Response Time** - Latency percentiles
2. **Throughput** - Requests per second
3. **Error Rate** - Percentage of failures
4. **Resource Usage** - CPU, memory, network

## Test Design
1. **Realistic Workloads** - Simulate real usage
2. **Ramp Up/Down** - Gradual load changes
3. **Warm Up Period** - Allow system to stabilize
4. **Steady State** - Measure at steady load

## Best Practices
1. **Isolate Tests** - No interference
2. **Monitor System** - Track resource usage
3. **Baseline Measurements** - Know current performance
4. **Track Over Time** - Performance trends

## Tools
1. **k6** - Modern load testing
2. **JMeter** - Feature-rich, Java-based
3. **Gatling** - Scala-based, high performance
4. **Locust** - Python-based, distributed

## Acceptance Criteria
1. **Response Time** - P95 < 200ms
2. **Throughput** - Handle 10x peak load
3. **Error Rate** - < 0.1% under normal load
4. **Recovery** - Recover from spike in < 5 min
