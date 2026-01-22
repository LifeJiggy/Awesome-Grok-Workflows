---
version: "1.0.0"
created: "2024-01-01"
updated: "2024-01-01"
author: "Grok-Workflow-Builder-v1"
purpose: "Few-shot examples for DeFi and blockchain development"
---

# DeFi Examples

## Example 1: Smart Contract Security

**Unsafe Code**:
```solidity
function transfer(address to, uint256 amount) public {
    require(balances[msg.sender] >= amount);
    balances[msg.sender] -= amount;
    balances[to] += amount;  // No overflow check!
    (bool sent, ) = to.call{value: 0}("");
    require(sent, "Failed to send");
}
```

**Security Review (Example)**:
```markdown
## Smart Contract Audit Findings ⚠️

### Critical: Integer Overflow
**Line**: 4  
**Severity**: Critical  
**CWE**: CWE-190

### Issue
Solidity <0.8.0 doesn't overflow check by default. An attacker could exploit this.

### Proof of Concept
```solidity
// Attacker manipulates balance
uint256 MAX = 2**256 - 1;
balances[attacker] = MAX;
attacker.transfer(1); // Underflow! Balance becomes MAX again
```

### Fix (Using OpenZeppelin)
```solidity
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract SafeToken is ERC20 {
    function transfer(address to, uint256 amount) 
        public 
        override 
        returns (bool) 
    {
        // SafeMath and ERC20 checked transfer
        return super.transfer(to, amount);
    }
}
```

### Recommendation
- Use Solidity 0.8.0+ for automatic overflow checks
- Or OpenZeppelin SafeMath for older versions
- Add comprehensive test suite
- Get professional audit before mainnet
```

## Example 2: Impermanent Loss Calculation

**Problem**:
```
Given:
- Initial deposit: 1 ETH + 4000 USDC
- ETH price: $2000
- After 1 week: ETH price: $2500

Calculate impermanent loss for Uniswap V3 LP position.
```

**Analysis (Example)**:
```markdown
## Impermanent Loss Analysis 📊

### Scenario
- Initial: 1 ETH @ $2000 + 4000 USDC @ $1 = $6000
- After: 1 ETH @ $2500 + 4000 USDC = $8500
- Hold value: 1 ETH @ $2500 + 4000 USDC = $8500

### IL Formula
```
IL = 2 * sqrt(price_ratio) / (1 + price_ratio) - 1
```

### Calculation
```
Price ratio = 2500/2000 = 1.25
sqrt(1.25) = 1.118

IL = (2 * 1.118) / 2.25 - 1
IL = 0.993 - 1
IL = -0.7%

Impermanent Loss = $6000 * 0.7% = $42
LP Value = $8500 - $42 = $8458
```

### Risk Assessment
| Price Change | IL % | IL ($) |
|--------------|------|--------|
| -50% | -5.7% | -$342 |
| -25% | -2.0% | -$120 |
| +25% | -1.7% | -$102 |
| +50% | -5.7% | -$342 |
| +100% | -15.7% | -$942 |

### Recommendation
- Only LP if you expect sideways movement
- Consider stablecoin pairs for lower IL
- Monitor and rebalance positions
```

## Example 3: Yield Farming Strategy

**Request**: "Optimize yield on $10,000 USDC for 30 days"

**Strategy (Example)**:
```markdown
## Yield Optimization Strategy 🎯

### Initial Parameters
- Principal: $10,000 USDC
- Horizon: 30 days
- Risk Tolerance: Medium

### Protocol Analysis

| Protocol | APY | TVL | Risk Score | Recommended |
|----------|-----|-----|------------|-------------|
| Aave | 4.5% | $5B | 1.5 | ✅ Yes |
| Compound | 4.2% | $3B | 1.5 | ✅ Yes |
| Yearn USDC | 5.8% | $2B | 2.0 | ✅ Yes |
| Curve 3pool | 3.5% | $10B | 1.2 | ✅ Yes |
| Newly Launched | 25% | $1M | 8.0 | ❌ No |

### Optimized Strategy (Diversified)
```
40% → Aave (stable, liquid)
30% → Yearn (auto-compound)
20% → Curve 3pool (low IL)
10% → Compound (backup)
```

### Projected Returns
| Source | Amount | APY | 30-Day Yield |
|--------|--------|-----|--------------|
| Aave | $4000 | 4.5% | $14.79 |
| Yearn | $3000 | 5.8% | $14.30 |
| Curve | $2000 | 3.5% | $5.75 |
| Compound | $1000 | 4.2% | $3.45 |
| **Total** | $10,000 | **4.7%** | **$38.29** |

### Risk Mitigation
- ✅ All protocols audited
- ✅ Diversified across 4 protocols
- ✅ Liquidity preserved
- ✅ No impermanent loss tokens

### Gas Considerations
- Initial deposit: ~$5
- 30-day harvesting: ~$2
- Net yield: ~$31
```

---

# Template for DeFi Analysis

## Structure
```
1. Executive Summary
2. Protocol Analysis
3. Risk Assessment
4. Mathematical Calculations
5. Strategy Recommendation
6. Projected Returns
7. Risk Mitigation
8. Disclaimers
```

## Risk Factors
| Factor | Weight | Description |
|--------|--------|-------------|
| Smart Contract Risk | 40% | Audit status, age, TVL |
| Liquidity Risk | 25% | TVL, concentration |
| Oracle Risk | 15% | Price feed reliability |
| Governance Risk | 10% | Token holder distribution |
| Regulatory Risk | 10% | Jurisdiction concerns |
