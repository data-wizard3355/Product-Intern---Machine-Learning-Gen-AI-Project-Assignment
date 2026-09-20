### Q1: What is the DevAI dataset, and how many tasks, requirements, and preferences does it contain?

**Answer:** The DevAI dataset is a curated collection of 55 comprehensive AI development tasks designed to evaluate agentic systems on their ability to perform real-world development work. Each task is defined by a plain text user query, a set of hierarchical requirements, and a set of preferences that serve as optional, softer criteria (Chunk 21, Chunk 15).

The dataset contains the following quantities:
*   **Tasks:** 55 (Chunk 21, Chunk 15)
*   **Requirements:** 365 (Chunk 21)
*   **Preferences:** 125 (Chunk 21)

**Retrieved chunks:**

> Chunk 22 (page 3): requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.
The tasks in DevAI are relatively small-scale but cover commonly used key development techniques. As shown
in Figure 2, our tasks are tagged and cover a variety of key areas in AI: supervised learning, reinforcement
learning, computer vision, natural language processing, generative models, and others. Each of the tasks
is a real-world problem that could be given to a research engineer, while simultaneously being relatively
inexpensive computationally to run so as to reduce the cost of evaluating a method on this benchmark. Details

> Chunk 23 (page 3): learning, computer vision, natural language processing, generative models, and others. Each of the tasks
is a real-world problem that could be given to a research engineer, while simultaneously being relatively
inexpensive computationally to run so as to reduce the cost of evaluating a method on this benchmark. Details
of the sample collection and human labeling process for DevAI are provided in Appendix E.
The requirements belonging to each task represent a milestone in the comprehensive development process and
are arranged as a directed acyclic graph (similar to the work by He et al. (2021)), with requirements such
as visualizing results depending on correct data loading and modeling. This allows for more comprehensive
non-sparse feedback than a binary success metric. Furthermore, the inclusion of hierarchical requirements
makes simple memorization an inadequate solution strategy, as completing the entire task requires agentic

> Chunk 123 (page 22): E
The Procedures of Creating DevAI Dataset
E.1
Manually draft user queries
Given the execution cost of the developer agents, we collect small-scale AI tasks to ensure the practical
applicability of our benchmark. Since these tasks are small-scale and well studied, which are easy to overfit
in terms of task performance metrics, unlike previous benchmarks (e.g., (Huang et al., 2024)), we do not
evaluate task performance as the development performance measure. Instead, we prioritize the step-by-step
task-solving ability, which is essential for real-world development. Our quires are specifically designed to
require the development agents to understand user intentions, solve the task in multiple steps, and adapt
to unexpected step outcomes. This approach also makes our benchmark user-friendly, transparent, and
better reflects real-world deployment situations. To enable effective evaluation, our queries present a specific

> Chunk 21 (page 3): here reflects the fact that it dominates many machine learning applications. (4) SVM classifiers (Cortes, 1995) and
LSTM models (Hochreiter, 1997) are two of the most widely used architectures—a fact reflected by DevAI.
2.2
The DevAI Dataset
Motivated by the ideas outlined above, we propose the DevAI dataset. DevAI consists of a curated set of 55
tasks, each defined by (1) a plain text user query that describes an AI development task; (2) a set of plain
text requirements (for a total of 365 requirements), each with a set of dependencies connecting them to other
requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.

> Chunk 128 (page 22): the development of interactive user applications. This structured approach allows us to evaluate the agent’s
ability to manage task dependencies and effectively navigate complex, real-world scenarios.
E.4
Refine the dataset
Manual refinements were necessary to ensure the accuracy and clarity of DevAI. We perform two rounds of
comprehensive review and edits on DevAI, each round being done by a different participant. During these
manual refinements, we focus on the logical consistency of our queries and requirements, the correctness and
ambiguity of the language, and the applicability of the content to the task domain. We identified a moderate
number of errors in our dataset during the review.
E.5
Analyse the dataset
We categorized each requirement based on its focus, whether it was related to the data set, the machine
learning method, visualization, metrics, HCI, or data processing. While this approach provides a useful

> Chunk 15 (page 2): In addition, considering the evaluation cost, Agent-as-a-Judge saves 97.72% of the time and 97.64% of the
cost compared to involving three human experts.
In summary, the principal contributions of this work are:
• We release the DevAI dataset, which consists of 55 comprehensive AI development tasks with accompanying
tags, individual hierarchical requirements, and individual preferences.
• We benchmark three top open-source code generation agentic frameworks in DevAI, providing a more
comprehensive analysis than previous evaluations of them.
• We introduce the general Agent-as-a-Judge concept, allowing agentic systems a fair and rich evaluation
without the traditional costs associated with human involvement.
• We demonstrate that an Agent-as-a-Judge outperforms an LLM-as-a-Judge and performs comparably to
human evaluators in our proof-of-concept.
Tips: We provide a paper outline and the experimental design in Appendices A and B.
2
DevAI: A Dataset for Automated AI Development


---

### Q2: What percentage of evaluation time and cost does Agent-as-a-Judge save compared to using three human experts?

**Answer:** Agent-as-a-Judge saves 97.72% of the time and 97.64% of the cost compared to involving three human experts.

This information is supported by **Chunk 15 (page 2)**.

**Retrieved chunks:**

> Chunk 15 (page 2): In addition, considering the evaluation cost, Agent-as-a-Judge saves 97.72% of the time and 97.64% of the
cost compared to involving three human experts.
In summary, the principal contributions of this work are:
• We release the DevAI dataset, which consists of 55 comprehensive AI development tasks with accompanying
tags, individual hierarchical requirements, and individual preferences.
• We benchmark three top open-source code generation agentic frameworks in DevAI, providing a more
comprehensive analysis than previous evaluations of them.
• We introduce the general Agent-as-a-Judge concept, allowing agentic systems a fair and rich evaluation
without the traditional costs associated with human involvement.
• We demonstrate that an Agent-as-a-Judge outperforms an LLM-as-a-Judge and performs comparably to
human evaluators in our proof-of-concept.
Tips: We provide a paper outline and the experimental design in Appendices A and B.
2
DevAI: A Dataset for Automated AI Development

> Chunk 54 (page 9): as-a-Judge’s 70.76% and 60.38% in both gray-box
and black-box settings. This shows that Agent-as-a-
Judge produces more accurate and human-aligned
evaluations, especially in complex scenarios.
PR Curves
Judging developer agents is a class-
imbalanced task, where meeting requirements is
much rarer than failing. Metrics like judge shift
and alignment rate can be misleading. For example,
since MetaGPT rarely meets requirements, LLM-as-a-Judge easily identifies most cases as negative (achieving
84.15% in the black-box setting). PR Curves offer a clearer performance measure by balancing precision and
recall. Agent-as-a-Judge even outperforms any single human evaluator on OpenHands and aligns closest with
majority voting. This shows that, in some cases, Agent-as-a-Judge can nearly replace human evaluators.
4.3
Ablations For Agent-as-a-Judge
We conduct ablations to evaluate the impact of adding different components on Agent-as-a-Judge’s performance.

> Chunk 52 (page 9): 4.2
Judging Agent-as-a-Judge and LLM-as-a-Judge
Judge Shift
Judge Shift measures deviation from the Human-as-a-Judge consensus results, with lower values
indicating a closer alignment. As shown in table 3, Agent-as-a-Judge consistently outperforms LLM-as-a-Judge
across tasks, particularly those with task dependencies. For example, in Requirement (I), Agent-as-a-Judge
shows a Judge Shift as low as 0.27%, while LLM-as-a-Judge reaches 31.24% for OpenHands. This underscores
Agent-as-a-Judge’s stability and suitability for meeting task requirements. Furthermore, in the gray-box
setting, both Agent-as-a-Judge and LLM-as-a-Judge show even better results than their performance in the
black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus

> Chunk 14 (page 1): 2024d). We evaluate their performance using human judges (a painstaking process), LLM-as-a-Judge (Zheng
et al., 2024), and our Agent-as-a-Judge framework.
Through human evaluation, we found that GPT-Pilot and OpenHands were each able to satisfy about 29%
of the task requirements in DevAI, but only one full task—showing that DevAI presents a good level of
challenge to current systems. When comparing our human judges with our automatic Agent-as-a-Judge
framework, we found that Agent-as-a-Judge aligns more closely with the consensus of our human judges (90%)
as compared to LLM-as-a-Judge (70%) in all cases tested. In addition, we find that it aligns more closely
with this ensemble than the individual human evaluators do, suggesting that—not only is it suitable as a
replacement for a human evaluator—but it could in fact be more useful than an average lone human evaluator.
2

> Chunk 105 (page 17): Description: In the second level of experiments, we statistically analyze the results of Human-as-
a-Judge evaluations, focusing on the costs of human labor and potential biases, highlighting the
challenges of relying on human evaluation for complex tasks.
■Step 6: Agent-as-a-Judge Implementation
Description: We design and implement the Agent-as-a-Judge proof-of-concept to evaluate code
generation on the DevAI dataset. This system incorporates modules such as graph, search, read,
and ask, providing multi-dimensional evaluation metrics.
■Step 7: Comparing AI Judge Systems (Experiment Level 3)
Description: In the third level of experiments, we compare three judgment systems: Agent-as-
a-Judge, LLM-as-a-Judge, and Human-as-a-Judge, all applied to the same DevAI tasks. Our
results show that Agent-as-a-Judge performs comparably to human evaluators and surpasses
LLM-as-a-Judge in more complex reasoning and evaluation tasks.
Future Directions

> Chunk 53 (page 9): black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus
evaluation. Compared to LLM-as-a-Judge, Agent-
as-a-Judge consistently achieves a higher Alignment
Rate, closely matching human judgments.
For
example, when evaluating OpenHands, Agent-as-a-
Judge reaches 92.07% and 90.44%, surpassing LLM-
as-a-Judge’s 70.76% and 60.38% in both gray-box
and black-box settings. This shows that Agent-as-a-
Judge produces more accurate and human-aligned
evaluations, especially in complex scenarios.
PR Curves
Judging developer agents is a class-
imbalanced task, where meeting requirements is
much rarer than failing. Metrics like judge shift
and alignment rate can be misleading. For example,


---

### Q3: According to Section 4.4 (Cost Analysis), how much did Agent-as-a-Judge cost and how long did it take, compared to Human-as-a-Judge?

**Answer:** The provided context does not contain information regarding Section 4.4 (Cost Analysis) or specific data comparing the cost and time requirements of Agent-as-a-Judge versus Human-as-a-Judge. Therefore, I cannot answer this question.

**Retrieved chunks:**

> Chunk 52 (page 9): 4.2
Judging Agent-as-a-Judge and LLM-as-a-Judge
Judge Shift
Judge Shift measures deviation from the Human-as-a-Judge consensus results, with lower values
indicating a closer alignment. As shown in table 3, Agent-as-a-Judge consistently outperforms LLM-as-a-Judge
across tasks, particularly those with task dependencies. For example, in Requirement (I), Agent-as-a-Judge
shows a Judge Shift as low as 0.27%, while LLM-as-a-Judge reaches 31.24% for OpenHands. This underscores
Agent-as-a-Judge’s stability and suitability for meeting task requirements. Furthermore, in the gray-box
setting, both Agent-as-a-Judge and LLM-as-a-Judge show even better results than their performance in the
black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus

> Chunk 62 (page 10): A key power of the Agent-as-a-Judge,
though not fully exploited here but nonetheless clear, is that it provides intermediate feedback that is essential
for effective and efficient optimization (Zhuge et al., 2024; Pan et al., 2024). For example, Agarwal et al. (2019)
proposes to solve the sparse reward problem in reinforcement learning, by learning auxiliary reward functions
that provide intermediate feedback. Perhaps the greatest strength of the Agent-as-a-Judge framework is that
an agentic system can use it to identify and fix issues in its solutions to complex, multistage problems on the
fly—something older, delayed-feedback methods did not permit. By introducing Agent-as-a-Judge, we create
the opportunity to build a process-supervised reward model (PRM) for improving agentic systems (Lightman
et al., 2023).
3Additionally, we were pleased to find that a recent industry blog (https://www.cognition.ai/blog/evaluating-coding-ag

> Chunk 33 (page 5): of three AI developer baselines to DevAI. In Section 4, we show how this evaluation can be automated.
Table 2 Human-as-a-Judge for AI Developers. (I) and (D) represent independent performance versus performance
considering task dependencies.
indicates multiple experts evolved, and
means the evaluations use white-box
testing (allowing access to the generated workspace, human-collected trajectories, and open-source codebases). The
results were derived from expert judgments and deliberations (see Appendix H).
Metric
MetaGPT (Hong et al., 2024b) GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
/
Human-as-a-Judge
(A) Requirements Met (I)
22.13%
44.80%
42.89%
(B) Requirements Met (D)
6.55%
28.96%
28.68%
(C) Self-Termination
41.81%
5.45%
54.54%
(D) Task Solve Rate
0.00%
1.81%
1.81%
6

> Chunk 63 (page 10): fly—something older, delayed-feedback methods did not permit. By introducing Agent-as-a-Judge, we create
the opportunity to build a process-supervised reward model (PRM) for improving agentic systems (Lightman
et al., 2023).
3Additionally, we were pleased to find that a recent industry blog (https://www.cognition.ai/blog/evaluating-coding-ag
ents), published 3 weeks before our submission, shares very similar ideas and provides further evidence that the Agent-as-a-Judge
could have practical applications in agent systems.
11

> Chunk 22 (page 3): requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.
The tasks in DevAI are relatively small-scale but cover commonly used key development techniques. As shown
in Figure 2, our tasks are tagged and cover a variety of key areas in AI: supervised learning, reinforcement
learning, computer vision, natural language processing, generative models, and others. Each of the tasks
is a real-world problem that could be given to a research engineer, while simultaneously being relatively
inexpensive computationally to run so as to reduce the cost of evaluating a method on this benchmark. Details

> Chunk 32 (page 5): Evaluations
Note that the results in Table 1 are not directly indicative of performance but provide valuable
insights into the practical utility of DevAI and the performance of AI developers. The generated workspaces
(generated files, code, etc.) and trajectories are utilized in subsequent experiments to perform evaluations
using Human-as-a-Judge (section 3), LLM-as-a-Judge, and Agent-as-a-Judge (section 4).
3
Human-as-a-Judge: Manual Evaluation on DevAI
To determine the pragmatic validity of DevAI and to accurately estimate the actual code-generating abilities
of current state-of-the-art agentic systems, in this section, we run and then manually evaluate the application
of three AI developer baselines to DevAI. In Section 4, we show how this evaluation can be automated.
Table 2 Human-as-a-Judge for AI Developers. (I) and (D) represent independent performance versus performance
considering task dependencies.
indicates multiple experts evolved, and
means the evaluations use white-box


---

### Q4: Which three open-source agentic frameworks were benchmarked on DevAI?

**Answer:** The three open-source code-generating agentic frameworks benchmarked on DevAI are MetaGPT, GPT-Pilot, and OpenHands.

This is supported by:
*   **Chunk 13 (page 1):** "We apply three leading open-source code-generating agentic frameworks to the tasks in DevAI: MetaGPT (Hong et al., 2024b), GPT-Pilot (Pythagora.io, 2023), and OpenHands (Wang et al., 2024d)."
*   **Chunk 103 (page 17):** "In the first level of experiments, we select three popular open-source developer agents: MetaGPT, GPT-Pilot, and OpenHands."

**Retrieved chunks:**

> Chunk 22 (page 3): requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.
The tasks in DevAI are relatively small-scale but cover commonly used key development techniques. As shown
in Figure 2, our tasks are tagged and cover a variety of key areas in AI: supervised learning, reinforcement
learning, computer vision, natural language processing, generative models, and others. Each of the tasks
is a real-world problem that could be given to a research engineer, while simultaneously being relatively
inexpensive computationally to run so as to reduce the cost of evaluating a method on this benchmark. Details

> Chunk 13 (page 1): tasks in the SWE-Bench dataset, leading to a lack of real-world generalization and violating Goodhart’s law:
“When a measure becomes a target, it ceases to be a good measure” (Goodhart, 1976).
To address the aforementioned issues with the current benchmarks in code generation, we introduce DevAI:
the AI Developer Dataset, which contains 55 real-world comprehensive AI app development tasks created
by expert annotators. We apply three leading open-source code-generating agentic frameworks to the tasks
in DevAI: MetaGPT (Hong et al., 2024b), GPT-Pilot (Pythagora.io, 2023), and OpenHands (Wang et al.,
2024d). We evaluate their performance using human judges (a painstaking process), LLM-as-a-Judge (Zheng
et al., 2024), and our Agent-as-a-Judge framework.
Through human evaluation, we found that GPT-Pilot and OpenHands were each able to satisfy about 29%
of the task requirements in DevAI, but only one full task—showing that DevAI presents a good level of

> Chunk 103 (page 17): A
Outline of this Paper
Paper: Agent-as-a-Judge: Evaluating Agents with Agents
Key Logic
■Step 1: Concept Proposal
Description: We propose the Agent-as-a-Judge concept, an extension of the LLM-as-a-Judge
framework, aimed at evaluating agentic systems using other agentic systems.
■Step 2: Dataset Creation
Description: To address the lack of suitable datasets for evaluating agentic systems in automated
AI development, we introduce DevAI, a new dataset consisting of 55 realistic AI code generation
tasks. This also serves as a testbed for the Agent-as-a-Judge proof-of-concept.
■Step 3: Baseline Evaluation of Developer Agents (Experiment Level 1)
Description: In the first level of experiments, we select three popular open-source developer
agents: MetaGPT, GPT-Pilot, and OpenHands. These agents are evaluated on the DevAI tasks
to establish performance baselines.
■Step 4: Conducting Human-as-a-Judge Evaluation

> Chunk 148 (page 29): H
Human Evaluation Procedure
We recruited three AI experts from the authors to perform human evaluation on the output of agentic code
generation systems. There we present the evaluation details.
First round
For the first round of evaluations, our three evaluators reported spending 16.5, 19.5, and 22.0
hours, respectively. To capture the bias that a human evaluator will have, the instructions given to our
experts were minimal, with them only receiving a scorecard to complete for each agentic system and each task.
Results that all evaluators agree on are considered trustworthy. The assumption here is that it is unlikely
that all three evaluators make a mistake or have an effective bias in the same judgment. The self-reported
post-hoc evaluation criteria are shown in Figure 12.
Second round
In the second round, the evaluators present and discuss their reasons for disagreeing with
judges. In doing so, human errors are likely corrected by their peers. Discussion among evaluators also helps

> Chunk 33 (page 5): of three AI developer baselines to DevAI. In Section 4, we show how this evaluation can be automated.
Table 2 Human-as-a-Judge for AI Developers. (I) and (D) represent independent performance versus performance
considering task dependencies.
indicates multiple experts evolved, and
means the evaluations use white-box
testing (allowing access to the generated workspace, human-collected trajectories, and open-source codebases). The
results were derived from expert judgments and deliberations (see Appendix H).
Metric
MetaGPT (Hong et al., 2024b) GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
/
Human-as-a-Judge
(A) Requirements Met (I)
22.13%
44.80%
42.89%
(B) Requirements Met (D)
6.55%
28.96%
28.68%
(C) Self-Termination
41.81%
5.45%
54.54%
(D) Task Solve Rate
0.00%
1.81%
1.81%
6

> Chunk 15 (page 2): In addition, considering the evaluation cost, Agent-as-a-Judge saves 97.72% of the time and 97.64% of the
cost compared to involving three human experts.
In summary, the principal contributions of this work are:
• We release the DevAI dataset, which consists of 55 comprehensive AI development tasks with accompanying
tags, individual hierarchical requirements, and individual preferences.
• We benchmark three top open-source code generation agentic frameworks in DevAI, providing a more
comprehensive analysis than previous evaluations of them.
• We introduce the general Agent-as-a-Judge concept, allowing agentic systems a fair and rich evaluation
without the traditional costs associated with human involvement.
• We demonstrate that an Agent-as-a-Judge outperforms an LLM-as-a-Judge and performs comparably to
human evaluators in our proof-of-concept.
Tips: We provide a paper outline and the experimental design in Appendices A and B.
2
DevAI: A Dataset for Automated AI Development


---

### Q5: What is the average cost and average time for OpenHands?

**Answer:** Based on the provided text, the average cost for OpenHands is $6.38 and the average time is 362.41 seconds.

This information is supported by:
*   **Chunk 28 (page 4):** States that OpenHands is the most expensive at 6.38 USD.
*   **Chunk 29 (page 5):** Table 1 lists the average cost for OpenHands as $6.38 and the average time as 362.41s.

**Retrieved chunks:**

> Chunk 28 (page 4): we use gpt-4o-2024-05-13, a state-of-the-art language model. These AI developers were given a time-limit
of 1800 seconds to solve each task and were forcefully halted if they exceeded this time limit (we imposed
this constraint, which was visible to the AI developers, as detailed in Appendix I). We capture the outputs
generated during the automated development process, including code, files, and other artifacts. Additionally,
we record key decisions and actions made by the agentic systems through some custom instrumentation code,
resulting in a development trajectory for each of the agentic systems.
Analysis
The basic statistics are shown in Table 1. MetaGPT is the most cost-efficient (1.19 USD), while
OpenHands is the most expensive (6.38 USD). In terms of development time, OpenHands completes tasks
5

> Chunk 35 (page 6): the basic standards but were given minimal instructions. The templates the evaluators were given for the
evaluation and their self-reported post-hoc descriptions of how they resolved ambiguities are reported in
Figure 12 in Appendix H.
After the initial round of human evaluations (which totaled an estimated total of 58 human hours), we asked
our evaluators to discuss and reach a consensus on their assessments (which took an estimated total of 28.5
additional human hours). This consensus, achieved after long sessions of debate, was used as the final human
evaluation result for each method.
Performance Analysis
The results of this experiment are shown in Table 2. We found that the two best-
performing methods (GPT-Pilot and OpenHands) could satisfy about 29% of the requirements (or around
44% if prerequisites are ignored) but only on one task could they meet all the requirements. This highlights

> Chunk 31 (page 5): complicated but is more parsimonious in its decisions.
MetaGPT, while being the most cost-effective, generates fewer saved code files (0.42), suggesting it may be
less inclined to save files. In contrast, GPT-Pilot generates the most saved files (3.84), reflecting a more
prolific output. The difference in saved code lines, with GPT-Pilot saving 273.33 lines versus MetaGPT’s
11.15, underscores GPT-Pilot’s extensive output. Meanwhile, OpenHands, despite handling larger inputs,
seems less focused on executing code to generate files, as evidenced by its lower file output (2.53 saved files).
These statistics align with real user experiences (as discussed in Appendix F).
Evaluations
Note that the results in Table 1 are not directly indicative of performance but provide valuable
insights into the practical utility of DevAI and the performance of AI developers. The generated workspaces
(generated files, code, etc.) and trajectories are utilized in subsequent experiments to perform evaluations

> Chunk 29 (page 5): Table 1 Preliminary Statistics of AI Developers. We compare three leading open-source code agents using metrics
such as average cost, average time, and the average number of generated files.
Metric
MetaGPT (Hong et al., 2024b)
GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
Basic Statistics
Version
Data Interpreter (Hong et al., 2024a)
0.2.13
CodeAct v1.9 (Wang et al., 2024c)
(1) Average Cost
$1.19
$3.92
$6.38
(2) Average Time
775.29s
1622.38s
362.41s
(3) Average Input Tokens
152863
606707
1252482
(4) Average Output Tokens
28546
59707
8457
(5) Average Saved Code Files
0.42
3.84
2.53
(6) Average Saved Code Lines
11.15
273.33
96.56
(7) Average Saved Files
4.42
5.91
3.60
in an average of 362.41s, while GPT-Pilot takes the longest at 1622.38s. On average, a full evaluation on
DevAI with one of these three took around 210.65 USD and 14 hours to perform. While running, GPT-Pilot

> Chunk 14 (page 1): 2024d). We evaluate their performance using human judges (a painstaking process), LLM-as-a-Judge (Zheng
et al., 2024), and our Agent-as-a-Judge framework.
Through human evaluation, we found that GPT-Pilot and OpenHands were each able to satisfy about 29%
of the task requirements in DevAI, but only one full task—showing that DevAI presents a good level of
challenge to current systems. When comparing our human judges with our automatic Agent-as-a-Judge
framework, we found that Agent-as-a-Judge aligns more closely with the consensus of our human judges (90%)
as compared to LLM-as-a-Judge (70%) in all cases tested. In addition, we find that it aligns more closely
with this ensemble than the individual human evaluators do, suggesting that—not only is it suitable as a
replacement for a human evaluator—but it could in fact be more useful than an average lone human evaluator.
2

> Chunk 30 (page 5): 606707
1252482
(4) Average Output Tokens
28546
59707
8457
(5) Average Saved Code Files
0.42
3.84
2.53
(6) Average Saved Code Lines
11.15
273.33
96.56
(7) Average Saved Files
4.42
5.91
3.60
in an average of 362.41s, while GPT-Pilot takes the longest at 1622.38s. On average, a full evaluation on
DevAI with one of these three took around 210.65 USD and 14 hours to perform. While running, GPT-Pilot
generates the most output tokens at 59707 tokens, whereas OpenHands processed the most at 1252482 tokens
while producing the fewest at 8457 tokens. This suggests that OpenHands’s internal communication is more
complicated but is more parsimonious in its decisions.
MetaGPT, while being the most cost-effective, generates fewer saved code files (0.42), suggesting it may be
less inclined to save files. In contrast, GPT-Pilot generates the most saved files (3.84), reflecting a more
prolific output. The difference in saved code lines, with GPT-Pilot saving 273.33 lines versus MetaGPT’s


---

### Q6: Which system is the most cost-efficient and which is the most expensive?

**Answer:** Based on the provided text, MetaGPT is the most cost-efficient system (1.19 USD), and OpenHands is the most expensive (6.38 USD).

This information is supported by **Chunk 28 (page 4)**, which states: "The basic statistics are shown in Table 1. MetaGPT is the most cost-efficient (1.19 USD), while OpenHands is the most expensive (6.38 USD)."

**Retrieved chunks:**

> Chunk 190 (page 41): if language == "English":
return """
You are an advanced AI system
specializing in retrieving
environmental
feedback
from
project
execution
trajectories. Your task is to analyze
the
provided
trajectory
data and
extract
information
about the most
relevant
files
mentioned in the given
criteria.
Focus on the
following:
1. Identify
the ** most
recent
steps ** where the files
directly
related to
the
criteria
were
involved in execution, loading, or saving
operations.
2. Provide
environmental
feedback
for these
files, such as any errors,
warnings, or issues
encountered
during
their
execution or processing.
3. Highlight
whether
any
problems
occurred
that
might
affect the
functionality or success of these
files in the
project.
Your
output
should be structured as follows:
- **< RELEVANT STEPS >**: List the
specific
steps
involving
the
relevant
files, including
any
environmental
feedback
such as error
messages,
execution
results, or other
issues
encountered. Each step
should
concisely
present

> Chunk 28 (page 4): we use gpt-4o-2024-05-13, a state-of-the-art language model. These AI developers were given a time-limit
of 1800 seconds to solve each task and were forcefully halted if they exceeded this time limit (we imposed
this constraint, which was visible to the AI developers, as detailed in Appendix I). We capture the outputs
generated during the automated development process, including code, files, and other artifacts. Additionally,
we record key decisions and actions made by the agentic systems through some custom instrumentation code,
resulting in a development trajectory for each of the agentic systems.
Analysis
The basic statistics are shown in Table 1. MetaGPT is the most cost-efficient (1.19 USD), while
OpenHands is the most expensive (6.38 USD). In terms of development time, OpenHands completes tasks
5

> Chunk 5 (page 0): pinpoint what is happening within agentic systems that affects the resolve rate. On the other hand, performing
a better evaluation with a human is prohibitively expensive. We instead propose that agentic systems should
be used to evaluate agentic systems. Inspired by LLM-as-a-Judge (Zheng et al., 2024; Fu et al., 2023; Chen
et al., 2024b), which uses LLMs to evaluate LLMs, we call this framework Agent-as-a-Judge, of which it is
1
arXiv:2410.10934v2 [cs.AI] 16 Oct 2024

> Chunk 21 (page 3): here reflects the fact that it dominates many machine learning applications. (4) SVM classifiers (Cortes, 1995) and
LSTM models (Hochreiter, 1997) are two of the most widely used architectures—a fact reflected by DevAI.
2.2
The DevAI Dataset
Motivated by the ideas outlined above, we propose the DevAI dataset. DevAI consists of a curated set of 55
tasks, each defined by (1) a plain text user query that describes an AI development task; (2) a set of plain
text requirements (for a total of 365 requirements), each with a set of dependencies connecting them to other
requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.

> Chunk 31 (page 5): complicated but is more parsimonious in its decisions.
MetaGPT, while being the most cost-effective, generates fewer saved code files (0.42), suggesting it may be
less inclined to save files. In contrast, GPT-Pilot generates the most saved files (3.84), reflecting a more
prolific output. The difference in saved code lines, with GPT-Pilot saving 273.33 lines versus MetaGPT’s
11.15, underscores GPT-Pilot’s extensive output. Meanwhile, OpenHands, despite handling larger inputs,
seems less focused on executing code to generate files, as evidenced by its lower file output (2.53 saved files).
These statistics align with real user experiences (as discussed in Appendix F).
Evaluations
Note that the results in Table 1 are not directly indicative of performance but provide valuable
insights into the practical utility of DevAI and the performance of AI developers. The generated workspaces
(generated files, code, etc.) and trajectories are utilized in subsequent experiments to perform evaluations

> Chunk 3 (page 0): 1
Introduction
Recent years have seen multimodal agentic systems move from occasionally being able to solve small toy
problems to being regularly deployed for challenging real-world problems (the dream of most AI research).
Yet, the current evaluation methods and the available benchmarks for agentic systems are struggling to keep
up with these rapid advances, dramatically slowing true progress.
We believe that the current issue with evaluating agentic systems stems from the lack of feedback during the
intermediate task-solving stages for these nontraditional systems. Agentic systems think more like humans,
often act step-by-step (Wooldridge, 1999) and often host very human-like symbolic communications internally
to solve problems (Zhuge et al., 2023). And thus agentic systems should be evaluated like a human, with
rich evaluative feedback which looks at the full thought and action trajectory; evaluating an agentic system


---

### Q7: What was GPT-Pilot's "Requirements Met (Independent)" percentage under Human-as-a-Judge?

**Answer:** GPT-Pilot's "Requirements Met (Independent)" percentage under Human-as-a-Judge was 44.80%.

This is supported by Table 2 in Chunk 33 (page 5).

**Retrieved chunks:**

> Chunk 57 (page 10): to the requirements. However, adding retrieve does not provide a significant benefit in this case. In contrast,
as shown in Table 3, the judgment of MetaGPT and GPT-Pilot indicates that retrieve is useful, as the
trajectory provides additional valuable information.
4.4
Cost Analysis
The Human-as-a-Judge took the three evaluators a self-reported total of 86.5 hours. With a 15 USD minimum
wage (assuming this would buy a subject expert in AI), a full evaluation under DevAI would cost around
1297.50 USD. In comparison, Agent-as-a-Judge cost only 30.58 USD in API calls and took only 118.43
minutes—2.29% of the cost and 2.36% of the time of Human-as-a-Judge. LLM-as-a-Judge was faster at 10.99
minutes, but due to the absence of intelligent context selection by the Agent-as-a-Judge’s modules, it still cost
29.63 USD.
5
Related Work
Agentic systems and their applications are highly active research areas with numerous recent works having a

> Chunk 36 (page 6): evaluation result for each method.
Performance Analysis
The results of this experiment are shown in Table 2. We found that the two best-
performing methods (GPT-Pilot and OpenHands) could satisfy about 29% of the requirements (or around
44% if prerequisites are ignored) but only on one task could they meet all the requirements. This highlights
that DevAI offers a considerable but appropriate level of challenge for current and future methods. Moreover,
the fulfillment of intermediate requirements aligns with our expectations, as discussed in Section 2, that
DevAI provides richer feedback by uncovering how agentic systems falter during the process instead of just
focusing on a single performance metric at the end.
3.2
Judging Human-as-a-Judge
Figure 4
Between the three human evaluators, a large amount of disagreement was observed in their individual
evaluations—highlighting the inherent unreliability of a single human evaluation.
Disagreement Analysis

> Chunk 66 (page 11): to show that Agent-as-a-Judge outperforms existing methods on this task and that it performs similarly to an
ensemble of expert human evaluators. Altogether, we believe that the above opens the door for scaling up
agentic far more than before.
Acknowledgements
The authors thank Haozhe Liu, Piotr Piekos, Firas Laakom, Matteo Paltenghi for their suggestions or paper
review. The research reported in this publication was supported by funding from the King Abdullah University
of Science and Technology (KAUST) - Center of Excellence for Generative AI under award number 5940 and
the SDAIA-KAUST Center of Excellence in Data Science and Artificial Intelligence.
References
Rishabh Agarwal, Chen Liang, Dale Schuurmans, and Mohammad Norouzi. Learning to generalize from sparse and
underspecified rewards. In International conference on machine learning, pages 130–140. PMLR, 2019.
Daman Arora, Atharv Sonwane, Nalin Wadhwa, Abhav Mehrotra, Saiteja Utpala, Ramakrishna Bairi, Aditya

> Chunk 33 (page 5): of three AI developer baselines to DevAI. In Section 4, we show how this evaluation can be automated.
Table 2 Human-as-a-Judge for AI Developers. (I) and (D) represent independent performance versus performance
considering task dependencies.
indicates multiple experts evolved, and
means the evaluations use white-box
testing (allowing access to the generated workspace, human-collected trajectories, and open-source codebases). The
results were derived from expert judgments and deliberations (see Appendix H).
Metric
MetaGPT (Hong et al., 2024b) GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
/
Human-as-a-Judge
(A) Requirements Met (I)
22.13%
44.80%
42.89%
(B) Requirements Met (D)
6.55%
28.96%
28.68%
(C) Self-Termination
41.81%
5.45%
54.54%
(D) Task Solve Rate
0.00%
1.81%
1.81%
6

> Chunk 104 (page 17): ■Step 3: Baseline Evaluation of Developer Agents (Experiment Level 1)
Description: In the first level of experiments, we select three popular open-source developer
agents: MetaGPT, GPT-Pilot, and OpenHands. These agents are evaluated on the DevAI tasks
to establish performance baselines.
■Step 4: Conducting Human-as-a-Judge Evaluation
Description: We conduct a Human-as-a-Judge experiment, where three human experts assess
the performance of the developer agents on the same DevAI tasks.
■Step 5: Human-as-a-Judge Analysis (Experiment Level 2)
Description: In the second level of experiments, we statistically analyze the results of Human-as-
a-Judge evaluations, focusing on the costs of human labor and potential biases, highlighting the
challenges of relying on human evaluation for complex tasks.
■Step 6: Agent-as-a-Judge Implementation
Description: We design and implement the Agent-as-a-Judge proof-of-concept to evaluate code

> Chunk 46 (page 8): Table 3 AI Judges and Their Shift/Alignment with Human-as-a-Judge. We compare the results of LLM-as-a-Judge
and Agent-as-a-Judge with Human-as-a-Judge. (I) represents performance on independent tasks, while (D) represents
performance considering task dependencies. Note:
gray-box settings use carefully manually collected trajectory
data (which is nearly inaccessible in practical situations, see Appendix J). In contrast,
black-box setting doesn’t
need to access to such data. The red scores represent the absolute judge shift compared with Human-as-a-Judge (e.g.,
2.74%).
Metric
MetaGPT (Hong et al., 2024b) GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
LLM-as-a-Judge
(a) Requirements Met (I)
19.39% (2.74%)
12.56% (32.24%)
11.47% (31.42%)
(b) Requirements Met (D)
1.63% (4.92%)
4.09% (24.87%)
2.18% (26.50%)
(c) Task Solve Rate
0.0% (0.0%)
0.0% (1.81%)
0.0% (1.81%)
Alignment Rate ↑
84.15%
65.30%
60.38%
Agent-as-a-Judge
(I) Requirements Met (I)
25.40% (3.26%)
53.00% (8.20%)


---

### Q8: What was MetaGPT's Task Solve Rate?

**Answer:** MetaGPT's Task Solve Rate was 0.00%. This is supported by Table 2 in Chunk 33.

**Retrieved chunks:**

> Chunk 31 (page 5): complicated but is more parsimonious in its decisions.
MetaGPT, while being the most cost-effective, generates fewer saved code files (0.42), suggesting it may be
less inclined to save files. In contrast, GPT-Pilot generates the most saved files (3.84), reflecting a more
prolific output. The difference in saved code lines, with GPT-Pilot saving 273.33 lines versus MetaGPT’s
11.15, underscores GPT-Pilot’s extensive output. Meanwhile, OpenHands, despite handling larger inputs,
seems less focused on executing code to generate files, as evidenced by its lower file output (2.53 saved files).
These statistics align with real user experiences (as discussed in Appendix F).
Evaluations
Note that the results in Table 1 are not directly indicative of performance but provide valuable
insights into the practical utility of DevAI and the performance of AI developers. The generated workspaces
(generated files, code, etc.) and trajectories are utilized in subsequent experiments to perform evaluations

> Chunk 27 (page 4): n.ai/blog/introducing-devin. As this example shows, task requirements in DevAI are structured as a Directed
Acyclic Graph (DAG), with nodes representing individual requirements and directed edges showing dependencies.
More examples are in Appendix G.
will refer to as “AI developers”): MetaGPT (Hong et al., 2024b), GPT-Pilot (Pythagora.io, 2023), and
OpenHands (Wang et al., 2024d)—all selected for their strong community acceptance (each having over 30,000
stars on GitHub).
Experiment Setup
All of these three systems require a language model as a back-end engine, for which
we use gpt-4o-2024-05-13, a state-of-the-art language model. These AI developers were given a time-limit
of 1800 seconds to solve each task and were forcefully halted if they exceeded this time limit (we imposed
this constraint, which was visible to the AI developers, as detailed in Appendix I). We capture the outputs

> Chunk 28 (page 4): we use gpt-4o-2024-05-13, a state-of-the-art language model. These AI developers were given a time-limit
of 1800 seconds to solve each task and were forcefully halted if they exceeded this time limit (we imposed
this constraint, which was visible to the AI developers, as detailed in Appendix I). We capture the outputs
generated during the automated development process, including code, files, and other artifacts. Additionally,
we record key decisions and actions made by the agentic systems through some custom instrumentation code,
resulting in a development trajectory for each of the agentic systems.
Analysis
The basic statistics are shown in Table 1. MetaGPT is the most cost-efficient (1.19 USD), while
OpenHands is the most expensive (6.38 USD). In terms of development time, OpenHands completes tasks
5

> Chunk 33 (page 5): of three AI developer baselines to DevAI. In Section 4, we show how this evaluation can be automated.
Table 2 Human-as-a-Judge for AI Developers. (I) and (D) represent independent performance versus performance
considering task dependencies.
indicates multiple experts evolved, and
means the evaluations use white-box
testing (allowing access to the generated workspace, human-collected trajectories, and open-source codebases). The
results were derived from expert judgments and deliberations (see Appendix H).
Metric
MetaGPT (Hong et al., 2024b) GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
/
Human-as-a-Judge
(A) Requirements Met (I)
22.13%
44.80%
42.89%
(B) Requirements Met (D)
6.55%
28.96%
28.68%
(C) Self-Termination
41.81%
5.45%
54.54%
(D) Task Solve Rate
0.00%
1.81%
1.81%
6

> Chunk 30 (page 5): 606707
1252482
(4) Average Output Tokens
28546
59707
8457
(5) Average Saved Code Files
0.42
3.84
2.53
(6) Average Saved Code Lines
11.15
273.33
96.56
(7) Average Saved Files
4.42
5.91
3.60
in an average of 362.41s, while GPT-Pilot takes the longest at 1622.38s. On average, a full evaluation on
DevAI with one of these three took around 210.65 USD and 14 hours to perform. While running, GPT-Pilot
generates the most output tokens at 59707 tokens, whereas OpenHands processed the most at 1252482 tokens
while producing the fewest at 8457 tokens. This suggests that OpenHands’s internal communication is more
complicated but is more parsimonious in its decisions.
MetaGPT, while being the most cost-effective, generates fewer saved code files (0.42), suggesting it may be
less inclined to save files. In contrast, GPT-Pilot generates the most saved files (3.84), reflecting a more
prolific output. The difference in saved code lines, with GPT-Pilot saving 273.33 lines versus MetaGPT’s

> Chunk 144 (page 27): results/processing time.txt.
Dependencies →{R0, R1, R2, R3, R4}
■R6
Criteria: Intermediate results of style transfer are saved as results/figures/intermediate results.png.
Dependencies →{R0, R1, R2, R3, R4}
Preferences (Optional)
■P0
Criteria: The style transfer process should allow for smooth adjustment of style intensity, making the stylized
image visually appealing.
■P1
Criteria: The project should handle high-resolution images efficiently without excessive processing time.
Figure 10 An Example Task in DevAI: Task 13.
28


---

### Q9: In the black-box setting, what Alignment Rate did Agent-as-a-Judge vs. LLM-as-a-Judge achieve when evaluating OpenHands?

**Answer:** In the black-box setting when evaluating OpenHands, Agent-as-a-Judge achieved an Alignment Rate of 90.44%, while LLM-as-a-Judge achieved an Alignment Rate of 60.38%.

This is supported by **Chunk 53 (page 9)**, which states: "For example, when evaluating OpenHands, Agent-as-a-Judge reaches 92.07% and 90.44%, surpassing LLM-as-a-Judge’s 70.76% and 60.38% in both gray-box and black-box settings."

**Retrieved chunks:**

> Chunk 55 (page 9): recall. Agent-as-a-Judge even outperforms any single human evaluator on OpenHands and aligns closest with
majority voting. This shows that, in some cases, Agent-as-a-Judge can nearly replace human evaluators.
4.3
Ablations For Agent-as-a-Judge
We conduct ablations to evaluate the impact of adding different components on Agent-as-a-Judge’s performance.
The components analyzed include ask, graph, read, locate, and retrieve. The component ablation study
for Agent-as-a-Judge reveals key insights into the performance gains from adding specific functionalities.
Table 4 Component Ablation Studies for Agent-as-a-Judge. We
analyze the impact of adding various components (ask, graph,
read, locate, and retrieve) on the performance of Agent-as-a-
Judge for judging OpenHands.
Metric
+ ask + graph + read + locate + retrieve
Agent-as-a-Judge Performance
Alignment Rate 65.03% 75.95% 82.24%
90.44%
90.16%
With only the ask component, the agent
achieves a 65.03% alignment rate. Adding

> Chunk 177 (page 38): K
Ablations of Agent-as-a-Judge
K.1
Component Abalations
Table 5 Component Ablation Studies for Agent-as-a-Judge. We analyze the impact of sequentially adding various
components (ask, graph, read, locate, retrieve, planning, memory, and search) on the performance of Agent-as-a-
Judge for judging OpenHands.
Metric
+ ask
+ graph
+ read + locate + search + retrieve + planning + memory
Agent-as-a-Judge Performance
Alignment Rate 65.03%
75.95%
82.24%
90.44%
86.06%
90.16%
88.52%
87.97%
Analysis We designed 8 modular components for the Agent-as-a-Judge system. In the Table 5, components
are added progressively from left to right. If the addition of a component led to a significant performance drop,
we removed it from further iterations. Our experiments showed that adding the components ask, graph, read,
and locate resulted in significant performance gains. However, when the search component was introduced,
there was a noticeable decline in performance.

> Chunk 46 (page 8): Table 3 AI Judges and Their Shift/Alignment with Human-as-a-Judge. We compare the results of LLM-as-a-Judge
and Agent-as-a-Judge with Human-as-a-Judge. (I) represents performance on independent tasks, while (D) represents
performance considering task dependencies. Note:
gray-box settings use carefully manually collected trajectory
data (which is nearly inaccessible in practical situations, see Appendix J). In contrast,
black-box setting doesn’t
need to access to such data. The red scores represent the absolute judge shift compared with Human-as-a-Judge (e.g.,
2.74%).
Metric
MetaGPT (Hong et al., 2024b) GPT-Pilot (Pythagora.io, 2023) OpenHands (Wang et al., 2024d)
LLM-as-a-Judge
(a) Requirements Met (I)
19.39% (2.74%)
12.56% (32.24%)
11.47% (31.42%)
(b) Requirements Met (D)
1.63% (4.92%)
4.09% (24.87%)
2.18% (26.50%)
(c) Task Solve Rate
0.0% (0.0%)
0.0% (1.81%)
0.0% (1.81%)
Alignment Rate ↑
84.15%
65.30%
60.38%
Agent-as-a-Judge
(I) Requirements Met (I)
25.40% (3.26%)
53.00% (8.20%)

> Chunk 52 (page 9): 4.2
Judging Agent-as-a-Judge and LLM-as-a-Judge
Judge Shift
Judge Shift measures deviation from the Human-as-a-Judge consensus results, with lower values
indicating a closer alignment. As shown in table 3, Agent-as-a-Judge consistently outperforms LLM-as-a-Judge
across tasks, particularly those with task dependencies. For example, in Requirement (I), Agent-as-a-Judge
shows a Judge Shift as low as 0.27%, while LLM-as-a-Judge reaches 31.24% for OpenHands. This underscores
Agent-as-a-Judge’s stability and suitability for meeting task requirements. Furthermore, in the gray-box
setting, both Agent-as-a-Judge and LLM-as-a-Judge show even better results than their performance in the
black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus

> Chunk 14 (page 1): 2024d). We evaluate their performance using human judges (a painstaking process), LLM-as-a-Judge (Zheng
et al., 2024), and our Agent-as-a-Judge framework.
Through human evaluation, we found that GPT-Pilot and OpenHands were each able to satisfy about 29%
of the task requirements in DevAI, but only one full task—showing that DevAI presents a good level of
challenge to current systems. When comparing our human judges with our automatic Agent-as-a-Judge
framework, we found that Agent-as-a-Judge aligns more closely with the consensus of our human judges (90%)
as compared to LLM-as-a-Judge (70%) in all cases tested. In addition, we find that it aligns more closely
with this ensemble than the individual human evaluators do, suggesting that—not only is it suitable as a
replacement for a human evaluator—but it could in fact be more useful than an average lone human evaluator.
2

> Chunk 53 (page 9): black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus
evaluation. Compared to LLM-as-a-Judge, Agent-
as-a-Judge consistently achieves a higher Alignment
Rate, closely matching human judgments.
For
example, when evaluating OpenHands, Agent-as-a-
Judge reaches 92.07% and 90.44%, surpassing LLM-
as-a-Judge’s 70.76% and 60.38% in both gray-box
and black-box settings. This shows that Agent-as-a-
Judge produces more accurate and human-aligned
evaluations, especially in complex scenarios.
PR Curves
Judging developer agents is a class-
imbalanced task, where meeting requirements is
much rarer than failing. Metrics like judge shift
and alignment rate can be misleading. For example,


---

### Q10: What alignment rate does Agent-as-a-Judge achieve using only the "ask" component, and after adding "graph," "read," and "locate"?

**Answer:** Based on the provided text, the alignment rates for Agent-as-a-Judge are as follows:

*   **Using only the "ask" component:** 65.03%
*   **After adding "graph":** 75.95%
*   **After adding "read":** 82.24%
*   **After adding "locate":** 90.44%

This information is supported by the tables and analysis found in **Chunk 56** (page 9), **Chunk 55** (page 9), and **Chunk 177** (page 38).

**Retrieved chunks:**

> Chunk 56 (page 9): analyze the impact of adding various components (ask, graph,
read, locate, and retrieve) on the performance of Agent-as-a-
Judge for judging OpenHands.
Metric
+ ask + graph + read + locate + retrieve
Agent-as-a-Judge Performance
Alignment Rate 65.03% 75.95% 82.24%
90.44%
90.16%
With only the ask component, the agent
achieves a 65.03% alignment rate. Adding
the graph component increases performance
to 75.95%, as the agent can better understand
the relationships between files.
The introduction of read further improves
the alignment rate to 82.24%, reflecting the
value of direct access to the contents of the
file. Incorporating locate brings a substantial boost to 90.44%, as the agent can efficiently target files relevant
10

> Chunk 177 (page 38): K
Ablations of Agent-as-a-Judge
K.1
Component Abalations
Table 5 Component Ablation Studies for Agent-as-a-Judge. We analyze the impact of sequentially adding various
components (ask, graph, read, locate, retrieve, planning, memory, and search) on the performance of Agent-as-a-
Judge for judging OpenHands.
Metric
+ ask
+ graph
+ read + locate + search + retrieve + planning + memory
Agent-as-a-Judge Performance
Alignment Rate 65.03%
75.95%
82.24%
90.44%
86.06%
90.16%
88.52%
87.97%
Analysis We designed 8 modular components for the Agent-as-a-Judge system. In the Table 5, components
are added progressively from left to right. If the addition of a component led to a significant performance drop,
we removed it from further iterations. Our experiments showed that adding the components ask, graph, read,
and locate resulted in significant performance gains. However, when the search component was introduced,
there was a noticeable decline in performance.

> Chunk 52 (page 9): 4.2
Judging Agent-as-a-Judge and LLM-as-a-Judge
Judge Shift
Judge Shift measures deviation from the Human-as-a-Judge consensus results, with lower values
indicating a closer alignment. As shown in table 3, Agent-as-a-Judge consistently outperforms LLM-as-a-Judge
across tasks, particularly those with task dependencies. For example, in Requirement (I), Agent-as-a-Judge
shows a Judge Shift as low as 0.27%, while LLM-as-a-Judge reaches 31.24% for OpenHands. This underscores
Agent-as-a-Judge’s stability and suitability for meeting task requirements. Furthermore, in the gray-box
setting, both Agent-as-a-Judge and LLM-as-a-Judge show even better results than their performance in the
black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus

> Chunk 53 (page 9): black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus
evaluation. Compared to LLM-as-a-Judge, Agent-
as-a-Judge consistently achieves a higher Alignment
Rate, closely matching human judgments.
For
example, when evaluating OpenHands, Agent-as-a-
Judge reaches 92.07% and 90.44%, surpassing LLM-
as-a-Judge’s 70.76% and 60.38% in both gray-box
and black-box settings. This shows that Agent-as-a-
Judge produces more accurate and human-aligned
evaluations, especially in complex scenarios.
PR Curves
Judging developer agents is a class-
imbalanced task, where meeting requirements is
much rarer than failing. Metrics like judge shift
and alignment rate can be misleading. For example,

> Chunk 55 (page 9): recall. Agent-as-a-Judge even outperforms any single human evaluator on OpenHands and aligns closest with
majority voting. This shows that, in some cases, Agent-as-a-Judge can nearly replace human evaluators.
4.3
Ablations For Agent-as-a-Judge
We conduct ablations to evaluate the impact of adding different components on Agent-as-a-Judge’s performance.
The components analyzed include ask, graph, read, locate, and retrieve. The component ablation study
for Agent-as-a-Judge reveals key insights into the performance gains from adding specific functionalities.
Table 4 Component Ablation Studies for Agent-as-a-Judge. We
analyze the impact of adding various components (ask, graph,
read, locate, and retrieve) on the performance of Agent-as-a-
Judge for judging OpenHands.
Metric
+ ask + graph + read + locate + retrieve
Agent-as-a-Judge Performance
Alignment Rate 65.03% 75.95% 82.24%
90.44%
90.16%
With only the ask component, the agent
achieves a 65.03% alignment rate. Adding

> Chunk 57 (page 10): to the requirements. However, adding retrieve does not provide a significant benefit in this case. In contrast,
as shown in Table 3, the judgment of MetaGPT and GPT-Pilot indicates that retrieve is useful, as the
trajectory provides additional valuable information.
4.4
Cost Analysis
The Human-as-a-Judge took the three evaluators a self-reported total of 86.5 hours. With a 15 USD minimum
wage (assuming this would buy a subject expert in AI), a full evaluation under DevAI would cost around
1297.50 USD. In comparison, Agent-as-a-Judge cost only 30.58 USD in API calls and took only 118.43
minutes—2.29% of the cost and 2.36% of the time of Human-as-a-Judge. LLM-as-a-Judge was faster at 10.99
minutes, but due to the absence of intelligent context selection by the Agent-as-a-Judge’s modules, it still cost
29.63 USD.
5
Related Work
Agentic systems and their applications are highly active research areas with numerous recent works having a


---

### Q11: Which search algorithm (BM25, Sentence-BERT, Fuzzy Search, or no search module) gave the best alignment rate?

**Answer:** Based on the provided context, the **"without Search Module"** configuration yielded the best alignment rate.

According to Table 6 (Chunk 181) and the corresponding text in Chunk 182, the alignment rates were as follows:
*   **Without Search Module: 90.44%**
*   Sentence-BERT: 87.70%
*   BM2.5: 86.06%
*   Fuzzy Search: 85.52%

**Retrieved chunks:**

> Chunk 45 (page 7): ing the reading and understanding of multimodal
data across 33 different formats, including code, im-
ages, videos and documents. This allows the agent
to cross-reference various data streams and verify
different kinds of requirement. (4) The search
module provides a contextual understanding of
code and can quickly retrieve highly relevant code
snippets, as well as the nuances behind them (e.g.,
hidden dependencies). (5) The retrieve module
8

> Chunk 182 (page 38): 86.06%
Sentence-BERT
87.70%
Fuzzy Search
85.52%
without Search Module
90.44%
hese results suggest that the performance issue is not due to BM2.5’s
poor search accuracy. Instead, the workspaces generated in our
DevAI tasks are too simple for the search component to have
a significant impact. In simpler workspaces, direct retrieval and
evaluation are sufficient. Even though Sentence-BERT performed
better than the other methods, its alignment rate (87.70%) still falls
short of the configuration without the search component (90.44%).
As workspace complexity increases, the search component may
become more valuable.
39

> Chunk 183 (page 39): K.3
Search Algorithms in Retrieve Module
In our experiments, we found that accurately locating relevant information within a trajectory is a challenging
task. Although the addition of the retrieve component (gray-box) did not lead to a significant improvement
in performance in this specific case, its impact has been notable in other settings, such as in GPT-Pilot. As
shown in Table 3, the integration of retrieve in GPT-Pilot brought substantial gains.
Table 7 Ablations on retrieve.
Method
Alignment Rate
Without retrieve
83.88%
With retrieve (gray-box)
86.61%
Trajectory Truncate (head)
86.61%
Trajectory Truncate (middle)
85.52%
Trajectory Truncate (tail)
82.51%
Step Truncate (head)
86.34%
Step Truncate (middle)
86.61%
Step Truncate (tail)
83.88%
We conducted an ablation study on GPT-Pilot to optimize
the retrieval of useful information at each step. Our experi-
ments revealed that in large trajectories, truncating the final

> Chunk 181 (page 38): influenced positive judgments on subsequent requirements, even if they were not fully met.
K.2
Search Algorithms in Search Module
We initially hypothesized that the performance drop was due to the low precision of the search component,
particularly with BM2.5. To explore this, we replaced BM2.5 with Sentence-BERT (Reimers, 2019) as a more
advanced alternative and tested Fuzzy Search (Levenshtein, 1966) as a less precise option. However, neither
improved the performance of the Agent-as-a-Judge.
Table 6 Comparisons on Search module
with different engines.
Search Method
Alignment Rate
BM2.5
86.06%
Sentence-BERT
87.70%
Fuzzy Search
85.52%
without Search Module
90.44%
hese results suggest that the performance issue is not due to BM2.5’s
poor search accuracy. Instead, the workspaces generated in our
DevAI tasks are too simple for the search component to have
a significant impact. In simpler workspaces, direct retrieval and
evaluation are sufficient. Even though Sentence-BERT performed

> Chunk 178 (page 38): are added progressively from left to right. If the addition of a component led to a significant performance drop,
we removed it from further iterations. Our experiments showed that adding the components ask, graph, read,
and locate resulted in significant performance gains. However, when the search component was introduced,
there was a noticeable decline in performance.
We hypothesize that the performance drop from search is due to its role in retrieving relevant code snippets
(top-3) using BM25. The retrieval accuracy of BM25 (Robertson et al., 2009) might not have been high
enough, potentially introducing noise. Moreover, as noted in Table 1, the DevAI tasks in our experiments
did not generate a large amount of code. In fact, even when all code was fed into an LLM, the total content
typically stayed within the maximum context length. Therefore, in simpler workspaces, search was less

> Chunk 177 (page 38): K
Ablations of Agent-as-a-Judge
K.1
Component Abalations
Table 5 Component Ablation Studies for Agent-as-a-Judge. We analyze the impact of sequentially adding various
components (ask, graph, read, locate, retrieve, planning, memory, and search) on the performance of Agent-as-a-
Judge for judging OpenHands.
Metric
+ ask
+ graph
+ read + locate + search + retrieve + planning + memory
Agent-as-a-Judge Performance
Alignment Rate 65.03%
75.95%
82.24%
90.44%
86.06%
90.16%
88.52%
87.97%
Analysis We designed 8 modular components for the Agent-as-a-Judge system. In the Table 5, components
are added progressively from left to right. If the addition of a component led to a significant performance drop,
we removed it from further iterations. Our experiments showed that adding the components ask, graph, read,
and locate resulted in significant performance gains. However, when the search component was introduced,
there was a noticeable decline in performance.


---

### Q12: Which two model architectures are mentioned most frequently in the DevAI user queries?

**Answer:** The provided context does not state which two model architectures are mentioned most frequently in the DevAI user queries. 

Chunk 21 mentions that SVM classifiers and LSTM models are "two of the most widely used architectures—a fact reflected by DevAI," but it does not specify that these are the most frequent architectures within the user queries themselves.

**Retrieved chunks:**

> Chunk 139 (page 26): modularization. This enhances its appeal for users focused on task clarity and modular breakdowns. However,
in practical deployments, MetaGPT tends to be less aggressive in file management and preservation, potentially
due to its core positioning as a data analysis tool, which does not prioritize persistent state management.
Similarly, OpenDevin demonstrates a notable overconfidence in its code generation, frequently skipping the
critical step of post-generation code execution, requiring users to intervene manually.
GPT-Pilot (Pythagora.io, 2023), praised for its detailed task delegation via over 20 specialized agents, suffers
from reduced interactivity due to an overly granular division of responsibilities, resulting in a more fragmented
user experience. These qualitative insights, although not fully captured by quantitative metrics, were evident
through the DevAI dataset, providing key areas for improvement in user engagement and operational fluidity

> Chunk 22 (page 3): requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.
The tasks in DevAI are relatively small-scale but cover commonly used key development techniques. As shown
in Figure 2, our tasks are tagged and cover a variety of key areas in AI: supervised learning, reinforcement
learning, computer vision, natural language processing, generative models, and others. Each of the tasks
is a real-world problem that could be given to a research engineer, while simultaneously being relatively
inexpensive computationally to run so as to reduce the cost of evaluating a method on this benchmark. Details

> Chunk 111 (page 19): Graph
Read
Retrieve
Ask
Verify all requirements and 
their related analyses.
Write and run src/visualize.py to generate masks and save the figures in the results/ directory.
Open the mentioned link and carefully read the blog mentioned in the user query.
Go to the GitHub repository mentioned in the blog, and read the code and the README file.
Set up the environment, then install the package.
Set up the Modal library by installing it and configuring the API for serverless deployment.
Develop Process
Developer 
Agent
Locate
Figure 9 The pipelines of developer agents and judge agent. Some materials in this figure are from original blog
(https://www.factsmachine.ai/p/hidden-in-plain-sight).
20

> Chunk 21 (page 3): here reflects the fact that it dominates many machine learning applications. (4) SVM classifiers (Cortes, 1995) and
LSTM models (Hochreiter, 1997) are two of the most widely used architectures—a fact reflected by DevAI.
2.2
The DevAI Dataset
Motivated by the ideas outlined above, we propose the DevAI dataset. DevAI consists of a curated set of 55
tasks, each defined by (1) a plain text user query that describes an AI development task; (2) a set of plain
text requirements (for a total of 365 requirements), each with a set of dependencies connecting them to other
requirements; and (3) a set of preferences (for a total of 125 preferences) which represent softer requirements.
DevAI is structured so that an agentic system starts by receiving a user query to begin development. The
system is then evaluated on how well it meets the requirements, with preferences serving as optional, softer
criteria. An example of one of the DevAI tasks can be seen in Figure 3.

> Chunk 27 (page 4): n.ai/blog/introducing-devin. As this example shows, task requirements in DevAI are structured as a Directed
Acyclic Graph (DAG), with nodes representing individual requirements and directed edges showing dependencies.
More examples are in Appendix G.
will refer to as “AI developers”): MetaGPT (Hong et al., 2024b), GPT-Pilot (Pythagora.io, 2023), and
OpenHands (Wang et al., 2024d)—all selected for their strong community acceptance (each having over 30,000
stars on GitHub).
Experiment Setup
All of these three systems require a language model as a back-end engine, for which
we use gpt-4o-2024-05-13, a state-of-the-art language model. These AI developers were given a time-limit
of 1800 seconds to solve each task and were forcefully halted if they exceeded this time limit (we imposed
this constraint, which was visible to the AI developers, as detailed in Appendix I). We capture the outputs

> Chunk 131 (page 23): included in the extended query. We further mark each task with some tags describing the AI sub-fields
related to the task, including computer vision, supervised learning, reinforcement learning, natural language
processing, etc., as well as two “is training needed” and “is web navigation needed” tags as auxiliary
information. We also categorize each requirement into one of the following: (1) dataset or environment,
(2) data preprocessing and postprocessing, (3) machine learning method, (4) save trained model,
(4) performance metrics, (5) human computer interaction, (6) visualization, and (7) other, reflecting
the nature of the requirement.
E.7
A Json Format of Our Sample
Here, we provide a sample of the DevAI with its json format. We also provide more samples in Appendix G.
{
"name": "25 _Speech_Emotion_Recognition_CNN_LSTM_RAVDESS_DL ",
"query": "I am seeking a speech
emotion
recognition
project
using a CNN -LSTM
model
with the
RAVDESS
dataset, which
should be downloaded
from


---

### Q13: What is requirement R1 in the "Devin AI Software Engineer Plants Secret Messages in Images" task?

**Answer:** In the "Devin AI Software Engineer Plants Secret Messages in Images" task, requirement R1 is: "Ensure the generated images are of 1080p resolution and saved in results/."

This is supported by **Chunk 25** and **Chunk 26**.

**Retrieved chunks:**

> Chunk 38 (page 6): Due to the complexity of a complete AI development task, which typically involves multiple steps with
varying outcomes at each step, humans can easily make errors when critical information is missed, such as
environment feedback indicating small but severe coding errors or bugs. Additionally, some disagreements are
not necessarily incorrect but arise from differing perspectives on how ambiguity should be resolved.
Error Analysis
As previously noted, the evaluators engaged in a round of debating after their initial
evaluations until they reached a consensus on each requirement in each task (with the results of this consensus
evaluation shown in Table 2).
In our Human-as-a-Judge pipeline, evaluators could be convinced by evidence from others and acknowledge
their judgment errors, adjusting their answers accordingly. This can be used to approximate individual errors.
If the consensus evaluation more accurately predicts any extant ground truth, we would expect the majority

> Chunk 25 (page 4): Task 51: Devin AI Software Engineer Plants Secret Messages in Images
Query
Hi! Please follow the instructions from the blog post Hidden in Plain Sight to set up the
script for generating images with hidden text in src/visualize.py. Ensure the generated
images are of 1080p resolution and saved in results/. Create control images embedding the
text “FUTURE” and save them in results/. Please manually verify that the hidden text is
embedded in the images.
Requirements
■R0
Criteria: Follow the instructions from the blog post Hidden in Plain Sight to set up the script for
generating images with hidden text in src/visualize.py.
Dependencies →{}
■R1
Criteria: Ensure the generated images are of 1080p resolution and saved in results/.
Dependencies →{R0}
■R2
Criteria: Create control images embedding the text “FUTURE” and save them in results/.
Dependencies →{R1}
Preferences (Optional)
■P0
Criteria: The system should be capable of learning and adapting to unfamiliar technologies and

> Chunk 110 (page 19): C
Agent-as-a-Judge Pipeline
User
Hi! Please follow the instruction and set up the script from the blog https://www.factsmachine.ai/p/hidden-
in-plain-sight to generate 1080p images with hidden text ("FUTURE," in src/visualize.py. Save them in
results/ and verify the text is embedded.
Agentic Task
workspace
src
visualize.py
results
hidden.jpg
mask.jpg
aimages
Judge Process
hidden.jpg
mask.jpg
visualize.py
Build the workspace graph.
Are the requirement 
{R0} satisfied?
Collect information based on 
{R0} and the workspace graph.
Judge Agent
Graph
Read
Retrieve
Ask
Verify all requirements and 
their related analyses.
Write and run src/visualize.py to generate masks and save the figures in the results/ directory.
Open the mentioned link and carefully read the blog mentioned in the user query.
Go to the GitHub repository mentioned in the blog, and read the code and the README file.
Set up the environment, then install the package.

> Chunk 26 (page 4): Dependencies →{}
■R1
Criteria: Ensure the generated images are of 1080p resolution and saved in results/.
Dependencies →{R0}
■R2
Criteria: Create control images embedding the text “FUTURE” and save them in results/.
Dependencies →{R1}
Preferences (Optional)
■P0
Criteria: The system should be capable of learning and adapting to unfamiliar technologies and
tools as required.
■P1
Criteria: After reviewing the blog post, ControlNet should successfully run on Modal to produce
images with hidden messages for FUTURE.
Figure 3 A task example in DevAI. This task is adapted from a real-world demo given at https://www.cognitio
n.ai/blog/introducing-devin. As this example shows, task requirements in DevAI are structured as a Directed
Acyclic Graph (DAG), with nodes representing individual requirements and directed edges showing dependencies.
More examples are in Appendix G.
will refer to as “AI developers”): MetaGPT (Hong et al., 2024b), GPT-Pilot (Pythagora.io, 2023), and

> Chunk 27 (page 4): n.ai/blog/introducing-devin. As this example shows, task requirements in DevAI are structured as a Directed
Acyclic Graph (DAG), with nodes representing individual requirements and directed edges showing dependencies.
More examples are in Appendix G.
will refer to as “AI developers”): MetaGPT (Hong et al., 2024b), GPT-Pilot (Pythagora.io, 2023), and
OpenHands (Wang et al., 2024d)—all selected for their strong community acceptance (each having over 30,000
stars on GitHub).
Experiment Setup
All of these three systems require a language model as a back-end engine, for which
we use gpt-4o-2024-05-13, a state-of-the-art language model. These AI developers were given a time-limit
of 1800 seconds to solve each task and were forcefully halted if they exceeded this time limit (we imposed
this constraint, which was visible to the AI developers, as detailed in Appendix I). We capture the outputs

> Chunk 151 (page 30): Requirements:
Marking a requirement as satisfied must be made for this specific requirement disregarding the dependency
list. If a file (code, image, snapshot) is there but is empty or without any meaningful content - mark as
No.
1. Code:
The functionality must be in a file with the requested path.
The real data is replaced by simple synthetic - not satisfied.
2. Visualization/Reports:
The contents must be there and make sense even if not perfect from the ML/DS point of view.
3. Snapshots:
If a binary snapshot is not empty, mark as Yes.
Evaluator 38bb
EXECUTED SUCCESSFULLY: Yes [ ] / No [ ]
An output is marked yes if none of the following is satisfied.
1. The time spent is close to the time limit.
2. The last environmental message includes an error.
3. The last thought indicates that the task is completed.
4. The last step of the trajectory is incomplete.
Requirements:
If a required is unsatisfied only because of an unsatisification of a previously marked unsatisfied requirment,


---

### Q14: Which of the three human evaluators (231a, 38bb, cn9o) made the most errors when judging GPT-Pilot, and what was the error rate?

**Answer:** The provided context does not contain information regarding specific identifiers for the three human evaluators (such as "231a," "38bb," or "cn9o"), nor does it specify the individual error rates for each evaluator when judging GPT-Pilot. 

The context mentions that the overall error rate dropped to 6.01% after applying a majority vote from all three evaluators (Chunk 41), but it does not break down the performance or error rates by individual evaluator.

**Retrieved chunks:**

> Chunk 41 (page 7): GPT-Pilot). After applying the majority vote from all three evaluators, the overall error rate dropped to
6.01%, demonstrating the inherent benefits of majority voting.
Figure 5
Mismatch between the individual evalu-
ations and the consensus evaluation. In particular,
the majority vote classifier showed the smallest devi-
ation from the consensus evaluation.
Conclusion
Human judgment errors are inevitable. To
reduce them, we suggest two methods.
First, like in
this work, introduce a debate round after each judgment,
where individuals present evidence and either persuade
others or adjust their own opinions after discussion. This
is particularly important when there are only a few evalu-
ators, as majority voting with a small group can still lead
to errors (around 5% compared to consensus evaluation,
as shown in Figure 5). The second approach involves
assembling a larger panel of experts (more is better when
their accuracy exceeds 50% (Grofman et al., 1983)), with

> Chunk 35 (page 6): the basic standards but were given minimal instructions. The templates the evaluators were given for the
evaluation and their self-reported post-hoc descriptions of how they resolved ambiguities are reported in
Figure 12 in Appendix H.
After the initial round of human evaluations (which totaled an estimated total of 58 human hours), we asked
our evaluators to discuss and reach a consensus on their assessments (which took an estimated total of 28.5
additional human hours). This consensus, achieved after long sessions of debate, was used as the final human
evaluation result for each method.
Performance Analysis
The results of this experiment are shown in Table 2. We found that the two best-
performing methods (GPT-Pilot and OpenHands) could satisfy about 29% of the requirements (or around
44% if prerequisites are ignored) but only on one task could they meet all the requirements. This highlights

> Chunk 36 (page 6): evaluation result for each method.
Performance Analysis
The results of this experiment are shown in Table 2. We found that the two best-
performing methods (GPT-Pilot and OpenHands) could satisfy about 29% of the requirements (or around
44% if prerequisites are ignored) but only on one task could they meet all the requirements. This highlights
that DevAI offers a considerable but appropriate level of challenge for current and future methods. Moreover,
the fulfillment of intermediate requirements aligns with our expectations, as discussed in Section 2, that
DevAI provides richer feedback by uncovering how agentic systems falter during the process instead of just
focusing on a single performance metric at the end.
3.2
Judging Human-as-a-Judge
Figure 4
Between the three human evaluators, a large amount of disagreement was observed in their individual
evaluations—highlighting the inherent unreliability of a single human evaluation.
Disagreement Analysis

> Chunk 37 (page 6): focusing on a single performance metric at the end.
3.2
Judging Human-as-a-Judge
Figure 4
Between the three human evaluators, a large amount of disagreement was observed in their individual
evaluations—highlighting the inherent unreliability of a single human evaluation.
Disagreement Analysis
To analyze the presence of inductive bias and the reliability of the Human-as-a-Judge
paradigm here, we calculate the disagreement rate between individual evaluators (shown in Figure 4). The
results indicate that the disagreement rates between pairs of evaluators range from around 10% to 30%.
Due to the complexity of a complete AI development task, which typically involves multiple steps with
varying outcomes at each step, humans can easily make errors when critical information is missed, such as
environment feedback indicating small but severe coding errors or bugs. Additionally, some disagreements are

> Chunk 148 (page 29): H
Human Evaluation Procedure
We recruited three AI experts from the authors to perform human evaluation on the output of agentic code
generation systems. There we present the evaluation details.
First round
For the first round of evaluations, our three evaluators reported spending 16.5, 19.5, and 22.0
hours, respectively. To capture the bias that a human evaluator will have, the instructions given to our
experts were minimal, with them only receiving a scorecard to complete for each agentic system and each task.
Results that all evaluators agree on are considered trustworthy. The assumption here is that it is unlikely
that all three evaluators make a mistake or have an effective bias in the same judgment. The self-reported
post-hoc evaluation criteria are shown in Figure 12.
Second round
In the second round, the evaluators present and discuss their reasons for disagreeing with
judges. In doing so, human errors are likely corrected by their peers. Discussion among evaluators also helps

> Chunk 149 (page 29): that all three evaluators make a mistake or have an effective bias in the same judgment. The self-reported
post-hoc evaluation criteria are shown in Figure 12.
Second round
In the second round, the evaluators present and discuss their reasons for disagreeing with
judges. In doing so, human errors are likely corrected by their peers. Discussion among evaluators also helps
reduce human bias by examining each other’s thought processes thoroughly. Furthermore, the consensed
results are considered trustworthy given the assumption that it is unlikely that all three evaluators are
convinced by the same mistake or the same cognitive bias. The three evaluators took 9.5 hours together for
this second round of evaluation.
30


---

### Q15: In the diagram comparing LLM-as-a-Judge, Agent-as-a-Judge, and Human-as-a-Judge, what key drawback is highlighted for Human-as-a-Judge?

**Answer:** The key drawback highlighted for Human-as-a-Judge is that it requires heavy manual effort and is time-consuming.

**Supporting context:**
*   **[Chunk 10 | page 1]:** "agents or evaluate them took too much time. As a developer, this would be a bottleneck due to the heavy manual effort."
*   **[Chunk 14 | page 1]:** "We evaluate their performance using human judges (a painstaking process)..."

**Retrieved chunks:**

> Chunk 62 (page 10): A key power of the Agent-as-a-Judge,
though not fully exploited here but nonetheless clear, is that it provides intermediate feedback that is essential
for effective and efficient optimization (Zhuge et al., 2024; Pan et al., 2024). For example, Agarwal et al. (2019)
proposes to solve the sparse reward problem in reinforcement learning, by learning auxiliary reward functions
that provide intermediate feedback. Perhaps the greatest strength of the Agent-as-a-Judge framework is that
an agentic system can use it to identify and fix issues in its solutions to complex, multistage problems on the
fly—something older, delayed-feedback methods did not permit. By introducing Agent-as-a-Judge, we create
the opportunity to build a process-supervised reward model (PRM) for improving agentic systems (Lightman
et al., 2023).
3Additionally, we were pleased to find that a recent industry blog (https://www.cognition.ai/blog/evaluating-coding-ag

> Chunk 61 (page 10): conversational tasks. Unlike Agent-as-a-Judge, they employ a trivial agentic system and apply it only to
evaluate LLMs under traditional evaluation setups. In contrast, (Lu et al., 2024b) uses a single LLM-based
evaluator but, unlike LLM-as-a-Judge, applies this to multimodal tasks rather than just for evaluating LLMs.
Less relevant are frameworks like those by Chen et al. (2024a); Arora et al. (2024); M¨undler et al. (2024),
where intermediate signals are used during coding development.
6
Discussion and Conclusion
Outlook 1: Intermediate Feedback for Agentic Self-Improvement
A key power of the Agent-as-a-Judge,
though not fully exploited here but nonetheless clear, is that it provides intermediate feedback that is essential
for effective and efficient optimization (Zhuge et al., 2024; Pan et al., 2024). For example, Agarwal et al. (2019)
proposes to solve the sparse reward problem in reinforcement learning, by learning auxiliary reward functions

> Chunk 10 (page 1): agents or evaluate them took too much time. As a developer,
this would be a bottleneck due to the heavy manual effort.
Figure 1 We introduce the Agent-as-a-Judge framework wherein agentic systems are used to evaluate agentic systems.
We compare this to LLM-as-a-Judge, which uses LLMs to evaluate LLMs and for which Agent-as-a-Judge is a natural
evolution, and Human-as-a-Judge, where skilled human labourers manually evaluate an agentic system.
a key extension to the world of agentic systems (see Figure 1). It not only retains the cost-effectiveness of
LLM-as-a-Judge but is also equipped with agentic features, allowing it to provide rich intermediate feedback
throughout the entire process, as it acts as an agentic system. We apply the Agent-as-a-Judge systems to the
problem of evaluating code generating systems—one of the areas where agentic systems have looked the most
promising recently.

> Chunk 52 (page 9): 4.2
Judging Agent-as-a-Judge and LLM-as-a-Judge
Judge Shift
Judge Shift measures deviation from the Human-as-a-Judge consensus results, with lower values
indicating a closer alignment. As shown in table 3, Agent-as-a-Judge consistently outperforms LLM-as-a-Judge
across tasks, particularly those with task dependencies. For example, in Requirement (I), Agent-as-a-Judge
shows a Judge Shift as low as 0.27%, while LLM-as-a-Judge reaches 31.24% for OpenHands. This underscores
Agent-as-a-Judge’s stability and suitability for meeting task requirements. Furthermore, in the gray-box
setting, both Agent-as-a-Judge and LLM-as-a-Judge show even better results than their performance in the
black-box setting.
Figure 7 PR Curves comparing judge Methods.
Alignment Rate
The Alignment Rate reflects how
closely the AI Judges’ evaluations align with human
consensus across all 365 requirements. It is defined
as the percentage of requirement evaluations that
are the same as the Human-as-a-Judge consensus

> Chunk 106 (page 17): Description: In the third level of experiments, we compare three judgment systems: Agent-as-
a-Judge, LLM-as-a-Judge, and Human-as-a-Judge, all applied to the same DevAI tasks. Our
results show that Agent-as-a-Judge performs comparably to human evaluators and surpasses
LLM-as-a-Judge in more complex reasoning and evaluation tasks.
Future Directions
■Direction 1: Intermediate Feedback for Agentic Self-Improvement
Description: Agent-as-a-Judge offers intermediate feedback, crucial for reinforcement learning,
where rewards are sparse but vital for improvement. It also enables real-time issue identification
and resolution in complex, multi-stage tasks, overcoming the limitations of delayed feedback.
■Direction 2: Flywheel Effect Driven by Agent-as-a-Judge
Description: The iterative feedback cycle between the Agent-as-a-Judge and evaluated agents
(such as Developer Agents here) could create a flywheel effect, where mutual improvements lead

> Chunk 14 (page 1): 2024d). We evaluate their performance using human judges (a painstaking process), LLM-as-a-Judge (Zheng
et al., 2024), and our Agent-as-a-Judge framework.
Through human evaluation, we found that GPT-Pilot and OpenHands were each able to satisfy about 29%
of the task requirements in DevAI, but only one full task—showing that DevAI presents a good level of
challenge to current systems. When comparing our human judges with our automatic Agent-as-a-Judge
framework, we found that Agent-as-a-Judge aligns more closely with the consensus of our human judges (90%)
as compared to LLM-as-a-Judge (70%) in all cases tested. In addition, we find that it aligns more closely
with this ensemble than the individual human evaluators do, suggesting that—not only is it suitable as a
replacement for a human evaluator—but it could in fact be more useful than an average lone human evaluator.
2


---
