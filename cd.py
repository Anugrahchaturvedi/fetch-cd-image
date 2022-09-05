import subprocess as sp
import requests
import sys
DASHBOARD=sp.getoutput("kubectl get po -ndevtroncd  -l component=dashboard  -o jsonpath='{.items[0].spec.containers[*].image}'")
ORCHESTRATOR=sp.getoutput("kubectl get po -ndevtroncd -l component=devtron -o jsonpath='{.items[0].spec.containers[*].image}'")
#MIGRATOR=sp.getoutput("kubectl get po -ndevtroncd -l component=postgresql-migrate-devtron -o jsonpath='{.items[0].spec.containers[*].image}'")
IMAGE_SCANNER=sp.getoutput("kubectl get po -ndevtroncd -l component=image-scanner -o jsonpath='{.items[0].spec.containers[*].image}'")
NOTIFIER=sp.getoutput("kubectl get pod -l component=notifier -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
KUBEWATCH=sp.getoutput("kubectl get pod -l app=kubewatch -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
KUBELINK=sp.getoutput("kubectl get pod -l app=kubelink -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
GIT_SENSOR=sp.getoutput("kubectl get po -l app=git-sensor  -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
LENS=sp.getoutput("kubectl get pod -l component=lens -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
CLAIR=sp.getoutput("kubectl get po -l component=clair -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
ROLLOUT=sp.getoutput("kubectl get po -l app.kubernetes.io/name=argo-rollouts -ndevtroncd -o jsonpath='{.items[0].spec.containers[*].image}'")
NATS_SERVER=sp.getoutput("kubectl get po devtron-nats-0    -ndevtroncd -o jsonpath='{.spec.containers[*].image}'")
# NATS_POD=sp.getoutput("kubectl get po -ndevtroncd -l app=nats-streaming -o name |awk 'FNR == 2' |awk -F \"/\" '{print $2}'")
# NATS_STREAM=sp.getoutput("kubectl get po %s   -ndevtroncd -o jsonpath='{.spec.containers[*].image}'"%NATS_POD)
print(DASHBOARD)
print(ORCHESTRATOR)
print(IMAGE_SCANNER)
print(NOTIFIER)
print(KUBEWATCH)
print(KUBELINK)
print(GIT_SENSOR)
print(LENS)
print(CLAIR)
print(ROLLOUT)
print(NATS_SERVER)

