# Docker Swarm Tutorial
Following the [official swarm tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)

## Create swarm
On host: 

    docker swarm init --advertise-addr <manager-ip>

SSH into each worker node and add them to the swarm with the ouput of the init command: 

    docker swarm join --token SWMTKN-1-658zprua3h5df9wyfceo27p144qop0g6l4gknud4sdnw3i3fvc-0ti1eq6lw9axrf13d9xukvsj6 192.168.0.104:2377

If there is an error like 'Timeout was reached' check to see if the ports are open (`nmap <ipaddress> -p 2377`). ufw will block traffic if not configured properly.

`docker node ls`: Show the status of each node


## Deploy a test to the cluster
Deploy a test service:

    docker service create --replicas 1 --name helloworld alpine ping docker.com

Then scale the service to have more replicas:
    
    docker service scale helloworld=<n>

`docker service inspect --pretty helloworld`: Show info about the service
`docker service ps helloworld`: Show status and where each replica is running
`docker service rm helloworld`: Remove the service


## Rolling update
Deploy a service:

    docker service create --replicas 3 --name redis --update-delay 10s redis:3.0.6

Execute the update:

    docker service update --image redis:3.0.7 redis

## Remove node services from node
Update a node so that all services are removed off of it and replicated elsewhere as needed.

    docker node update --availability drain <node id or host name>

