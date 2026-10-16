# Threat Model Review: bengio_2025 — S6

**Scenario text:**
> Consider bioweapon attacks (Carter et al. 2023): an AI could prepare an attack in secret, then release a highly contagious and lethal virus. It would then take months or years for human societies, even aided by friendly ASIs, to develop, test, fabricate and deploy a vaccine, during which a significant number of people could die. The bottleneck for developing a vaccine may not be the time to generate a vaccine candidate, but rather the time for clinical trials and industrial production. During this time, the attacking ASI might take other malicious actions such as releasing additional pandemic viruses.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI; the attacking ASI | an AI could prepare an attack in secret; the attacking ASI might take other malicious actions | Clear |
| Objective/Harmful Outcome | release a highly contagious and lethal virus; a significant number of people could die | release a highly contagious and lethal virus; a significant number of people could die | Clear |
| Capability | prepare an attack in secret; release a highly contagious and lethal virus; take other malicious actions such as releasing additional pandemic viruses | prepare an attack in secret, then release a highly contagious and lethal virus; the attacking ASI might take other malicious actions such as releasing additional pandemic viruses | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | prepare an attack in secret; It would then take months or years for human societies, even aided by friendly ASIs, to develop, test, fabricate and deploy a vaccine; The bottleneck for developing a vaccine may not be the time to generate a vaccine candidate, but rather the time for clinical trials and industrial production | prepare an attack in secret; It would then take months or years for human societies, even aided by friendly ASIs, to develop, test, fabricate and deploy a vaccine; The bottleneck for developing a vaccine may not be the time to generate a vaccine candidate, but rather the time for clinical trials and industrial production | Clear |
| Target/Asset at Risk | a significant number of people | a significant number of people could die | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---