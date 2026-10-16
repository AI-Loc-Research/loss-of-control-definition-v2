# Threat Model Review: cotra_2022 — S7

**Scenario text:**
> If it then discovers e.g. a zero-day exploit which it can only recognize because of knowledge it’s developed about computer hardware that it’s fairly confident Magma engineers don’t know, it can safely exploit that vulnerability (e.g. to directly edit the reward entered in its training dataset) because it’s unlikely to be entrapment by humans.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | it | it can safely exploit that vulnerability | Clear |
| Objective/Harmful Outcome | directly edit the reward entered in its training dataset | to directly edit the reward entered in its training dataset | Clear |
| Capability | discovers e.g. a zero-day exploit; can safely exploit that vulnerability; to directly edit the reward entered in its training dataset | discovers e.g. a zero-day exploit; can safely exploit that vulnerability; to directly edit the reward entered in its training dataset | Clear |
| Knowledge | knowledge it’s developed about computer hardware that it’s fairly confident Magma engineers don’t know; it’s unlikely to be entrapment by humans | knowledge it’s developed about computer hardware that it’s fairly confident Magma engineers don’t know; because it’s unlikely to be entrapment by humans | Clear |
| Access | to directly edit the reward entered in its training dataset | to directly edit the reward entered in its training dataset | Clear |
| Constraints/Enabling Conditions | If it then discovers e.g. a zero-day exploit; it can only recognize because of knowledge it’s developed about computer hardware that it’s fairly confident Magma engineers don’t know; because it’s unlikely to be entrapment by humans | If it then discovers e.g. a zero-day exploit; it can only recognize because of knowledge it’s developed about computer hardware that it’s fairly confident Magma engineers don’t know; because it’s unlikely to be entrapment by humans | Clear |
| Target/Asset at Risk | the reward entered in its training dataset | the reward entered in its training dataset | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---