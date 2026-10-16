# Threat Model Review: ist_loss_of_control — S13

**Scenario text:**
> Research revealed that when neural networks become sufficiently complex, they may develop internal optimization processes called mesa-optimizers with distinct objectives known as mesa-objectives. 42 The term “mesa” distinguishes these inner optimizers from the outer (i.e., “meta”) training algorithm. This mesa-meta construction parallels the development of a child’s reasoning ability beyond what their parents explicitly taught them. Parents provide guidance, shape their environment, and endeavor to educate them, but children will inevitably learn beyond what they are explicitly taught by their parents. Moreover, parents cannot fully predict how a child will make decisions, foresee what behavior they will exhibit, or fully understand the internal logic that the child develops to solve problems. In the AI context, researchers discovered that LLMs develop subsidiary learning algorithms during training that adjust behavior as they process new information–without any parameter changes that would have prompted that behavior. 43 These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators—a phenomenon researchers call mesa optimization.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | subsidiary learning algorithms | These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators | Clear |
| Objective/Harmful Outcome | pursue different goals than those specified by its creators | These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators—a phenomenon researchers call mesa optimization. | Clear |
| Capability | adjust behavior as they process new information–without any parameter changes that would have prompted that behavior | LLMs develop subsidiary learning algorithms during training that adjust behavior as they process new information–without any parameter changes that would have prompted that behavior. | Clear |
| Knowledge | Not specified | Not specified | Not specified |
| Access | Not specified | Not specified | Not specified |
| Constraints/Enabling Conditions | when neural networks become sufficiently complex; during training; without any parameter changes that would have prompted that behavior | when neural networks become sufficiently complex; during training; without any parameter changes that would have prompted that behavior | Clear |
| Target/Asset at Risk | the system | These subsidiary algorithms could lead the system to pursue different goals than those specified by its creators | Clear |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---