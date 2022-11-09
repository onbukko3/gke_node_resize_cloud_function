#!/bin/bash

# User action initiative script to start a GKE node

# Get activated project id
PROJECT_ID = $(gcloud config get project)

echo "Initialize your GKE cluster to enable storing data into GCP"
read -p "Cluster ID: " CLUSTER_ID
read -p "Node Pool ID: " NODEPOOL_ID
read -p "Number of node size: " NUM_NODES

# Resize the number of node size by user's demand
gcloud container clusters resize CLUSTER_ID --node-pool NODEPOOL_ID \
    --num-nodes NUM_NODES


