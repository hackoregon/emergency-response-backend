#! /bin/bash
# Tag, Push and Deploy only if it's not a pull request
# Comment
source ./bin/aws-env.sh

if [ "$TRAVIS_BRANCH" == "master" ]; then
    docker login --username "$DOCKER_USERNAME" --password "$DOCKER_PASSWORD"
    docker push "$DOCKER_REPO"/"$DOCKER_WEB_IMAGE":latest
    ecs-cli compose --project-name "$ECS_PROJECT" --file ecs-deploy.yml service up;
fi
