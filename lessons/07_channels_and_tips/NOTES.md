# Lesson 07 — channels and tips

## Part 1 - one channel vs 8 channels

**Goal:** how signle channel and multichannel pipetting workds in PyLabRobot,

**what I learned**:  
1. setting set_tip_tracking(True) and set_volume_tracking(True) help PyLabRobot track which tips are used and how much volume is in well/container.
2. there is no need to specify if you are using single channel or multichannel piptte. PyLabRobot uses one channel for each entry in the list: a list of 1 uses 1 channel, a list of 8 uses 8 channels
3. If the list given to the function doesn't match (number of wells and the number of volumes for them) PyLabRobot has guardrail to catch it, but it is still important to think about the workflow and step, since ome other mistakes (like possibility of cross-contamination) is not automatically checked
4. using multichannel (if possible in your workflow) will reduce the travel time for the arm and accelerate the process.
5. discard_tips() sends tips to the trash while return_tips() puts them back where they were picked up from.
