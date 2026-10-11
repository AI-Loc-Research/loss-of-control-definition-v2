# Definition Extraction Review: barnett_2024

**Paper:** Barnett, P. & Gillen, J. (2024). Without Fundamental Advances, Misalignment and Catastrophe Are the Default Outcomes of Training Powerful AI.
**Experiment:** 1a_kimi-k3-nvidia_prompt_1a_v2
**Model:** moonshotai/kimi-k3
**Date:** 2026-10-11T13:33:29.133737+00:00

---

## Extraction 1

**Term:** uncontrolled
**Location:** Section 4 (Behavioral training is an imprecise way to specify goals), page 15

**Extracted quote:**
> There are several categories of problems that make it difficult to specify goals. Each category introduces an uncontrolled degree of freedom in the goal specification which exists because we are only using feedback based on behavior.

**Context from source** (±3 sentences):
> By behavioral training we are referring to a wide variety
of training techniques, which involve running a parameterized model, providing feedback on the
output of the model, and updating the model based on this feedback. Examples include model-free
RL using PPO [25], model-based RL like MuZero [26], next token prediction on tokens describing
goal-directed behavior [27]. In previous sections we have described the behavioral properties that appear to be necessary for hard
tasks. That is: powerful AIs are behaviorally, approximately, optimizing their actions to produce
outcomes.20
We haven’t described the internal operation of such trained AIs, mainly because we expect it to be a
mess in the same way that humans and other evolved systems are a mess.21
There are several categories of problems that make it difficult to specify goals. Each category
introduces an uncontrolled degree of freedom in the goal specification which exists because we
are only using feedback based on behavior. Because there are lots of potential degrees of freedom
that we don’t have control over (via behavioral training), we can think of the space of “intended
goals” as being a small subset of the space of “goals that empirically are pursued after training and
deployment”. In this way, behavioral training is imprecise and is exceedingly unlikely to nail down
the goal we intended. We describe multiple separate failure modes and so failure is disjunctive; we
only need one failure of goal specification for the AI to be misaligned.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---

## Extraction 2

**Term:** loss of control
**Location:** Section 6.1 (A misaligned AI achieving its goals would be bad for humans), page 26

**Extracted quote:**
> In this section we will discuss concretely why AI systems, which are capable of hard tasks and are misaligned, will likely lead to catastrophically bad outcomes for humans; outcomes such as extinction or total loss of control of the future.

**Context from source** (±3 sentences):
> We are uncertain about
these questions, but we expect the default outcomes to be bad for humans. Overall, it looks difficult but possible to achieve good outcomes by taking actions before a powerful
misaligned AI exists and is put to use, but that impressive levels of global coordination might be
required. After a misaligned AI gains any ability to act autonomously in the world, we expect that it
will be too late for humans to take any mitigating actions. 6.1
A misaligned AI achieving its goals would be bad for humans
In this section we will discuss concretely why AI systems, which are capable of hard tasks and are
misaligned, will likely lead to catastrophically bad outcomes for humans; outcomes such as extinction
or total loss of control of the future. Such an AI would be attempting to pursue outcomes, and be
extremely good at overcoming obstacles in order to achieve outcomes. Humans would be treated as
obstacles in the way of the AI achieving its goals, to whatever extent we are actually obstacles. 6.1.1
Instrumental convergence toward gaining control of limited resources
Resources and power are extremely useful for achieving a wide range of goals, especially goals about
the external world.

**Quote verification:** VERIFIED (ratio: 0.99)

**Reviewer decision:** [ ] Accept  [ ] Reject  [ ] Needs discussion

**Reviewer notes:**

---