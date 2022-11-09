# gke_node_resize_cloud_function

The solution is based using GCP Cloud Function to resize GKE node size. As an Cloud User, sometimes it happends to forget to shut down a cluster via resizing the number of node to zero. To prevent from that, it will be applicable to automate changing the number of node via combination with Cloud Function and Cloud Scheduler.

