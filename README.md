# DevSecOps Lab

Laboratorio práctico y progresivo para desarrollar competencias profesionales en **DevOps, DevSecOps y Ciberseguridad**, mediante la construcción, automatización, seguridad y despliegue de una API REST de gestión de tareas.

El proyecto está diseñado como un laboratorio de aprendizaje a largo plazo y evolucionará progresivamente desde una aplicación local hasta un entorno DevSecOps completo.

---

## 🎯 Objetivo

Construir un proyecto real que permita aprender y aplicar de forma práctica:

- Administración de sistemas Linux
- Bash y automatización
- Redes y protocolos
- Git y GitHub
- Python
- Desarrollo de APIs
- Testing
- Docker
- Docker Compose
- CI/CD
- SAST
- SCA
- Secret Scanning
- Container Security
- DAST
- IaC Security
- SBOM
- Supply Chain Security
- Gestión de vulnerabilidades
- Kubernetes Security
- Cloud Security
- Monitoring
- Logging
- DevSecOps

El objetivo no es únicamente aprender a utilizar herramientas, sino comprender:

- Qué problema resuelve cada herramienta.
- Dónde se integra.
- Qué riesgos ayuda a reducir.
- Qué limitaciones tiene.
- Qué alternativas existen.
- Cómo automatizarla.
- Cómo integrarla dentro de un pipeline CI/CD.
- Cómo interpretar sus resultados.
- Cómo tomar decisiones técnicas.

---

# 🏗️ Proyecto

El proyecto inicial será una **API REST de gestión de tareas**.

La aplicación comenzará siendo sencilla y posteriormente será utilizada como base para introducir progresivamente diferentes tecnologías y controles de seguridad.

Arquitectura inicial:

```text
                    Cliente
                       │
                       │ HTTP
                       ▼
                ┌──────────────┐
                │   Task API   │
                │    Python    │
                └──────┬───────┘
                       │
                       ▼
                    SQLite
```

La aplicación podrá evolucionar posteriormente hacia una arquitectura más completa:

```text
                         Usuario
                            │
                            ▼
                     Reverse Proxy
                            │
                            ▼
                       Task API
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
               Database           Logging
                                      │
                                      ▼
                                Monitoring
```

Y posteriormente:

```text
Developer
    │
    ▼
GitHub
    │
    ▼
CI/CD Pipeline
    │
    ├── Tests
    ├── SAST
    ├── SCA
    ├── Secret Scanning
    ├── Container Security
    ├── SBOM
    └── Security Gates
    │
    ▼
Container Registry
    │
    ▼
Deployment
    │
    ▼
Kubernetes / Cloud
```

---

# 💻 Entornos de desarrollo

El laboratorio está diseñado para funcionar en diferentes sistemas operativos.

## Entornos principales

- Kali Linux
- Windows 11 Pro

También se buscará mantener compatibilidad con otros sistemas cuando sea técnicamente razonable.

### Kali Linux

Será nuestro entorno principal para aprender:

- Linux
- Bash
- administración de sistemas
- redes
- herramientas de seguridad
- análisis
- automatización
- Docker
- DevSecOps

### Windows 11 Pro

Será utilizado como segundo entorno de desarrollo y laboratorio.

Permitirá trabajar con:

- Git
- Python
- Docker
- Docker Compose
- VS Code
- herramientas de desarrollo
- herramientas de DevOps y DevSecOps compatibles

El objetivo es que el proyecto sea lo más independiente posible del sistema operativo.

Las diferencias específicas entre Linux y Windows serán documentadas cuando sea necesario.

---

# 📁 Estructura del repositorio

La estructura inicial será:

```text
devsecops-lab/
│
├── app/
│   └── Código de la aplicación
│
├── tests/
│   └── Pruebas automatizadas
│
├── docker/
│   └── Configuración relacionada con Docker
│
├── docs/
│   └── Documentación técnica
│
├── .gitignore
└── README.md
```

La estructura evolucionará durante el desarrollo del laboratorio.

Posteriormente podremos incorporar directorios como:

```text
.github/
├── workflows/
└── dependabot.yml

iac/
├── terraform/
└── ansible/

k8s/
├── deployments/
├── services/
├── ingress/
└── policies/

security/
├── sast/
├── sca/
├── dast/
└── policies/

scripts/
└── automation/
```

Estas carpetas solamente serán incorporadas cuando tengan un propósito real dentro del proyecto.

---

# 🧪 Metodología del laboratorio

Cada etapa del laboratorio seguirá un proceso progresivo:

```text
Concepto
   ↓
Arquitectura
   ↓
Instalación / Configuración
   ↓
Ejercicio práctico
   ↓
Vulnerabilidad deliberada
   ↓
Detección
   ↓
Análisis
   ↓
Explotación controlada
   ↓
Corrección
   ↓
Automatización
   ↓
Buenas prácticas
```

Las vulnerabilidades serán introducidas únicamente dentro del entorno controlado del laboratorio y con fines educativos.

---

# 🔐 Seguridad

La seguridad será incorporada progresivamente dentro del ciclo de desarrollo.

El objetivo será evolucionar desde:

```text
Código
```

hacia:

```text
Código
   ↓
Testing
   ↓
SAST
   ↓
SCA
   ↓
Secret Scanning
   ↓
Container Security
   ↓
DAST
   ↓
IaC Security
   ↓
Security Gates
   ↓
Deployment seguro
```

Se estudiarán conceptos como:

- Secure SDLC
- Shift Left Security
- Defense in Depth
- Least Privilege
- Vulnerability Management
- Security Gates
- Supply Chain Security
- Software Composition Analysis
- Software Bill of Materials
- Gestión de secretos
- Seguridad de contenedores
- Seguridad de infraestructura
- Seguridad de Kubernetes
- Cloud Security

---

# 🐛 Vulnerabilidades deliberadas

Durante el laboratorio se introducirán vulnerabilidades de manera controlada.

El objetivo será aprender el ciclo:

```text
Crear
  ↓
Detectar
  ↓
Analizar
  ↓
Explotar de forma controlada
  ↓
Corregir
  ↓
Probar
  ↓
Automatizar la prevención
```

Algunos ejemplos que podremos estudiar posteriormente:

- SQL Injection
- Cross-Site Scripting
- Broken Access Control
- Improper Input Validation
- Insecure Authentication
- Information Disclosure
- Insecure Dependencies
- Hardcoded Secrets
- Vulnerable Container Images
- Misconfigured Docker Containers
- Insecure Infrastructure as Code
- Kubernetes Security Misconfigurations

Las pruebas de seguridad se realizarán exclusivamente dentro de nuestro entorno de laboratorio.

---

# 🛡️ DevSecOps

El objetivo final será integrar seguridad dentro del ciclo de desarrollo y operación.

Conceptualmente:

```text
                    DEV
                     │
                     ▼
                   CODE
                     │
                     ▼
                   BUILD
                     │
          ┌──────────┼──────────┐
          │          │          │
         SAST       SCA       Secrets
          │          │          │
          └──────────┼──────────┘
                     ▼
                 CONTAINER
                     │
                     ▼
            Container Security
                     │
                     ▼
                   DAST
                     │
                     ▼
                DEPLOYMENT
                     │
                     ▼
              MONITORING
                     │
                     ▼
                 FEEDBACK
                     │
                     └──────────► Development
```

---

# 🚀 Ruta de aprendizaje

El laboratorio seguirá aproximadamente esta progresión:

## Etapa 0 — Preparación del laboratorio

- Diseño del repositorio
- Estructura del proyecto
- Git
- Git workflow
- Documentación
- `.gitignore`
- Buenas prácticas iniciales

## Etapa 1 — Fundamentos Linux

- Sistema de archivos
- permisos
- usuarios
- grupos
- procesos
- servicios
- systemd
- logs
- Bash
- variables
- pipes
- redirecciones
- scripting

## Etapa 2 — Redes

- TCP/IP
- IPv4
- puertos
- DNS
- HTTP
- HTTPS
- SSH
- sockets
- firewalls
- troubleshooting de red

## Etapa 3 — Git y GitHub

- repositorios
- commits
- branches
- merge
- conflictos
- Pull Requests
- tags
- releases
- GitHub
- Git workflow
- code review

## Etapa 4 — Python

- fundamentos
- estructuras de datos
- funciones
- módulos
- excepciones
- entornos virtuales
- dependencias
- APIs
- testing
- automatización

## Etapa 5 — API REST

Construcción de nuestra API de tareas.

Conceptos:

- HTTP
- REST
- endpoints
- métodos HTTP
- status codes
- JSON
- validación
- errores
- persistencia

## Etapa 6 — Docker

- imágenes
- contenedores
- Dockerfile
- layers
- registries
- redes
- volúmenes
- logs
- Docker Compose
- buenas prácticas
- seguridad de contenedores

## Etapa 7 — DevOps

- CI/CD
- GitHub Actions
- pipelines
- automated testing
- artifacts
- environments
- deployments
- rollback
- automatización

## Etapa 8 — DevSecOps

- Secure SDLC
- Shift Left
- SAST
- SCA
- Secret Scanning
- Dependency Security
- Container Security
- DAST
- Security Gates
- Vulnerability Management
- SBOM
- Supply Chain Security

## Etapa 9 — Infrastructure as Code

- Terraform
- Ansible
- IaC
- configuración segura
- validación
- scanning
- GitOps

## Etapa 10 — Kubernetes

- arquitectura
- Pods
- Deployments
- Services
- Ingress
- Namespaces
- ConfigMaps
- Secrets
- RBAC
- Network Policies
- Helm
- Workload Security
- Runtime Security

## Etapa 11 — Cloud Security

Se seleccionará inicialmente un proveedor cloud principal para estudiarlo con profundidad.

Conceptos:

- IAM
- redes
- almacenamiento
- compute
- logging
- monitoring
- secrets
- workload security
- cloud posture
- mínimo privilegio

Posteriormente se trasladarán los conocimientos a otros proveedores.

## Etapa 12 — Observabilidad

- Logging
- Metrics
- Monitoring
- Alerting
- Troubleshooting
- SIEM
- Detection
- Correlation
- Incident Response

## Etapa 13 — DevSecOps completo

Integración de todos los componentes:

```text
Developer
    │
    ▼
GitHub
    │
    ▼
Pull Request
    │
    ├── Code Review
    ├── Tests
    ├── SAST
    ├── SCA
    ├── Secret Scanning
    └── IaC Security
    │
    ▼
Build
    │
    ▼
Container Image
    │
    ├── Image Scanning
    ├── SBOM
    └── Supply Chain Security
    │
    ▼
Registry
    │
    ▼
Deployment
    │
    ▼
Kubernetes / Cloud
    │
    ├── Monitoring
    ├── Logging
    └── Security Monitoring
```

---

# 🧠 Filosofía de aprendizaje

Este laboratorio no busca convertirnos en operadores de herramientas.

El objetivo es comprender:

```text
Problema
   ↓
Riesgo
   ↓
Solución
   ↓
Herramienta
   ↓
Automatización
   ↓
Validación
```

Cada herramienta deberá responder a una pregunta:

> ¿Qué problema profesional resuelve esta herramienta?

Antes de utilizar una herramienta se estudiará:

- Qué problema resuelve.
- Cómo funciona conceptualmente.
- Dónde se integra.
- Qué información necesita.
- Qué resultados produce.
- Qué limitaciones tiene.
- Qué alternativas existen.
- Cómo automatizarla.
- Cómo interpretar sus resultados.

---

# 📚 Documentación

Las decisiones técnicas importantes serán documentadas en `docs/`.

La documentación podrá incluir:

```text
docs/
├── architecture/
├── linux/
├── networking/
├── git/
├── python/
├── docker/
├── cicd/
├── security/
├── kubernetes/
├── cloud/
└── troubleshooting/
```

La estructura se irá creando a medida que el proyecto avance.

---

# 🎓 Objetivo profesional

El objetivo final del laboratorio es desarrollar competencias aplicables a posiciones como:

- DevSecOps Engineer
- DevOps Engineer con enfoque Security
- Security Engineer
- Application Security Engineer
- Cloud Security Engineer
- Container Security Engineer
- Kubernetes Security Engineer

El laboratorio busca servir como evidencia práctica de conocimientos adquiridos durante el proceso de formación en ciberseguridad.

---

# 📈 Evolución del proyecto

El proyecto evolucionará progresivamente:

```text
API
 │
 ▼
API + Tests
 │
 ▼
Git
 │
 ▼
Docker
 │
 ▼
Docker Compose
 │
 ▼
CI/CD
 │
 ▼
Secure CI/CD
 │
 ▼
Security Scanning
 │
 ▼
Infrastructure as Code
 │
 ▼
Kubernetes
 │
 ▼
Cloud
 │
 ▼
Monitoring
 │
 ▼
DevSecOps Platform
```

La complejidad se incrementará únicamente cuando los fundamentos anteriores hayan sido comprendidos.

---

# ⚠️ Uso educativo

Este repositorio forma parte de un laboratorio educativo.

Las vulnerabilidades, configuraciones inseguras y técnicas de explotación utilizadas durante el aprendizaje se ejecutarán exclusivamente en entornos controlados y autorizados.

No se utilizarán estas prácticas contra sistemas, aplicaciones, redes o infraestructuras sin autorización.

---

# 📌 Estado actual

**Etapa:** 0.2 — Git Workflow profesional

**Estado:**

- [x] Crear estructura inicial
- [x] Crear `.gitignore`
- [x] Diseñar proyecto
- [x] Definir entornos de desarrollo
- [x] Inicializar Git
- [x] Configurar rama `main`
- [x] Configurar identidad Git
- [x] Primer commit
- [x] Conectar con GitHub
- [x] Crear rama de trabajo
- [ ] Comenzar desarrollo de la API

---

## 🚧 Próximo objetivo

Completar la configuración inicial del repositorio y realizar el primer commit funcional.

Posteriormente comenzaremos con los fundamentos necesarios para desarrollar nuestra API de forma profesional y segura.
