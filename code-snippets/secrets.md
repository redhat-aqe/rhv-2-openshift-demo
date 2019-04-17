# Application secrets

OpenShift has built-in Secret object for storing passwords/secret files.

Using oc command:
```
 oc create secret generic my_secret_file \                             
    --from-file="$SECRET_REPO/msg-my_secret_file.crt"

oc create secret generic secret_password --from-literal=password=$passwd
```

Using Ansible:
```yaml
- name: Create secret file
  no_log: True
  openshift_raw:
    api_key: "{{ ocp_token }}"
    host: "{{ ocp_host }}"
    state: present
    definition:
      apiVersion: v1
      kind: Secret
      metadata:
        name: "{{ my_secret_file }}"
        namespace: "{{ ocp_namespace }}"
      type: Opaque
      data:
        keytab: "{{ lookup('file', my_secret_file.cert) }}"


- name: Create secret password
  no_log: True
  openshift_raw:
    api_key: "{{ ocp_token }}"
    host: "{{ ocp_host }}"
    state: present
    definition:
      apiVersion: v1
      kind: Secret
      metadata:
        name: "secret_password"
        namespace: "{{ ocp_namespace }}"
      type: Opaque
      data:
        password: "{{ my_password }}" # value is stored in Ansible vault

```

The secret file or password can be injected to application as ENV variable or as a volume.
```yaml
  - apiVersion: v1
    kind: DeploymentConfig
    metadata:
      name: my-app
      labels:
        app: my-app
    spec:
      template:
        spec:
          volumes:
            - name: secret-file
              secret:
                secretName: secret-file
          containers:
            - env:
              - name: SECRET_PASSWD
                valueFrom:
                  secretKeyRef:
                    name: secret_password
                    key: password
              name: my-app
              volumeMounts:
                - name: secret-file
                  mountPath: /etc/my-app/secrets
```