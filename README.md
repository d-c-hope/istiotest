# Istio test
3 images will be used in the test
WebApp1 communicates with WebApp2 and is available outside the cluster
WebApp3 tries to communicate with WebApp2 but is now allowed by Istio rules

Each web app runs in a namespace like WebApp1NS and has an associated service account in the cluster


## Preparing the test images that will be used in the mini cluster

Do this if you want to build with minikube docker so that minikube can use local images
eval $(/usr/local/minikube docker-env)

 * docker build -t username/image_name:tag_name -f Docker/Dockerfile . 
 * docker run --publish 8001:8001 --detach --name mysanicapp <image>
 * docker run --publish 8002:8001 --detach --name mysanicapp2 <image>

docker tag IMAGE_ID docker.pkg.github.com/d-c-hope/repository-name/IMAGE_NAME:VERSION
$ docker build -t docker.pkg.github.com/OWNER/REPOSITORY/IMAGE_NAME:VERSION PATH


docker tag f60ccea1e618 docker.pkg.github.com/d-c-hope/basicimages/basicpywebapp:0.01
docker tag 5238a56ffe68 basicpywebapp:0.01
docker tag 4d32cfb42ed1 docker.pkg.github.com/d-c-hope/basicimages/basicpywebapp2:0.01
docker tag 4d32cfb42ed1 basicpywebapp2:0.01

/usr/local/kubectl apply -f ./TestApp1/K8s/TestWebAppDeployment.yaml
/usr/local/kubectl describe deployment webapp1-deployment
/usr/local/kubectl apply -f ./TestApp1/K8s/TestWebAppService.yaml
/usr/local/kubectl describe service webapp1-service
/usr/local/minikube service webapp1-service

/usr/local/minikube ip

/usr/local/kubectl apply -f ./K8s/TestWebAppDeployment.yaml --namespace=app1ns
/usr/local/kubectl apply -f ./K8s/TestWebAppService.yaml --namespace=app1ns
/usr/local/minikube service webapp1-service --namespace=app1ns

/usr/local/kubectl apply -f ./K8s/TestWebApp2Deployment.yaml --namespace=app2ns
/usr/local/kubectl apply -f ./K8s/TestWebApp2Service.yaml --namespace=app2ns 


istioctl install --set profile=demo
kubectl label namespace app1ns istio-injection=enabled
kubectl label namespace app2ns istio-injection=enabled

/usr/local/kubectl apply -f ./K8s/TestWebAppVirtualService2.yaml --namespace=app2ns
Note i am not clear on what namespace should be used here, rule worked with either app1ns or app2ns

Do this to see the ingress gateway:
kubectl get svc istio-ingressgateway -n istio-system --show-labels