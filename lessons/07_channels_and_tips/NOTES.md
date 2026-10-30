# Lesson 07 — channels and tips

## Part 1 - one channel vs 8 channels

**Goal:** how signle channel and multichannel pipetting workds in PyLabRobot,

**what I learned**:  
1. setting set_tip_tracking(True) and set_volume_tracking(True) help PyLabRobot track which tips are used and how much volume is in well/container.
2. there is no need to specify if you are using single channel or multichannel piptte. PyLabRobot uses one channel for each entry in the list: a list of 1 uses 1 channel, a list of 8 uses 8 channels
3. If the list given to the function doesn't match (number of wells and the number of volumes for them) PyLabRobot has guardrail to catch it, but it is still important to think about the workflow and step, since ome other mistakes (like possibility of cross-contamination) is not automatically checked
4. using multichannel (if possible in your workflow) will reduce the travel time for the arm and accelerate the process.
5. discard_tips() sends tips to the trash while return_tips() puts them back where they were picked up from.

## Part 2 - to discard or not to discard

**Goal:** importance of discarding or not discarding the tips. how to write a robust code that could adapt easy with changing sample size

**what I learned**: 
1. Based on the workflow, one should decide if the tips should be discarded between sample manipulation to avoide cross-contamination
2. there are two tiptracker. PyLabRobot always tracks if there is tip on the pipette, but whether there are tips in the rack after manipulation should be enabled using set_tip_tracking(True) opetion.
3. it is important to write your code in a way that would be easy to change setting. instead of remembering which lines I should change if I switch from x number of samples to y number of samples