# Scheduled updates of image streams

To make sure base image is always updated and contains all security patches we can create image stream which is always synchronized with remote registry.

To create scheduled image stream use following command:

```
➜  oc import-image \
    --scheduled=true \
    --confirm=true \
    --from registry.access.redhat.com/rhel7:latest
    rhel7:latest 
    
imagestream.image.openshift.io/rhel7 imported

Name:			rhel7
Namespace:		araszka-playground
Created:		Less than a second ago
Labels:			<none>
Annotations:		openshift.io/image.dockerRepositoryCheck=2019-04-15T12:05:34Z
Docker Pull Spec:	docker-registry.default.svc:5000/araszka-playground/rhel7
Image Lookup:		local=false
Unique Images:		1
Tags:			1

latest
  updates automatically from registry registry.access.redhat.com/rhel7:latest

  * registry.access.redhat.com/rhel7@sha256:e3f12513a4b22a2d7c0e7c9207f52128113758d9d68c7d06b11a0ac7672966f7
      Less than a second ago

Image Name:	rhel7:latest
Docker Image:	registry.access.redhat.com/rhel7@sha256:e3f12513a4b22a2d7c0e7c9207f52128113758d9d68c7d06b11a0ac7672966f7
Name:		sha256:e3f12513a4b22a2d7c0e7c9207f52128113758d9d68c7d06b11a0ac7672966f7
Created:	Less than a second ago
Annotations:	image.openshift.io/dockerLayersOrder=ascending
Image Size:	75.84MB in 2 layers
Layers:		75.83MB	sha256:76608b6b9d54251299c5d3be69fdf53e05f97a3735bbcd5889c30ebb78608428
		1.266kB	sha256:3c81a5d20855a6cef8b997d709410e047e2839b5ad113f4c34d25e9fae9e3beb
Image Created:	6 days ago
Author:		Red Hat, Inc.
Arch:		amd64
Command:	/bin/bash
Working Dir:	<none>
User:		<none>
Exposes Ports:	<none>
Docker Labels:	architecture=x86_64
		authoritative-source-url=registry.access.redhat.com
		build-date=2019-04-08T13:38:26.374779
		com.redhat.build-host=cpt-0002.osbs.prod.upshift.rdu2.redhat.com
		com.redhat.component=rhel-server-container
		com.redhat.license_terms=https://www.redhat.com/licenses/eulas
		description=The Red Hat Enterprise Linux Base image is designed to be a fully supported foundation for your containerized applications. This base image provides your operations and application teams with the packages, language runtimes and tools necessary to run, maintain, and troubleshoot all of your applications. This image is maintained by Red Hat and updated regularly. It is designed and engineered to be the base layer for all of your containerized applications, middleware and utilities. When used as the source for all of your containers, only one copy will ever be downloaded and cached in your production environment. Use this image just like you would a regular Red Hat Enterprise Linux distribution. Tools like yum, gzip, and bash are provided by default. For further information on how this image was built look at the /root/anacanda-ks.cfg file.
		distribution-scope=public
		io.k8s.description=The Red Hat Enterprise Linux Base image is designed to be a fully supported foundation for your containerized applications. This base image provides your operations and application teams with the packages, language runtimes and tools necessary to run, maintain, and troubleshoot all of your applications. This image is maintained by Red Hat and updated regularly. It is designed and engineered to be the base layer for all of your containerized applications, middleware and utilities. When used as the source for all of your containers, only one copy will ever be downloaded and cached in your production environment. Use this image just like you would a regular Red Hat Enterprise Linux distribution. Tools like yum, gzip, and bash are provided by default. For further information on how this image was built look at the /root/anacanda-ks.cfg file.
		io.k8s.display-name=Red Hat Enterprise Linux 7
		io.openshift.tags=base rhel7
		name=rhel7
		release=202.1554729462
		summary=Provides the latest release of Red Hat Enterprise Linux 7 in a fully featured and supported base image.
		url=https://access.redhat.com/containers/#/registry.access.redhat.com/rhel7/images/7.6-202.1554729462
		vcs-ref=8614a40bd9d01571d521f5b87954947d1c8bbe33
		vcs-type=git
		vendor=Red Hat, Inc.
		version=7.6
Environment:	PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
		container=oci


➜ oc get is rhel7 -o yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  annotations:
    openshift.io/image.dockerRepositoryCheck: 2019-04-15T12:05:34Z
  creationTimestamp: 2019-04-15T12:05:34Z
  generation: 1
  name: rhel7
  namespace: araszka-playground
  resourceVersion: "55223044"
  selfLink: /apis/image.openshift.io/v1/namespaces/araszka-playground/imagestreams/rhel7
  uid: c5f28e85-5f76-11e9-8b0f-fa163e006653
spec:
  lookupPolicy:
    local: false
  tags:
  - annotations: null
    from:
      kind: DockerImage
      name: registry.access.redhat.com/rhel7:latest
    generation: 1
    importPolicy:
      scheduled: true
    name: latest
    referencePolicy:
      type: Source
status:
  dockerImageRepository: docker-registry.default.svc:5000/araszka-playground/rhel7
  tags:
  - items:
    - created: 2019-04-15T12:05:34Z
      dockerImageReference: registry.access.redhat.com/rhel7@sha256:e3f12513a4b22a2d7c0e7c9207f52128113758d9d68c7d06b11a0ac7672966f7
      generation: 1
      image: sha256:e3f12513a4b22a2d7c0e7c9207f52128113758d9d68c7d06b11a0ac7672966f7
    tag: latest

```

Your application which is build on top of base image can be also automatically rebuilt when BuildConfig uses imageChange triggers.

Here is an example of buildConfig which uses the trigger:

```yaml
 
 - apiVersion: v1
    kind: BuildConfig
    metadata:
      labels:
        app: my-app
      name: my-app
    spec:
      ...
      triggers:
        type: "imageChange" 
        imageChange: {}
        type: "imageChange" 
        imageChange:
        from:
            kind: "ImageStreamTag"
            name: "rhel7:latest"


```