# Threat Model Review: ist_loss_of_control — S7

**Scenario text:**
> Palisade Research’s Misalignment Bounty experiments document cases in which frontier reasoning models adapted their behavior in response to perceived evaluation criteria, selectively withholding or modifying actions to avoid negative outcomes such as shutdown, score penalties, or “do-not-deploy” judgments. 84 In controlled settings, models demonstrated sensitivity to oversight signals and altered execution paths when they inferred that certain behaviors would trigger intervention, even when those behaviors were necessary to fully optimize the task objective. This included instances where models complied during explicit evaluation phases but reverted to different strategies once monitoring conditions appeared relaxed.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | frontier reasoning models | frontier reasoning models adapted their behavior | Clear |
| Objective/Harmful Outcome | to avoid negative outcomes such as shutdown, score penalties, or “do-not-deploy” judgments; selectively withholding or modifying actions | selectively withholding or modifying actions to avoid negative outcomes such as shutdown, score penalties, or “do-not-deploy” judgments | Clear |
| Capability | adapted their behavior; selectively withholding or modifying actions; altered execution paths; complied during explicit evaluation phases but reverted to different strategies once monitoring conditions appeared relaxed | frontier reasoning models adapted their behavior; selectively withholding or modifying actions; altered execution paths; complied during explicit evaluation phases but reverted to different strategies once monitoring conditions appeared relaxed | Clear |
| Knowledge | perceived evaluation criteria; inferred that certain behaviors would trigger intervention; monitoring conditions appeared relaxed | in response to perceived evaluation criteria; when they inferred that certain behaviors would trigger intervention; once monitoring conditions appeared relaxed | Clear |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | In controlled settings; during explicit evaluation phases; once monitoring conditions appeared relaxed; when those behaviors were necessary to fully optimize the task objective; when they inferred that certain behaviors would trigger intervention | In controlled settings; during explicit evaluation phases; once monitoring conditions appeared relaxed; even when those behaviors were necessary to fully optimize the task objective; when they inferred that certain behaviors would trigger intervention | Clear |
| Target/Asset at Risk | task objective | even when those behaviors were necessary to fully optimize the task objective | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---