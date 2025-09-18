# Importación de Issues para GitHub

Este directorio contiene los archivos necesarios para importar una estructura completa de issues al repositorio del Sistema de Gestión Empresarial.

## Archivos incluidos

- `github_issues.csv` - CSV con 246 issues organizadas (épicas, features, tasks)
- `import_issues.py` - Script de Python para importar las issues automáticamente
- `ISSUES_IMPORT_README.md` - Este archivo con instrucciones

## Estructura de Issues

El CSV contiene **246 issues** organizadas en tres niveles:

### 📋 Épicas (16 principales)
- Business Core (ERP tradicional)
- AI Engine (Motor de IA)
- Logistics Core (Logística inteligente)
- Automation Hub (Automatización)
- Customer Engagement (CRM)
- Supplier Network (Proveedores)
- Financial Operations (Finanzas especializadas)
- Analytics Platform (Análisis avanzado)
- Integration Layer (Integración)
- Intelligent UI (Interfaz inteligente)
- Mobile Field Ops (Operaciones móviles)
- Compliance Regulatory (Cumplimiento)
- Document Management (Gestión documental)
- Communication Hub (Comunicaciones)
- Configuration Engine (Configuración)
- Security Governance (Seguridad)

### 🎯 Features y Tasks
Cada épica contiene múltiples features y cada feature contiene varias tasks específicas con descripciones detalladas de implementación.

## Prerrequisitos para importación

### 1. Instalar GitHub CLI
```bash
# Ubuntu/Debian
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# macOS
brew install gh

# Windows
winget install GitHub.CLI
```

### 2. Autenticarse con GitHub
```bash
gh auth login
```
Sigue las instrucciones en pantalla para autenticarte.

### 3. Verificar que las Issues están habilitadas
```bash
gh repo edit --enable-issues
```

## Instrucciones de importación

### Paso 1: Crear labels necesarios
```bash
gh label create "epic" --color "d73a4a" --description "Epic stories"
gh label create "feature" --color "0075ca" --description "New features"
gh label create "task" --color "7057ff" --description "Tasks to complete"
```

### Paso 2: Importar issues
```bash
# Para una prueba con las primeras 5 issues:
head -6 github_issues.csv > test_issues.csv
python3 import_issues.py test_issues.csv

# Para importar todas las 246 issues:
python3 import_issues.py github_issues.csv
```

⚠️ **Nota**: El proceso de importación puede tomar 10-15 minutos debido a los límites de rate de la API de GitHub.

## Verificación de la importación

Una vez completada la importación, verifica que se crearon correctamente:

```bash
# Contar issues creadas
gh issue list --limit 300 | wc -l

# Ver issues por label
gh issue list --label "epic"
gh issue list --label "feature"
gh issue list --label "task"
```

## Organización posterior

### Crear Milestones por fases
```bash
gh api repos/:owner/:repo/milestones -f title="Fase 1: Fundaciones IA" -f description="Meses 1-3: Implementar AI Engine y Analytics Platform"
gh api repos/:owner/:repo/milestones -f title="Fase 2: Logística Inteligente" -f description="Meses 4-6: Logistics Core y Real-time Data"
gh api repos/:owner/:repo/milestones -f title="Fase 3: Automatización Avanzada" -f description="Meses 7-9: Automation Hub e Intelligent UI"
gh api repos/:owner/:repo/milestones -f title="Fase 4: Optimización y Escala" -f description="Meses 10-12: Experimentation Lab y optimización"
```

### Configurar Projects (opcional)
1. Ve a la pestaña **Projects** del repositorio
2. Crea un nuevo project board
3. Configura columnas: **To Do**, **In Progress**, **Review**, **Done**
4. Arrastra las épicas a las columnas correspondientes

## Distribución sugerida del equipo

- **AI/ML Team (3)**: AI Engine, Analytics Platform
- **Backend Logistics (3)**: Logistics Core, Automation Hub
- **Integration & Data (3)**: Integration Layer, Real-time Data Stream
- **Frontend & UX (2)**: Intelligent UI, Mobile Field Ops
- **Business Core (2)**: Business Core, Financial Operations
- **Customer & Supplier (2)**: Customer Engagement, Supplier Network
- **DevOps & Security (1)**: Infrastructure Management, Security Governance
- **Compliance & Docs (1)**: Compliance Regulatory, Document Management
- **Configuration (1)**: Configuration Engine, Communication Hub
- **Innovation (1)**: Experimentation Lab, Knowledge Training

## Métricas de éxito esperadas

- **Reducción de costos de transporte**: 15-25%
- **Mejora en tiempo de entrega**: 20-30%
- **Optimización de rutas**: 90% automáticas
- **Reducción de stock muerto**: 30-40%
- **Mejora en disponibilidad**: 95%+
- **Predicción de demanda**: 85%+ precisión
- **Reducción de errores manuales**: 80%+

## Soporte

Para dudas sobre la estructura de issues o problemas con la importación, consulta la documentación del proyecto o contacta al equipo de desarrollo.

---

**Generado automáticamente para el Sistema de Gestión Empresarial**