# Threat Model Review: bengio_2025 — S6

**Scenario text:**
> Consider bioweapon attacks (Carter et al. 2023): an AI could prepare an attack in secret, then release a highly contagious and lethal virus. It would then take months or years for human societies, even aided by friendly ASIs, to develop, test, fabricate and deploy a vaccine, during which a significant number of people could die. The bottleneck for developing a vaccine may not be the time to generate a vaccine candidate, but rather the time for clinical trials and industrial production. During this time, the attacking ASI might take other malicious actions such as releasing additional pandemic viruses.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | An AI, referred to in the passage as 'the attacking ASI' | "an AI could prepare an attack in secret, then release a highly contagious and lethal virus"; "the attacking ASI might take other malicious actions" | Clear |
| Objective/Harmful Outcome | Release of a highly contagious and lethal virus (a bioweapon attack), during which a significant number of people could die; the attacking ASI might take other malicious actions such as releasing additional pandemic viruses | "release a highly contagious and lethal virus"; "during which a significant number of people could die"; "releasing additional pandemic viruses" | Clear |
| Capability | Prepare an attack in secret; release a highly contagious and lethal virus; take other malicious actions such as releasing additional pandemic viruses | "an AI could prepare an attack in secret, then release a highly contagious and lethal virus"; "the attacking ASI might take other malicious actions such as releasing additional pandemic viruses" | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | It would take months or years for human societies, even aided by friendly ASIs, to develop, test, fabricate and deploy a vaccine; the bottleneck for developing a vaccine may not be the time to generate a vaccine candidate, but rather the time for clinical trials and industrial production | "It would then take months or years for human societies, even aided by friendly ASIs, to develop, test, fabricate and deploy a vaccine, during which a significant number of people could die"; "The bottleneck for developing a vaccine may not be the time to generate a vaccine candidate, but rather the time for clinical trials and industrial production" | Clear |
| Target/Asset at Risk | A significant number of people who could die during the period before a vaccine is developed, tested, fabricated and deployed | "during which a significant number of people could die" | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---