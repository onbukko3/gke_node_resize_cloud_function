"""Python GKE API is mainly used to get the current detailed node information in order to decide 
whether a node will be activated or shutted down. 
https://cloud.google.com/python/docs/reference/container/latest"""

from google.cloud import container_v1beta1
# Magic numbers for the number of nodes, the numbers should be adjusted by requirements
SHUTDOWN_N_NODE = 0
INITIAL_N_NODE = 2

# Replace here with your details
project_id=PROJECT_ID
zone=ZONE
cluster_id=CLUSTER_ID
node_pool_id=NODE_POOL_ID


def main(request):
    set_node_size(project_id,zone,cluster_id,node_pool_id)
    return "200"

def _get_node_pool_size(project_id,zone,cluster_id,node_pool_id):
    from google.cloud import container_v1beta1
    # Create a client
    client = container_v1beta1.ClusterManagerClient()

    # Initialize request argument(s)
    request = container_v1beta1.GetNodePoolRequest(
        project_id=project_id,
        zone=zone,
        cluster_id=cluster_id,
        node_pool_id=node_pool_id,
    )

    # Make the request
    response = client.get_node_pool(request=request)
    
    return response.initial_node_count

def set_node_size(project_id,zone,cluster_id,node_pool_id,node_count=None):
    global SHUTDOWN_N_NODE, INITIAL_N_NODE
    # Create a client
    client = container_v1beta1.ClusterManagerClient()

    # Check the state of the number of node size 
    if _get_node_pool_size(project_id,zone,cluster_id,node_pool_id) > 0 :
        node_count = SHUTDOWN_N_NODE
    else:
        node_count = INITIAL_N_NODE
    
    # Initialize request argument(s)
    request = container_v1beta1.SetNodePoolSizeRequest(
        project_id=project_id,
        zone=zone,
        cluster_id=cluster_id,
        node_pool_id=node_pool_id,
        node_count=node_count,)

    # Make the request
    response = client.set_node_pool_size(request=request)
    # Handle the response