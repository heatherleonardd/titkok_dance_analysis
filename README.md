# TikTok Dance Analysis

## Description

Project to investigate correlations and similarites between different TikTok dance trends and their impact on engagement. Uses AlphaPose for pose detection, a custom built classifier to determine whether a video contains dancing or not and clustering techniques to investigate similarites in choreography.

## About

TikTok is a widely used social media platform, dance trends make up a significant part of the type of content available. 
This project aims to bridge the gap in research surrounding TikTok and provide solid foundational work in area of TikTok dance trends. 
TikTok provides a way for brands and content creators to promote their products/businesses, understanding what contributes to 'virality' is essential in reaching a wide range of customers. It is the hope this research can help achieve this.

Focusing on 5 dance trends:

1. Apple - Charlixcx, choreographed by Kelley Heyer
2. Savage - Megan Thee Stallion, choregraphed by Keara Wilson
3. Sayso - Doja Cat, choreographed by Haley Sharpe
4. Cannibal - Kesha, choreographed by Briana Hantsch
5. Supalonely - Benee, choreographed by Zoifishh

Additional dance added for further analysis:

6. No Pole - Don Toliver, choreographed by TikTok user ‘yungsir.03’, 

## Steps

### Step 1 - Data Collection

- Videos collected using TikAPi - downloading_data_step1.ipynb
- Change sound IDs based on what videos to collect

### Step 2 - Pose Detection 

- Used AlphaPose - https://github.com/MVIG-SJTU/AlphaPose
- Build using instructions from GitHub
- Files were modified to suit project's need, these can be found in the AlphaPose scripts folder.
  - Replace writer file in alphapose/utils
  - Add process_videos into the scripts folder
  - Add ‘256x192_res152_lr1e-3_1x-duc.yaml’ to directory ‘AlphaPose/configs/coco/resnet’
  - Add ‘fast_421_res152_256x192.pth’ to directory  ‘AlphaPose/model_files’ (this file is available to download: https://github.com/MVIG-SJTU/AlphaPose/blob/master/docs/MODEL_ZOO.md

### Step 3 - Data Normalisation 

- Took one person from each video
- Normalised coordinates using nose
- getting_all_data_step3_4_5.ipynb

### Step 4 - Dance Classifier

- Best one uses XGBoost
- Classifies dance based on AlphaPose coordinates
- dance_classifier.ipynb
- Run on data - getting_all_data_step3_4_5.ipynb

### Step 5 - Video metrics

- Number of people in each dance
- Likes, comments, followers, description using TikAPI
- getting_all_data_step3_4_5.ipynb

### Step 6 - Clustering

- Finding similarities between dance trends using coordinates
- Hierarchical clustering works best
- clustering_step6.ipynb
- Some code in this file may not work, clustering techniques not suitable for data

### Step 7 - Research Questions

- research_questions_step7
  - Use of graphs, regressions and ANOVA. 

**1. When videos have the same soundtrack, do videos with dance routines receive more engagement?**

- Generally, yes on average.

    **a) Does the answer change as the number of people following an account changes?**
    - No, the amount of followers usually increases likes for both dancing and non dancing videos.

2. Do videos with multiple dancers perform better or worse than those with one dancer?

- No, they perform similarly.





## Future Work

- Identify similar dance moves between each dance
- Create a 'formula' for TikTok dance trends
- Improve dance classifier
- Use alternative techniques for classifier - computer vision, AI
- Use different pose detection method
- Calculate number of people in each dance more accurately
- Get alternative clustering techniques working correctly


## Note

The csv files are too large to be uploaded here, but the necessary steps to obtain the data can be done by following the steps. 
