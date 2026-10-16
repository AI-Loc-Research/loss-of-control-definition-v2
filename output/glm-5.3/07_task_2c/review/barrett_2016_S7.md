# Threat Model Review: barrett_2016 — S7

**Scenario text:**
> (2) Soft takeoff limits fail. A soft takeoff proceeds slowly, permitting significant human intervention in the takeoff process. Figure 3 models three soft takeoff scenarios (i.e., failures of soft takeoff limits): (1) hardware quantity, in which the AI takes off due to gradually increasing its amount of available hardware;10 (2) hardware quality, in which AI takes off due to gradually develops faster hardware; and (3) software quality, in which the AI gradually develops smarter AI software.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI | the AI takes off due to gradually increasing its amount of available hardware; ... the AI gradually develops smarter AI software | Clear |
| Objective/Harmful Outcome | The AI takes off, i.e., soft takeoff limits fail (no intention or objective is stated for the AI) | Soft takeoff limits fail. ... Figure 3 models three soft takeoff scenarios (i.e., failures of soft takeoff limits): (1) hardware quantity, in which the AI takes off due to gradually increasing its amount of available hardware; (2) hardware quality, in which AI takes off due to gradually develops faster hardware | Clear |
| Capability | Gradually increasing its amount of available hardware; gradually developing faster hardware; gradually developing smarter AI software | (1) hardware quantity, in which the AI takes off due to gradually increasing its amount of available hardware; (2) hardware quality, in which AI takes off due to gradually develops faster hardware; and (3) software quality, in which the AI gradually develops smarter AI software | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Its amount of available hardware (hardware available to the AI) | its amount of available hardware | Clear |
| Constraints/Enabling Conditions | A soft takeoff proceeds slowly, permitting significant human intervention in the takeoff process | A soft takeoff proceeds slowly, permitting significant human intervention in the takeoff process. | Clear |
| Target/Asset at Risk | Soft takeoff limits (which fail) | Soft takeoff limits fail ... three soft takeoff scenarios (i.e., failures of soft takeoff limits) | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---