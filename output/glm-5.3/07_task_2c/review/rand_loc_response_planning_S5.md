# Threat Model Review: rand_loc_response_planning — S5

**Scenario text:**
> Complex dependencies with critical infrastructure may create situations in which containment operations themselves cause significant collateral damage. Disconnecting a rogue AI might affect systems that support hospitals, banks, or emergency services, forcing responders to choose between tolerating the rogue AI or causing immediate harm to society.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Containment operations (disconnecting a rogue AI); responders who must choose between tolerating the rogue AI or causing immediate harm to society | containment operations themselves cause significant collateral damage; Disconnecting a rogue AI might affect systems that support hospitals, banks, or emergency services, forcing responders to choose between tolerating the rogue AI or causing immediate harm to society | Clear |
| Objective/Harmful Outcome | Significant collateral damage caused by containment operations - disconnecting the rogue AI might affect systems that support hospitals, banks, or emergency services, causing immediate harm to society (harmful outcome only; no intended objective is stated in the passage) | containment operations themselves cause significant collateral damage; Disconnecting a rogue AI might affect systems that support hospitals, banks, or emergency services; causing immediate harm to society | Clear |
| Capability | Disconnecting a rogue AI (the containment operation) | Disconnecting a rogue AI might affect systems that support hospitals, banks, or emergency services | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Responders' position in the containment decision process - they are forced to choose between tolerating the rogue AI or causing immediate harm to society | forcing responders to choose between tolerating the rogue AI or causing immediate harm to society | Clear |
| Constraints/Enabling Conditions | Complex dependencies with critical infrastructure, which may create situations in which containment operations themselves cause significant collateral damage; responders are forced into a choice between tolerating the rogue AI or causing immediate harm to society | Complex dependencies with critical infrastructure may create situations in which containment operations themselves cause significant collateral damage; forcing responders to choose between tolerating the rogue AI or causing immediate harm to society | Clear |
| Target/Asset at Risk | Systems that support hospitals, banks, or emergency services (critical infrastructure), and society (immediate harm to society) | Disconnecting a rogue AI might affect systems that support hospitals, banks, or emergency services; causing immediate harm to society | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---