# Disengagement Detection in Mice using IBL BiasedChoiceWorld Data
## Boredom Score Description:
The boredom score is a continuous measure representing the disengagement level of a mouse during a behavioral session. We define it as a weighted combination of behavioral proxies indicative of cognitive fatigue, distraction, or lack of motivation:
## boredom_score_definition
```
boredom_score=w 1⋅reaction_time_smoothed+w 2 ⋅(1−rolling_accuracy)+w 3⋅trial_duration+w 4⋅skip_rate_smoothed
```
Where:
- reaction_time_smoothed: Moving average of reaction times — longer times suggest fatigue/disengagement.
- rolling_accuracy: Recent accuracy (lower values signal poor attention or disengagement).
- trial_duration: Time between stimOn and feedback — longer trials may reflect hesitation.
- skip_rate_smoothed: Smoothed fraction of skipped trials — more skips suggest boredom.
<Br/>
Weights were empirically tuned using a *random forest model* to emphasize reaction time and accuracy, two primary behavioral indicators of engagement.

## Behavioral Proxies and Justification
Feature	Why it was chosen
- Reaction Time	Slower responses reflect hesitation or reduced task engagement.
- Rolling Accuracy	A drop in accuracy signals cognitive fatigue or loss of focus.
- Trial Duration	Longer trials hint at uncertainty or delay in decision-making.
- Skip Rate	Frequent skipping directly reflects disengagement with the task.
## Observed Patterns Across Sessions
Using 10 sessions from subject CSHL_001, we observed the following:

Boredom scores tend to rise mid-to-late session, corresponding with increased reaction times and a spike in trial skips.

Smoothed boredom trajectories vary session-to-session but show consistent intra-session increase, indicating a general trend of decreasing engagement.

Some sessions show periodic recovery, possibly due to external cues or task resets, showing short-term re-engagement.

🤖 Model Performance
We trained a Random Forest Regressor to predict the boredom score from trial-wise features.

A binary classifier (high vs. low boredom) was created by thresholding the score.

Final classification accuracy: 100% on held-out test data (split from combined sessions).

Important features: Reaction time and trial duration were top predictors; rolling_accuracy had lower importance in regression but helped in classification.

📁 Files Description
File Name	Description
demo_solution_10sessions_combined(CSHL_001).ipynb	Final model with boredom score computation, visualization, and regression/classification logic.
demo_solution_10sessions_combined(CSHL_001) (1).ipynb	Slightly earlier version, used for debugging and initial analysis.
