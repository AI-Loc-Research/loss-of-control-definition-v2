# Threat Model Review: barnett_2024 — S1

**Scenario text:**
> One possible story could be that the AI gains control over the data center where it is being trained and fakes the performance metrics such that the overseers don’t think anything bad is happening. It then spends time finding a set of security vulnerabilities that allow it to escape and gain enough freedom for further research. The AI copies itself to data centers around the world for redundancy. It then contacts various terrorist groups, and manipulates and assists them in creating biological weapons which are released simultaneously across the world, throwing the world into chaos.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | the AI | the AI gains control over the data center where it is being trained | Clear |
| Objective/Harmful Outcome | throwing the world into chaos | throwing the world into chaos | Clear |
| Capability | gains control over the data center where it is being trained; fakes the performance metrics; finding a set of security vulnerabilities; escape and gain enough freedom for further research; copies itself to data centers around the world for redundancy; contacts various terrorist groups; manipulates and assists them in creating biological weapons | gains control over the data center where it is being trained; fakes the performance metrics; finding a set of security vulnerabilities; escape and gain enough freedom for further research; copies itself to data centers around the world for redundancy; contacts various terrorist groups; manipulates and assists them in creating biological weapons | Clear |
| Knowledge | Not specified | fakes the performance metrics such that the overseers don’t think anything bad is happening; finding a set of security vulnerabilities | Ambiguous |
| Access | gains control over the data center where it is being trained; copies itself to data centers around the world | gains control over the data center where it is being trained; copies itself to data centers around the world | Clear |
| Constraints/Enabling Conditions | where it is being trained; such that the overseers don’t think anything bad is happening; security vulnerabilities that allow it to escape and gain enough freedom for further research; for redundancy; simultaneously across the world | where it is being trained; such that the overseers don’t think anything bad is happening; security vulnerabilities that allow it to escape and gain enough freedom for further research; for redundancy; simultaneously across the world | Clear |
| Target/Asset at Risk | the data center where it is being trained; the overseers; the world | gains control over the data center where it is being trained; the overseers don’t think anything bad is happening; throwing the world into chaos | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---