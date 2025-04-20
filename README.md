🚗 Motion Prediction for Autonomous Vehicles
This repository contains the implementation of a data-driven motion prediction model for autonomous vehicles. Developed as part of our academic work at Technical University of Kaiserslautern, the project evaluates different motion prediction strategies and proposes a deep learning-based approach using a fully connected neural network trained on the inD dataset.

📄 About the Project
Predicting the motion of surrounding agents (cars, bikes, pedestrians) is a critical function for the safe operation of autonomous vehicles. In this project, we explore:

The limitations of traditional physics-based, maneuver-based, and interaction-aware models

A fully connected neural network built with TensorFlow Keras

The use of hyperparameter tuning to optimize the model

Performance evaluation using metrics like ADE, FDE, and AHE

📦 Dataset
We used the inD dataset, which consists of naturalistic road user trajectories recorded by drones at four intersections in Aachen, Germany. It provides:

Over 13,500 trajectories

Data from automobiles, bikes, and pedestrians

10 hours of recording with high positional accuracy

🧠 Model Overview
We implemented a fully connected neural network with:

Two hidden layers (Dense)

ReLU activation for hidden layers

SoftMax activation for output layer (3-class classification)

Optimized using Stochastic Gradient Descent (SGD)

Hyperparameter tuning with grid/random search


🔁 Workflow:
Data preprocessing from inD dataset

Model creation using TensorFlow Keras

Compilation with ReLU, SoftMax, and SGD

Training and Validation

Performance Evaluation

📊 Evaluation Metrics
Metric | Description | Result
ADE | Avg. Displacement Error | 1.668 m
FDE | Final Displacement Error | 1.806 m
AHE | Avg. Absolute Heading Error | 8.11°