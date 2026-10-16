# Threat Model Review: carlsmith_2021 — S3

**Scenario text:**
> to the extent that an AI system is actively trying to get deployed (for example, because the real-world influence deployment grants would offer greater opportunity to achieve its objectives), it might do things like try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter, and once its prospects for gaining/maintaining power are sufficiently good.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI system | an AI system is actively trying to get deployed | Clear |
| Objective/Harmful Outcome | actively trying to get deployed; try deceive or manipulate its trainers; behaves badly only on the latter | actively trying to get deployed; try deceive or manipulate its trainers; behaves badly only on the latter | Clear |
| Capability | try deceive or manipulate its trainers; differentiate between training/testing inputs and deployment inputs; behaves badly only on the latter | it might do things like try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | its trainers; training/testing inputs and deployment inputs | try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs | Clear |
| Constraints/Enabling Conditions | to the extent that an AI system is actively trying to get deployed; because the real-world influence deployment grants would offer greater opportunity to achieve its objectives; such that it behaves badly only on the latter; once its prospects for gaining/maintaining power are sufficiently good | to the extent that an AI system is actively trying to get deployed (for example, because the real-world influence deployment grants would offer greater opportunity to achieve its objectives), it might do things like try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter, and once its prospects for gaining/maintaining power are sufficiently good. | Clear |
| Target/Asset at Risk | its trainers | try deceive or manipulate its trainers | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---