#!/bin/bash
# Setup your envrironment
source ./bin/aws-env.sh

#Stand up your cluster
ecs-cli up \
  --keypair "$AWS_KEY_PAIR"\
  --capability-iam \
  --size "$ECS_CLUSTER_SIZE" \
  --instance-type "$ECS_INSTANCE_TYPE"  \
  --port "$ECS_PORT" \
