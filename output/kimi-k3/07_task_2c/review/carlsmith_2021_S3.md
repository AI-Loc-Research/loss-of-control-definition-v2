# Threat Model Review: carlsmith_2021 — S3

**Scenario text:**
> to the extent that an AI system is actively trying to get deployed (for example, because the real-world influence deployment grants would offer greater opportunity to achieve its objectives), it might do things like try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter, and once its prospects for gaining/maintaining power are sufficiently good.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI system actively trying to get deployed | an AI system is actively trying to get deployed | Clear |
| Objective/Harmful Outcome | gaining/maintaining power through real-world influence that deployment grants, in order to achieve its objectives | the real-world influence deployment grants would offer greater opportunity to achieve its objectives ... once its prospects for gaining/maintaining power are sufficiently good | Clear |
| Capability | deceive or manipulate its trainers; differentiate between training/testing inputs and deployment inputs; behaves badly only on deployment inputs | try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter | Clear |
| Knowledge | differentiate between training/testing inputs and deployment inputs | differentiate between training/testing inputs and deployment inputs | Ambiguous |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | once its prospects for gaining/maintaining power are sufficiently good | once its prospects for gaining/maintaining power are sufficiently good | Clear |
| Target/Asset at Risk | its trainers | try deceive or manipulate its trainers | Ambiguous |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---