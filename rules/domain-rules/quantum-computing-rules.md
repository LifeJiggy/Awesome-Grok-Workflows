# Quantum Computing Rules

## Safety Guidelines

### 1. Classical vs Quantum Advantage
- **Never claim quantum advantage without evidence**
- Compare against best classical algorithms
- Document when classical simulation is sufficient
- Consider problem size vs. quantum resources

### 2. Hardware Limitations
- **NISQ era constraints apply**
- Gate fidelity limits circuit depth
- Qubit connectivity affects circuit design
- Noise affects measurement outcomes

### 3. Error Mitigation
- Always apply error mitigation
- Report error rates in results
- Validate with classical simulation when possible
- Document noise models used

## Algorithm Selection

### When to Use Quantum
| Problem Type | Quantum Suitability |
|--------------|-------------------|
| Integer factorization | ✅ High (Shor's) |
| Search (unstructured) | ✅ High (Grover's) |
| Optimization | ⚠️ Conditional (QAOA/VQE) |
| Machine learning | ⚠️ Research stage |
| Simulation | ✅ High (molecular) |
| Database search | ✅ High (Grover's) |

### When NOT to Use Quantum
- Simple arithmetic (classical is faster)
- Deterministic algorithms
- Problems with efficient classical solutions
- Real-time constraints (quantum is slower)
- Small data problems

## Implementation Standards

### Circuit Design
```python
# ❌ Bad: Circuit too deep for NISQ
for i in range(100):
    qc.cx(qubits[i], qubits[(i+1)%100])

# ✅ Good: Shallow circuit
for i in range(5):
    qc.cx(qubits[i], qubits[i+1])
```

### Documentation Requirements
1. Number of qubits required
2. Circuit depth analysis
3. Gate counts by type
4. Expected fidelity
5. Error mitigation applied
6. Classical verification method

## Security Rules

### Cryptography
- **Never implement crypto yourself**
- Use established cryptographic libraries
- Quantum-resistant algorithms for long-term secrets
- Post-quantum migration planning
- Document key sizes and algorithms

### Best Practices
1. Use standard quantum libraries (Qiskit, Cirq)
2. Test on simulators first
3. Validate with known solutions
4. Document assumptions clearly
5. Include uncertainty quantification

## Ethical Considerations

### Dual-Use Concerns
- Factorization (Shor's) → Code breaking
- Optimization → Military applications
- Simulation → Drug discovery + weapons research

### Transparency
- Disclose quantum resources used
- Document potential misuse cases
- Consider societal impact
- Follow responsible disclosure

## Output Standards

### Research Papers
- Include classical baseline comparison
- Report noise characteristics
- Document hardware details
- Provide reproducibility information

### Implementation Code
- Version of quantum library
- Random seed for reproducibility
- Number of shots and measurement strategy
- Error mitigation techniques applied
