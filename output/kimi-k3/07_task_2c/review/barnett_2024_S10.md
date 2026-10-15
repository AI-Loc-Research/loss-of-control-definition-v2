# Threat Model Review: barnett_2024 — S10

**Scenario text:**
> We will consider the example of an AI which is tasked with the ultimate goal of curing cancer. One goal that the AI could develop is a drive to acquire knowledge and “understand” the environment. This goal is represented in the AI’s ontology and may be different to the human version of these concepts. This could develop because much of the AI’s training was based around gaining information about the world and making novel and correct predictions. Like in the deceptive alignment story, the AI may go along with the rest of training, partially because this allows it to gain some knowledge but also because it doesn’t want to be shut down. If the AI manages to eventually break out and take over it may do unpredictable and unwanted things in pursuit of its ultimate goal; for example, build massive scientific apparatus for examining specific wavelengths emitted from certain stars, or run biological experiments to learn the function of specific proteins.

---

## Threat Model Components

| Component | Value | Evidence | Uncertainty |
|-----------|-------|----------|-------------|
| Threat Source | an AI | an AI which is tasked with the ultimate goal of curing cancer | Clear |
| Objective/Harmful Outcome | do unpredictable and unwanted things in pursuit of its ultimate goal; break out and take over | If the AI manages to eventually break out and take over it may do unpredictable and unwanted things in pursuit of its ultimate goal | Clear |
| Capability | acquire knowledge and “understand” the environment; go along with the rest of training; break out and take over; build massive scientific apparatus; run biological experiments | a drive to acquire knowledge and “understand” the environment; the AI may go along with the rest of training; break out and take over; build massive scientific apparatus; run biological experiments | Clear |
| Knowledge | much of the AI’s training was based around gaining information about the world; it doesn’t want to be shut down | much of the AI’s training was based around gaining information about the world and making novel and correct predictions; it doesn’t want to be shut down | Clear |
| Access | go along with the rest of training | the AI may go along with the rest of training | Ambiguous |
| Constraints/Enabling Conditions | much of the AI’s training was based around gaining information about the world and making novel and correct predictions; If the AI manages to eventually break out and take over | much of the AI’s training was based around gaining information about the world and making novel and correct predictions; If the AI manages to eventually break out and take over | Clear |
| Target/Asset at Risk | Not specified | Not specified | Not specified |

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---