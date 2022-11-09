from google.cloud import container_v1beta1
# Magic numbers for the number of nodes
SHUTDOWN_N_NODE = 0
INITIAL_N_NODE = 2

project_id="dgcp-sandbox-mde-sf"
zone="europe-west1-d"
cluster_id="mc-cluster"
node_pool_id="default-pool"


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
    # Initialize request argument(s)
    if _get_node_pool_size(project_id,zone,cluster_id,node_pool_id) > 0 :
        node_count = SHUTDOWN_N_NODE
    else:
        node_count = INITIAL_N_NODE
    
    request = container_v1beta1.SetNodePoolSizeRequest(
        project_id=project_id,
        zone=zone,
        cluster_id=cluster_id,
        node_pool_id=node_pool_id,
        node_count=node_count,)

    # Make the request
    response = client.set_node_pool_size(request=request)
    # Handle the response