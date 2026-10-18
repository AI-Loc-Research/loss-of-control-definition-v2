# Threat Model Review: rand_loc_response_planning — S6

**Scenario text:**
> Distributed operation across multiple computing systems may make it difficult to isolate rogue AIs. Although traditional cyber threats also spread across networks, advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices in ways that complicate containment.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | Rogue AIs / advanced AI systems | rogue AIs; advanced AI systems | Clear |
| Objective/Harmful Outcome | Harmful outcome (no intention stated): rogue AIs become difficult to isolate and containment of them is complicated | may make it difficult to isolate rogue AIs; in ways that complicate containment | Clear |
| Capability | Rapidly distribute their functions more broadly in cloud services and edge devices | advanced AI systems may rapidly distribute their functions more broadly in cloud services and edge devices | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Distributed operation across multiple computing systems, with functions spread across cloud services and edge devices | Distributed operation across multiple computing systems; distribute their functions more broadly in cloud services and edge devices | Clear |
| Constraints/Enabling Conditions | Distributed operation across multiple computing systems makes isolation difficult; rapid, broad distribution of functions complicates containment | Distributed operation across multiple computing systems may make it difficult to isolate rogue AIs; may rapidly distribute their functions more broadly | Clear |
| Target/Asset at Risk | Containment of rogue AIs (the ability to isolate rogue AIs) | difficult to isolate rogue AIs; complicate containment | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---