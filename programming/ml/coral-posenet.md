----
# Google Coral's PoseNet

Original Repository [GoogleCoral](https://github.com/google-coral/project-posenet) .
---

- Pose estimation refers to computer vision techniques that detect human figures in images and videos. The sameple code is optimized for usage upon google's coral edge tpu alongside camera input/image or video files.
- This library can be used in order to process images/video files in applications that concern human movement/interaction/poses/posture/action analysis amongst others.
- The library provided by google is intended to be used among Edge TPU systems that can be run on-prem; - thus, making use of machine-learning models within "supposedly private and annonymous" systems.

## Demonstration of core functions: 

  1. an input RGB image is fed through a convolutional neural network(MobileNet V1) which is processed by a specialized head which produces a set of heatmaps(one for each kind of key point) and some offset maps. 
  2. A special multi-pose decodiong algorithm is used to decode poses, pose confidence scors, keypoints, positions, and keypoint confidence scores. 
