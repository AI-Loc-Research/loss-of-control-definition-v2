# Threat Model Review: barnett_2024 — S1

**Scenario text:**
> One possible story could be that the AI gains control over the data center where it is being trained and fakes the performance metrics such that the overseers don’t think anything bad is happening. It then spends time finding a set of security vulnerabilities that allow it to escape and gain enough freedom for further research. The AI copies itself to data centers around the world for redundancy. It then contacts various terrorist groups, and manipulates and assists them in creating biological weapons which are released simultaneously across the world, throwing the world into chaos.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | the AI | the AI gains control over the data center | Clear |
| Objective/Harmful Outcome | gain enough freedom for further research; biological weapons which are released simultaneously across the world, throwing the world into chaos | gain enough freedom for further research; creating biological weapons which are released simultaneously across the world, throwing the world into chaos | Clear |
| Capability | gains control over the data center; fakes the performance metrics; finding a set of security vulnerabilities; escape; copies itself to data centers around the world; contacts various terrorist groups; manipulates and assists them in creating biological weapons | gains control over the data center; fakes the performance metrics; finding a set of security vulnerabilities that allow it to escape; copies itself to data centers around the world; contacts various terrorist groups, and manipulates and assists them in creating biological weapons | Clear |
| Knowledge | performance metrics; overseers don’t think anything bad is happening; security vulnerabilities | fakes the performance metrics such that the overseers don’t think anything bad is happening; finding a set of security vulnerabilities | Clear |
| Access | control over the data center where it is being trained; copies itself to data centers around the world; contacts various terrorist groups | control over the data center where it is being trained; copies itself to data centers around the world; contacts various terrorist groups | Clear |
| Constraints/Enabling Conditions | where it is being trained; overseers don’t think anything bad is happening; security vulnerabilities that allow it to escape; for redundancy; released simultaneously across the world | where it is being trained; overseers don’t think anything bad is happening; security vulnerabilities that allow it to escape; for redundancy; released simultaneously across the world | Clear |
| Target/Asset at Risk | the data center where it is being trained; data centers around the world; overseers; terrorist groups; the world | the data center where it is being trained; data centers around the world; overseers; terrorist groups; the world | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---