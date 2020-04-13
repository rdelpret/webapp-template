k8s_yaml('kubernetes/backend/deployment.yaml')
k8s_yaml('kubernetes/backend/service.yaml')

k8s_yaml('kubernetes/frontend/deployment.yaml')
k8s_yaml('kubernetes/frontend/service.yaml')

k8s_yaml('kubernetes/psql/deployment.yaml')
k8s_yaml('kubernetes/psql/service.yaml')

docker_build('backend', 'backend/.')
docker_build('frontend', 'frontend/.')

k8s_resource('backend', port_forwards=8000)
k8s_resource('frontend', port_forwards=8080)
