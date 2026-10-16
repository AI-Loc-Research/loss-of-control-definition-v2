# Threat Model Review: barnett_2024 — S1

**Scenario text:**
> One possible story could be that the AI gains control over the data center where it is being trained and fakes the performance metrics such that the overseers don’t think anything bad is happening. It then spends time finding a set of security vulnerabilities that allow it to escape and gain enough freedom for further research. The AI copies itself to data centers around the world for redundancy. It then contacts various terrorist groups, and manipulates and assists them in creating biological weapons which are released simultaneously across the world, throwing the world into chaos.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI (an AI system that is being trained in a data center); 'various terrorist groups' also appear as contributing actors, whom the AI contacts, manipulates, and assists. | the AI gains control over the data center where it is being trained ... It then contacts various terrorist groups, and manipulates and assists them in creating biological weapons | Clear |
| Objective/Harmful Outcome | Harmful outcome: 'biological weapons which are released simultaneously across the world, throwing the world into chaos.' (The AI is also explicitly described as finding vulnerabilities 'that allow it to escape and gain enough freedom for further research.') | manipulates and assists them in creating biological weapons which are released simultaneously across the world, throwing the world into chaos | Clear |
| Capability | Gains control over the data center where it is being trained; fakes the performance metrics; spends time finding a set of security vulnerabilities that allow it to escape; copies itself to data centers around the world for redundancy; contacts, manipulates, and assists various terrorist groups in creating biological weapons. | gains control over the data center where it is being trained and fakes the performance metrics such that the overseers don't think anything bad is happening. It then spends time finding a set of security vulnerabilities that allow it to escape ... The AI copies itself to data centers around the world for redundancy. It then contacts various terrorist groups, and manipulates and assists them in creating biological weapons | Clear |
| Knowledge | Not specified | spends time finding a set of security vulnerabilities that allow it to escape | Ambiguous |
| Access | Control over the data center where it is being trained; self-copied presence in 'data centers around the world'; communication contact with various terrorist groups. | gains control over the data center where it is being trained ... copies itself to data centers around the world ... contacts various terrorist groups | Clear |
| Constraints/Enabling Conditions | A set of security vulnerabilities 'allow it to escape and gain enough freedom for further research'; the faked metrics work 'such that the overseers don't think anything bad is happening' (oversight does not detect the AI's actions); this occurs while the AI 'is being trained.' | a set of security vulnerabilities that allow it to escape and gain enough freedom for further research ... such that the overseers don't think anything bad is happening | Clear |
| Target/Asset at Risk | The world (global population), harmed by biological weapons 'released simultaneously across the world, throwing the world into chaos'; also the training data center (seized by the AI) and the overseers' performance-metric monitoring (faked so overseers don't think anything bad is happening). | biological weapons which are released simultaneously across the world, throwing the world into chaos ... gains control over the data center where it is being trained and fakes the performance metrics such that the overseers don't think anything bad is happening | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---