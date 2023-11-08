<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/outline/website/07fe265b1695432797200a21cc54df1c4f572808/public/images/logo.svg" width="100" />
<br>outline-infra
</h1>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Pulumi-8A3391.svg?style&logo=Pulumi&logoColor=white" alt="Pulumi" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
</p>
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

This project leverages the Pulumi framework to automate the provisioning of various resources on DigitalOcean. It provides functionalities like setting up a VPC, deploying a Redis cluster, creating a Cloudflare DNS record, configuring DigitalOcean Spaces, and creating a DigitalOcean app with a Postgres database and Redis cluster. By automating the process of resource provisioning, this project increases efficiency and reduces the time required to set up a production-ready application environment on DigitalOcean.

---

## ⚙️ Features

Creates:
- DigitalOcean Project
- VPC
- Redis Instance
- DigitalOcean Spaces (S3) Bucket
- App Deployment with integrated PostgreSQL Database
- Cloudflare DNS Record

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                                      | Summary                                                                                                                                                                                                                                                                                               |
| ---                                                                                       | ---                                                                                                                                                                                                                                                                                                   |
| [vpc.py](https://github.com/cdiaz2799/outline-infra/blob/main/vpc.py)                     | The code sets up a VPC (Virtual Private Cloud) in a specified region using the Pulumi framework, specifically for the DigitalOcean provider. The VPC is named "outline-vpc" and an output is created to export the VPC's name. |
| [outline_redis.py](https://github.com/cdiaz2799/outline-infra/blob/main/outline_redis.py) | This code sets up a Redis cluster on DigitalOcean using Pulumi. It allows the user to define the size and configuration of the Redis instance.                                                                                                                                                        |
| [bucket.py](https://github.com/cdiaz2799/outline-infra/blob/main/bucket.py)               | This code sets up a Bucket on DigitalOcean Spaces called'outline-s3-bucket', configures CORS rules, attaches it to a project, and exports the bucket name.                                                                                                                                            |
| [dns.py](https://github.com/cdiaz2799/outline-infra/blob/main/dns.py)                     | This code sets up a Cloudflare DNS record for a specified URL. It creates a CNAME record with the desired URL as the value and includes additional configurations for comments and proxying. The code also exports the URL.                                           |
| [app.py](https://github.com/cdiaz2799/outline-infra/blob/main/app.py)                     | The code sets up the DigitalOcean app with a Postgres database and attaches the Redis cluster. It also configures various environment variables and outputs the app's default ingress URL.                                                                                                          |
| [__main__.py](https://github.com/cdiaz2799/outline-infra/blob/main/__main__.py)           | This code integrates various functionalities including application management, bucket storage, dns, database caching, project handling, and virtual private network (vpc).                                                                                                                            |
| [project.py](https://github.com/cdiaz2799/outline-infra/blob/main/project.py)             | This code sets up a DigitalOcean project in the production environment called "outline" for a web application.                                                                                             |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

> - `ℹ️ Configure DigitalOcean Credentials`
> - `ℹ️ Configure Cloudflare API token`
> - `ℹ️ Configure DigitalOcean Spaces API Credentials`
> - `ℹ️ Create Slack app`


### 📦 Installation

1. Clone the outline-infra repository:
```sh
git clone https://github.com/cdiaz2799/outline-infra
```

2. Change to the project directory:
```sh
cd outline-infra
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using Pulumi

```sh
pulumi up
```

### 🧪 Previewing Changes
```sh
pulumi preview
```