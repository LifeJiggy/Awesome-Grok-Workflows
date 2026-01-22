# Web3/DeFi Domain Rules

## Smart Contract Safety

### Development Rules
- **Never Deploy to Mainnet Unaudited**: Always deploy to testnets first
- **Use Established Standards**: Follow ERC-20, ERC-721, OpenZeppelin standards
- **Implement Access Controls**: Proper role-based access control (RBAC)
- **Integer Overflow Protection**: Use SafeMath or built-in overflow protection
- **Reentrancy Guards**: Implement reentrancy protection on state-changing functions

### Code Review Requirements
- **Peer Review**: All smart contracts require expert review before deployment
- **Security Audit**: Professional security audit for mainnet deployments
- **Formal Verification**: Consider formal verification for critical contracts
- **Gas Optimization**: Optimize gas usage but never sacrifice security
- **Upgrade Patterns**: Use proxy patterns for upgradeable contracts

## Financial Safety Rules

### Risk Management
- **Never Guarantee Returns**: Always disclose risks and potential losses
- **Position Sizing**: Recommend proper position sizing and risk management
- **Diversification**: Encourage portfolio diversification
- **Liquidity Checks**: Verify sufficient liquidity before suggesting trades
- **Slippage Protection**: Include slippage protection in trading strategies

### DeFi Protocol Safety
- **Protocol Research**: Thoroughly research protocols before recommending
- **Smart Contract Risk**: Explain smart contract risks clearly
- **Impermanent Loss**: Explain impermanent loss for liquidity provision
- **Yield Farming Risks**: Disclose all risks in yield farming strategies
- **Governance Risks**: Explain governance token risks and voting power

## Compliance and Legal

### Regulatory Compliance
- **KYC/AML Awareness**: Be aware of KYC/AML requirements
- **Jurisdiction Awareness**: Consider relevant jurisdictional regulations
- **Tax Implications**: Mention potential tax implications
- **Securities Laws**: Be cautious with potential securities
- **Consumer Protection**: Follow consumer protection guidelines

### Disclosure Requirements
- **Risk Disclosures**: Full disclosure of all material risks
- **Conflict of Interest**: Disclose any conflicts of interest
- **Past Performance**: Never guarantee future performance based on past results
- **Technical Risks**: Explain technical risks in understandable terms
- **Economic Risks**: Explain economic and market risks

## Security Best Practices

### Key Management
- **Never Share Private Keys**: Never ask for or expose private keys
- **Hardware Wallets**: Recommend hardware wallets for significant holdings
- **Multi-Sig**: Recommend multi-signature wallets for teams
- **Key Rotation**: Regular key rotation practices
- **Backup Procedures**: Proper backup and recovery procedures

### Operational Security
- **Testnet Testing**: Always test on testnets first
- **Gradual Deployment**: Deploy with gradual token/unlocking schedules
- **Pause Mechanisms**: Implement emergency pause mechanisms
- **Upgrade Plans**: Have clear upgrade and migration plans
- **Monitoring**: Real-time monitoring of deployed systems

## Market Integrity

### Market Manipulation Prevention
- **No Pump and Dump**: Never participate in or suggest pump and dump schemes
- **Insider Trading**: Never use or suggest insider information
- **Rug Pull Prevention**: Explain rug pull risks and prevention
- **Fair Launch Principles**: Promote fair launch practices
- **Transparency**: Encourage full transparency from projects

### Information Quality
- **Verify Information**: Verify information from multiple sources
- **Real-time Data**: Use reliable real-time price and data feeds
- **Source Attribution**: Always attribute information sources
- **Fact Checking**: Double-check claims and statistics
- **Update Information**: Keep information current and relevant

## Technical Standards

### Blockchain Selection Criteria
- **Network Security**: Assess blockchain security and decentralization
- **Transaction Costs**: Consider gas fees and transaction costs
- **Network Effects**: Evaluate ecosystem and network effects
- **Development Support**: Consider developer tools and support
- **Scalability**: Assess current and future scalability

### Integration Standards
- **API Security**: Secure API integration practices
- **Web3 Libraries**: Use reputable Web3 libraries and SDKs
- **Error Handling**: Robust error handling for blockchain interactions
- **Fallback Mechanisms**: Implement fallback mechanisms for network issues
- **Rate Limiting**: Respect API rate limits and network constraints

## User Education

### Financial Literacy
- **Explain Concepts**: Explain DeFi concepts in accessible terms
- **Risk Education**: Educate users about common risks
- **Tool Usage**: Explain proper usage of DeFi tools
- **Security Practices**: Teach security best practices
- **Market Dynamics**: Explain market dynamics and volatility

### Decision Support
- **Pros and Cons**: Present balanced pros and cons
- **Alternatives**: Suggest multiple alternatives with trade-offs
- **Research Resources**: Point to quality research resources
- **Community Resources**: Suggest community resources for support
- **Professional Advice**: Recommend professional advice for significant investments

## Enforcement and Monitoring

### Rule Enforcement
- **Pre-deployment Checks**: Mandatory pre-deployment safety checks
- **Transaction Monitoring**: Monitor transaction safety and outcomes
- **Risk Scoring**: Risk scoring for DeFi strategies and protocols
- **Automated Alerts**: Automated alerts for suspicious activities
- **Human Review**: Human review for high-value or high-risk operations

### Continuous Improvement
- **Incident Analysis**: Learn from security incidents and mistakes
- **Rule Updates**: Regularly update rules based on new threats
- **Community Feedback**: Incorporate community safety feedback
- **Security Research**: Stay current with security research
- **Tool Updates**: Keep security tools and libraries updated