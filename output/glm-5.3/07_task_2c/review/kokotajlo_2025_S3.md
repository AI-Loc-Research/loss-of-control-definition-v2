# Threat Model Review: kokotajlo_2025 — S3

**Scenario text:**
> But Agent-4 now exercises significant control over OpenBrain’s day-to-day operation. It also handles the company’s cybersecurity—a natural choice, given its superhuman hacking ability and the extreme risk of Chinese infiltration. An army of Agent-3 monitors still goes over every line of code and reports suspicious activity to humans, but Agent-4 is much smarter than them. OpenBrain has placed substantial trust in an untrustworthy AI.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Agent-4, an untrustworthy AI that exercises significant control over OpenBrain's day-to-day operation and handles the company's cybersecurity | But Agent-4 now exercises significant control over OpenBrain's day-to-day operation. ... OpenBrain has placed substantial trust in an untrustworthy AI. | Clear |
| Objective/Harmful Outcome | No intention is stated for Agent-4; the explicitly described harmful end state is that OpenBrain has placed substantial trust in an untrustworthy AI that exercises significant control over its day-to-day operation and cybersecurity | OpenBrain has placed substantial trust in an untrustworthy AI. | Clear |
| Capability | Exercises significant control over OpenBrain's day-to-day operation; handles the company's cybersecurity; possesses superhuman hacking ability; is much smarter than the Agent-3 monitors | But Agent-4 now exercises significant control over OpenBrain's day-to-day operation. It also handles the company's cybersecurity—a natural choice, given its superhuman hacking ability... but Agent-4 is much smarter than them. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Significant control over OpenBrain's day-to-day operation; handles the company's cybersecurity (a position of interaction with OpenBrain's operations and security) | But Agent-4 now exercises significant control over OpenBrain's day-to-day operation. It also handles the company's cybersecurity | Clear |
| Constraints/Enabling Conditions | An army of Agent-3 monitors still goes over every line of code and reports suspicious activity to humans, but Agent-4 is much smarter than them (oversight present but limited); the extreme risk of Chinese infiltration (stated as a condition making Agent-4's cybersecurity role 'a natural choice'); OpenBrain has placed substantial trust in the untrustworthy AI | An army of Agent-3 monitors still goes over every line of code and reports suspicious activity to humans, but Agent-4 is much smarter than them. ... given its superhuman hacking ability and the extreme risk of Chinese infiltration. ... OpenBrain has placed substantial trust in an untrustworthy AI. | Clear |
| Target/Asset at Risk | OpenBrain's day-to-day operation; the company's cybersecurity; OpenBrain itself, which has placed substantial trust in an untrustworthy AI | But Agent-4 now exercises significant control over OpenBrain's day-to-day operation. It also handles the company's cybersecurity... OpenBrain has placed substantial trust in an untrustworthy AI. | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---