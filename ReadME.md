# Flask AWS Monitor - Helm Chart

This repository contains the Helm chart configuration for deploying the Flask AWS Monitor application to a Kubernetes cluster. 

## Prerequisites
* Kubernetes cluster running and accessible (`kubectl get nodes`)
* Helm installed and configured

## Chart Structure & Configuration

This chart was initialized using the standard Helm scaffolding and customized for the Flask application. Unnecessary example files have been removed to keep the template clean.

### Core Resources
* **Deployment (`templates/deployment.yaml`):** Pulls the latest application image from Docker Hub and exposes it on port **5001**. Environment variables are mounted for AWS credentials.
* **Service (`templates/service.yaml`):** Configured as either `ClusterIP` or `LoadBalancer` depending on the environment, exposing port **5001**.
* **Ingress (`templates/ingress.yaml`):** (Optional) Configured with host/path routing for clusters utilizing an Ingress controller.

### Values Configuration (`values.yaml`)
The deployment is highly customizable via `values.yaml`. Key configurations include:
* Default Docker image and tag.
* Replica count for horizontal scalability.
* Resource requests and limits to ensure stable cluster performance.

**⚠️ Security Note for AWS Credentials:**
AWS keys are specified in a separate values file named `aws-values.yaml`. 
**Crucial:** Ensure `aws-values.yaml` is added to your `.gitignore` file to prevent committing sensitive credentials to version control.

## Deployment Instructions

1. **Verify Cluster Access:**
   Ensure your Kubernetes cluster is running and your context is correctly set.
   ```bash
   kubectl get nodes
