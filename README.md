# Cloud Function Deploy Tutorial

Google Cloud functions provide serverless functions executed on Google Cloud Platform.
They can be triggered via HTTP or periodically using cron-expressions.
For continous deployment (CD), GitHub workflows (GitHub Actions) can be used to push code to GCP.
The following tutorial explains how to setup a minimal example function on GCP and deploy new iterations using GitHub Actions.