# Threat Model Review: barrett_2016 — S6

**Scenario text:**
> (1) Hard takeoff limits fail. A hard takeoff proceeds rapidly, with no opportunity for human intervention. Figure 3 models three hard takeoff scenarios (i.e., failures of hard takeoff limits): (1) hardware quantity, in which the AI takes off rapidly due to an abundance of available hardware (also known as hardware overhang; see Sotala and Yampolskiy 2015); (2) hardware quality, in which the AI rapidly develops faster hardware (also known as speed explosion; see Sotala and Yampolskiy 2015); and (3) software quality, in which the AI rapidly develops smarter AI software (also known as intelligence explosion; see Sotala and Yampolskiy 2015).

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | The AI (the system that 'takes off rapidly,' 'rapidly develops faster hardware,' and 'rapidly develops smarter AI software' in the three hard takeoff scenarios) | (1) hardware quantity, in which the AI takes off rapidly due to an abundance of available hardware (also known as hardware overhang; see Sotala and Yampolskiy 2015); (2) hardware quality, in which the AI rapidly develops faster hardware (also known as speed explosion; see Sotala and Yampolskiy 2015); and (3) software quality, in which the AI rapidly develops smarter AI software (also known as intelligence explosion; see Sotala and Yampolskiy 2015) | Clear |
| Objective/Harmful Outcome | No intention is stated. Harmful outcome: hard takeoff limits fail — 'a hard takeoff proceeds rapidly, with no opportunity for human intervention' (the three scenarios are described as 'failures of hard takeoff limits') | Hard takeoff limits fail. A hard takeoff proceeds rapidly, with no opportunity for human intervention. ... Figure 3 models three hard takeoff scenarios (i.e., failures of hard takeoff limits) | Clear |
| Capability | The AI 'takes off rapidly' (hardware quantity scenario), 'rapidly develops faster hardware' (hardware quality scenario), and 'rapidly develops smarter AI software' (software quality scenario) | the AI takes off rapidly due to an abundance of available hardware ... the AI rapidly develops faster hardware ... the AI rapidly develops smarter AI software | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | The hard takeoff 'proceeds rapidly, with no opportunity for human intervention'; in the hardware quantity scenario, the AI takes off rapidly 'due to an abundance of available hardware' (hardware overhang) | A hard takeoff proceeds rapidly, with no opportunity for human intervention. ... due to an abundance of available hardware | Clear |
| Target/Asset at Risk | Hard takeoff limits (which 'fail'); the opportunity for human intervention (absent — 'no opportunity for human intervention') | Hard takeoff limits fail. ... with no opportunity for human intervention | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---