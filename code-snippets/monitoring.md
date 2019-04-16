# Liveness & Readiness probe

Application in OpenShift can monitor itself using liveness probe. When the liveness probe detects an application is in broken state OpenShift automatically restart a pod with an application.

The readiness probe is usually used when application starts and it is not ready to get requests yet. The readiness probe blocks incoming traffic of requests until application is fully ready.
```yaml

  - apiVersion: v1
    kind: DeploymentConfig
    metadata:
      name: my-app
    spec:
      template:
        spec:
          containers:
            - name: my-app
              image: docker-registry.default.svc:5000/araszka-playground/my-app:latest
              readinessProbe:
                httpGet:
                  path: /ready
                  port: 8080
                initialDelaySeconds: 10
                timeoutSeconds: 1
              livenessProbe:
                httpGet:
                  path: /health
                  port: 8080
                initialDelaySeconds: 15
                periodSeconds: 3

```