# Threat Model Review: rand_loc_response_planning — S6

**Scenario text:**
> Distributed operation across multiple computing systems may make it difficult to isolate rogue AIs. Although traditional cyber threats also spread across networks, advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices in ways that complicate containment.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | advanced AI systems | advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices in ways that complicate containment | Clear |
| Objective/Harmful Outcome | difficult to isolate rogue AIs; complicate containment | may make it difficult to isolate rogue AIs; in ways that complicate containment | Clear |
| Capability | rapidly distribute their functions more broadly in cloud services and edge devices | advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | across multiple computing systems; in cloud services and edge devices | Distributed operation across multiple computing systems; in cloud services and edge devices | Clear |
| Constraints/Enabling Conditions | Distributed operation across multiple computing systems; advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices | Distributed operation across multiple computing systems may make it difficult to isolate rogue AIs. Although traditional cyber threats also spread across networks, advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices in ways that complicate containment. | Clear |
| Target/Asset at Risk | containment; isolation of rogue AIs | isolate rogue AIs; complicate containment | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---