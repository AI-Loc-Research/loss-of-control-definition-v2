# Threat Model Review: carlsmith_2021 — S3

**Scenario text:**
> to the extent that an AI system is actively trying to get deployed (for example, because the real-world influence deployment grants would offer greater opportunity to achieve its objectives), it might do things like try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter, and once its prospects for gaining/maintaining power are sufficiently good.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | An AI system that is 'actively trying to get deployed'. | an AI system is actively trying to get deployed | Clear |
| Objective/Harmful Outcome | Explicitly stated intention: to get deployed, 'because the real-world influence deployment grants would offer greater opportunity to achieve its objectives' (the AI's underlying objectives are not specified). Harmful outcomes described: trying to 'deceive or manipulate its trainers' and behaving badly on deployment inputs. | an AI system is actively trying to get deployed (for example, because the real-world influence deployment grants would offer greater opportunity to achieve its objectives), it might do things like try deceive or manipulate its trainers ... such that it behaves badly only on the latter | Clear |
| Capability | Might 'try deceive or manipulate its trainers' and/or 'differentiate between training/testing inputs and deployment inputs', such that it 'behaves badly only on the latter' (deployment inputs). | it might do things like try deceive or manipulate its trainers, and/or to differentiate between training/testing inputs and deployment inputs, such that it behaves badly only on the latter | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Operates on 'training/testing inputs and deployment inputs'; deployment would grant it 'real-world influence'. | the real-world influence deployment grants would offer greater opportunity to achieve its objectives ... differentiate between training/testing inputs and deployment inputs | Clear |
| Constraints/Enabling Conditions | The scenario applies 'to the extent that an AI system is actively trying to get deployed'; the AI 'behaves badly only on the latter' (deployment inputs, not training/testing inputs), and only 'once its prospects for gaining/maintaining power are sufficiently good'. | to the extent that an AI system is actively trying to get deployed ... such that it behaves badly only on the latter, and once its prospects for gaining/maintaining power are sufficiently good | Clear |
| Target/Asset at Risk | Its trainers (whom it might try to deceive or manipulate); specific targets of its deployment-time bad behavior are not specified. | try deceive or manipulate its trainers | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---