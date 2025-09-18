# sistema-gestion-empresarial

Sistema de Gestión Empresarial con arquitectura modular e inteligencia artificial integrada.

## Estructura del Proyecto

```
sistema_gestion_empresarial/
├── 🏢 business_core/                  # Núcleo de Negocio Tradicional (ERP Base)
├── 🧠 ai_engine/                      # Motor Central de IA
├── 🚛 logistics_core/                 # Núcleo de Logística Inteligente
├── 🤖 automation_hub/                 # Centro de Automatización
├── 👥 customer_engagement/            # Gestión de Clientes y CRM
├── 🏭 supplier_network/               # Red de Proveedores y Procurement
├── 💰 financial_operations/           # Operaciones Financieras Especializadas
├── 📊 analytics_platform/             # Plataforma de Análisis Avanzado
├── 🔗 integration_layer/              # Capa de Integración
├── 📱 intelligent_ui/                 # Interfaz Inteligente
├── 📱 mobile_field_ops/               # Operaciones Móviles y de Campo
├── 📋 compliance_regulatory/          # Cumplimiento Regulatorio Logístico
├── 📁 document_management/            # Gestión Documental Empresarial
├── 🔔 communication_hub/              # Centro de Comunicaciones
├── ⚙️ configuration_engine/           # Motor de Configuración y Personalización
├── 🛡️ security_governance/            # Seguridad y Gobernanza
├── 📡 real_time_data_stream/          # Procesamiento de Datos en Tiempo Real
├── 🔄 infrastructure_management/      # Gestión de Infraestructura y DR
├── 📚 knowledge_training/             # Gestión de Conocimiento y Entrenamiento
└── 🧪 experimentation_lab/            # Laboratorio de Experimentación IA
```

## Cómo comenzar

1. Crea el entorno virtual:
   ```bash
   python -m venv .venv
   ```
2. Activa el entorno virtual:
   - En Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación:
   ```bash
   python sistema_gestion_empresarial/main.py
   ```


# Sistema de Gestión Empresarial Inteligente
## Arquitectura para Logística y Automatización con IA

### 🏗️ Arquitectura General Completa

```
sistema_gestion_empresarial/
├── 🏢 business_core/                  # Núcleo de Negocio Tradicional (ERP Base)
├── 🧠 ai_engine/                      # Motor Central de IA
├── 🚛 logistics_core/                 # Núcleo de Logística Inteligente
├── 🤖 automation_hub/                 # Centro de Automatización
├── 👥 customer_engagement/            # Gestión de Clientes y CRM
├── 🏭 supplier_network/               # Red de Proveedores y Procurement
├── 💰 financial_operations/           # Operaciones Financieras Especializadas
├── 📊 analytics_platform/             # Plataforma de Análisis Avanzado
├── 🔗 integration_layer/              # Capa de Integración
├── 📱 intelligent_ui/                 # Interfaz Inteligente
├── 📱 mobile_field_ops/               # Operaciones Móviles y de Campo
├── 📋 compliance_regulatory/          # Cumplimiento Regulatorio Logístico
├── 📁 document_management/            # Gestión Documental Empresarial
├── 🔔 communication_hub/              # Centro de Comunicaciones
├── ⚙️ configuration_engine/           # Motor de Configuración y Personalización
├── 🛡️ security_governance/            # Seguridad y Gobernanza
├── 📡 real_time_data_stream/          # Procesamiento de Datos en Tiempo Real
├── 🔄 infrastructure_management/      # Gestión de Infraestructura y DR
├── 📚 knowledge_training/             # Gestión de Conocimiento y Entrenamiento
└── 🧪 experimentation_lab/            # Laboratorio de Experimentación IA
```

---

## 🏢 Business Core (Núcleo de Negocio Tradicional)
*Equipos: 2 Backend Engineers + 1 Business Analyst*

### ERP Foundational:

#### `business_core/traditional_modules/`
- **`financial_management/`**
  - `general_ledger.py` - Contabilidad general robusta
  - `accounts_payable_receivable.py` - Cuentas por pagar y cobrar
  - `budgeting_planning.py` - Presupuestación y planificación financiera
  - `tax_management.py` - Gestión de impuestos multi-jurisdicción

- **`human_resources/`**
  - `employee_lifecycle.py` - Ciclo de vida completo de empleados
  - `payroll_management.py` - Nómina y beneficios
  - `performance_management.py` - Gestión de desempeño tradicional
  - `compliance_hr.py` - Cumplimiento de RRHH

#### `business_core/master_data/`
- **`data_governance/`** - Gobernanza de datos maestros
- **`entity_management/`** - Gestión de entidades empresariales
- **`hierarchy_management/`** - Gestión de jerarquías organizacionales

---

## 👥 Customer Engagement (Gestión de Clientes y CRM)
*Equipos: 1 Backend Engineer + 1 Frontend Engineer*

### CRM Inteligente:

#### `customer_engagement/intelligent_crm/`
- **`customer_360/`**
  - `customer_profiling.py` - Perfiles de clientes 360°
  - `interaction_history.py` - Historial completo de interacciones
  - `predictive_customer_analytics.py` - Análisis predictivo de clientes

- **`sales_automation/`**
  - `lead_management.py` - Gestión inteligente de leads
  - `opportunity_tracking.py` - Seguimiento de oportunidades
  - `quote_configuration.py` - Configuración y cotización inteligente

#### `customer_engagement/service_excellence/`
- **`customer_service/`**
  - `case_management.py` - Gestión de casos de servicio
  - `sla_management.py` - Gestión de niveles de servicio
  - `customer_feedback_analysis.py` - Análisis de feedback de clientes

---

## 🏭 Supplier Network (Red de Proveedores y Procurement)
*Equipos: 1 Backend Engineer + 1 Procurement Specialist*

### Gestión Inteligente de Proveedores:

#### `supplier_network/procurement_intelligence/`
- **`supplier_management/`**
  - `supplier_qualification.py` - Calificación y evaluación de proveedores
  - `performance_monitoring.py` - Monitoreo de desempeño de proveedores
  - `risk_assessment.py` - Evaluación de riesgos de proveedores
  - `contract_management.py` - Gestión inteligente de contratos

#### `supplier_network/sourcing_optimization/`
- **`strategic_sourcing/`**
  - `spend_analysis.py` - Análisis inteligente de gastos
  - `supplier_selection.py` - Selección optimizada de proveedores
  - `negotiation_support.py` - Soporte a negociaciones

---

## 💰 Financial Operations (Operaciones Financieras Especializadas)
*Equipos: 1 Backend Engineer especializado en FinTech*

### Finanzas Especializadas en Logística:

#### `financial_operations/logistics_costing/`
- **`transportation_costing/`**
  - `freight_cost_management.py` - Gestión de costos de flete
  - `fuel_cost_optimization.py` - Optimización de costos de combustible
  - `carrier_billing.py` - Facturación inteligente de transportistas

#### `financial_operations/revenue_management/`
- **`pricing_intelligence/`**
  - `dynamic_pricing.py` - Precios dinámicos basados en IA
  - `profitability_analysis.py` - Análisis de rentabilidad por ruta/cliente
  - `invoice_automation.py` - Automatización inteligente de facturación

---

## 📱 Mobile Field Operations (Operaciones Móviles y de Campo)
*Equipos: 1 Mobile Developer + 1 Frontend Engineer*

### Apps para Operaciones de Campo:

#### `mobile_field_ops/driver_apps/`
- **`driver_mobile_suite/`**
  - `route_navigation.py` - Navegación optimizada para conductores
  - `delivery_confirmation.py` - Confirmación de entregas con firmas
  - `vehicle_inspection.py` - Inspecciones de vehículos digitales
  - `hours_of_service.py` - Gestión de horas de servicio

#### `mobile_field_ops/warehouse_mobility/`
- **`warehouse_mobile_apps/`**
  - `mobile_picking.py` - Aplicación de picking móvil
  - `inventory_scanning.py` - Escaneo de inventario en tiempo real
  - `quality_control.py` - Control de calidad móvil

---

## 📋 Compliance & Regulatory (Cumplimiento Regulatorio Logístico)
*Equipos: 1 Compliance Engineer + 0.5 Legal Specialist*

### Cumplimiento Especializado:

#### `compliance_regulatory/transportation_compliance/`
- **`regulatory_management/`**
  - `dot_compliance.py` - Cumplimiento DOT (Department of Transportation)
  - `hazmat_management.py` - Gestión de materiales peligrosos
  - `international_trade.py` - Comercio internacional y aduanas
  - `environmental_compliance.py` - Cumplimiento ambiental

#### `compliance_regulatory/audit_trail/`
- **`compliance_monitoring/`**
  - `regulatory_reporting.py` - Reportería regulatoria automatizada
  - `compliance_alerts.py` - Alertas de cumplimiento proactivas

---

## 📁 Document Management (Gestión Documental Empresarial)
*Equipos: 1 Backend Engineer*

### Documentación Inteligente:

#### `document_management/intelligent_docs/`
- **`document_processing/`**
  - `document_digitization.py` - Digitalización inteligente de documentos
  - `automated_classification.py` - Clasificación automática de documentos
  - `contract_intelligence.py` - Inteligencia de contratos y documentos legales

#### `document_management/logistics_docs/`
- **`shipping_documentation/`**
  - `bill_of_lading.py` - Gestión de conocimientos de embarque
  - `customs_documentation.py` - Documentación aduanal automatizada
  - `certification_management.py` - Gestión de certificaciones

---

## 🔔 Communication Hub (Centro de Comunicaciones)
*Equipos: 1 Backend Engineer*

### Comunicaciones Empresariales:

#### `communication_hub/notification_engine/`
- **`intelligent_notifications/`**
  - `priority_routing.py` - Enrutamiento de notificaciones por prioridad
  - `multi_channel_delivery.py` - Entrega multi-canal (SMS, email, app)
  - `escalation_management.py` - Gestión de escalamientos automáticos

#### `communication_hub/collaboration_tools/`
- **`team_collaboration/`**
  - `task_coordination.py` - Coordinación inteligente de tareas
  - `real_time_messaging.py` - Mensajería empresarial en tiempo real

---

## ⚙️ Configuration Engine (Motor de Configuración)
*Equipos: 1 Backend Engineer + 0.5 DevOps Engineer*

### Personalización Empresarial:

#### `configuration_engine/customization_framework/`
- **`business_rules_engine/`**
  - `configurable_workflows.py` - Flujos de trabajo configurables
  - `industry_templates.py` - Plantillas específicas por industria
  - `white_label_configuration.py` - Configuración white-label

#### `configuration_engine/tenant_management/`
- **`multi_tenancy/`**
  - `tenant_isolation.py` - Aislamiento de inquilinos
  - `custom_branding.py` - Personalización de marca por cliente

---

## 🔄 Infrastructure Management (Gestión de Infraestructura)
*Equipos: 1 DevOps Engineer + 1 Infrastructure Engineer*

### Operaciones de Infraestructura:

#### `infrastructure_management/disaster_recovery/`
- **`backup_systems/`**
  - `automated_backups.py` - Respaldos automatizados
  - `disaster_recovery.py` - Recuperación ante desastres
  - `business_continuity.py` - Continuidad de negocio

#### `infrastructure_management/monitoring/`
- **`system_monitoring/`**
  - `performance_monitoring.py` - Monitoreo de performance del sistema
  - `capacity_planning.py` - Planificación de capacidad
  - `sla_monitoring.py` - Monitoreo de SLAs técnicos

---

## 📚 Knowledge & Training (Gestión de Conocimiento)
*Equipos: 1 Technical Writer + 0.5 Training Specialist*

### Capacitación y Conocimiento:

#### `knowledge_training/learning_management/`
- **`training_modules/`**
  - `user_training.py` - Módulos de entrenamiento de usuarios
  - `certification_tracking.py` - Seguimiento de certificaciones
  - `knowledge_base.py` - Base de conocimiento inteligente

#### `knowledge_training/documentation/`
- **`intelligent_help/`**
  - `contextual_help.py` - Ayuda contextual inteligente
  - `automated_documentation.py` - Documentación automatizada
*Equipos: 2 ML Engineers + 1 Data Scientist*

### Componentes Principales:

#### `ai_engine/core/`
- **`prediction_models/`**
  - `demand_forecasting.py` - Predicción de demanda multi-modal
  - `supply_risk_assessment.py` - Evaluación de riesgos de suministro
  - `maintenance_predictor.py` - Mantenimiento predictivo de activos
  - `customer_behavior_analysis.py` - Análisis de comportamiento de clientes

#### `ai_engine/ml_ops/`
- **`model_training/`** - Pipeline de entrenamiento automatizado
- **`model_deployment/`** - Despliegue y versionado de modelos
- **`model_monitoring/`** - Monitoreo de drift y performance
- **`feature_engineering/`** - Ingeniería de características automatizada

#### `ai_engine/knowledge_graph/`
- **`entity_management/`** - Gestión de entidades empresariales
- **`relationship_mapping/`** - Mapeo de relaciones complejas
- **`semantic_search/`** - Búsqueda semántica avanzada

---

## 🚛 Logistics Core (Núcleo de Logística Inteligente)
*Equipos: 3 Backend Engineers + 1 Logistics Specialist*

### Componentes Especializados:

#### `logistics_core/intelligent_routing/`
- **`dynamic_route_optimizer.py`**
  - Algoritmos genéticos para optimización multi-objetivo
  - Consideración de tráfico en tiempo real
  - Gestión de restricciones de vehículos y conductores
  
- **`fleet_management/`**
  - `vehicle_tracking.py` - Rastreo y telemetría de vehículos
  - `driver_performance.py` - Análisis de desempeño de conductores
  - `fuel_optimization.py` - Optimización de consumo de combustible

#### `logistics_core/smart_inventory/`
- **`predictive_inventory_management/`**
  - `demand_sensing.py` - Sensado de demanda en tiempo real
  - `stock_optimization.py` - Optimización de niveles de stock
  - `supplier_intelligence.py` - Inteligencia de proveedores
  
- **`warehouse_optimization/`**
  - `space_allocation.py` - Asignación inteligente de espacios
  - `picking_path_optimization.py` - Optimización de rutas de picking
  - `cross_docking_manager.py` - Gestión inteligente de cross-docking

#### `logistics_core/supply_chain_visibility/`
- **`end_to_end_tracking/`** - Trazabilidad completa de la cadena
- **`disruption_management/`** - Gestión proactiva de disrupciones
- **`collaborative_planning/`** - Planificación colaborativa con socios

---

## 🤖 Automation Hub (Centro de Automatización)
*Equipos: 2 Backend Engineers + 1 IoT Specialist*

### Sistemas de Automatización:

#### `automation_hub/robotics_integration/`
- **`warehouse_robotics/`**
  - `robot_coordination.py` - Coordinación de múltiples robots
  - `task_scheduling.py` - Programación inteligente de tareas
  - `collision_avoidance.py` - Prevención de colisiones y congestión

#### `automation_hub/iot_ecosystem/`
- **`sensor_networks/`**
  - `environmental_monitoring.py` - Monitoreo de condiciones ambientales
  - `asset_condition_tracking.py` - Seguimiento de condición de activos
  - `energy_management.py` - Gestión inteligente de energía

#### `automation_hub/process_automation/`
- **`workflow_engine/`**
  - `business_process_automation.py` - RPA empresarial
  - `approval_workflows.py` - Flujos de aprobación inteligentes
  - `exception_handling.py` - Manejo automatizado de excepciones

---

## 📊 Analytics Platform (Plataforma de Análisis Avanzado)
*Equipos: 1 Data Engineer + 1 BI Developer*

### Capacidades Analíticas:

#### `analytics_platform/real_time_dashboard/`
- **`executive_cockpit/`** - Dashboard ejecutivo en tiempo real
- **`operational_dashboards/`** - Dashboards operacionales especializados
- **`predictive_alerts/`** - Sistema de alertas predictivas

#### `analytics_platform/advanced_analytics/`
- **`pattern_recognition/`**
  - `anomaly_detection.py` - Detección de anomalías en operaciones
  - `trend_analysis.py` - Análisis de tendencias avanzado
  - `correlation_mining.py` - Minería de correlaciones ocultas

#### `analytics_platform/business_intelligence/`
- **`automated_reporting/`** - Reportería automatizada e inteligente
- **`what_if_scenarios/`** - Análisis de escenarios hipotéticos
- **`roi_optimization/`** - Optimización de retorno de inversión

---

## 🔗 Integration Layer (Capa de Integración)
*Equipos: 2 Integration Engineers*

### Conectividad Empresarial:

#### `integration_layer/api_gateway/`
- **`unified_api_management/`** - Gestión unificada de APIs
- **`rate_limiting/`** - Control de tráfico y límites
- **`authentication_hub/`** - Centro de autenticación unificado

#### `integration_layer/data_connectors/`
- **`erp_connectors/`** - Conectores para sistemas ERP existentes
- **`iot_data_ingestion/`** - Ingestión de datos IoT masivos
- **`third_party_apis/`** - Integración con APIs de terceros
- **`legacy_system_bridges/`** - Puentes para sistemas heredados

#### `integration_layer/message_bus/`
- **`event_streaming/`** - Streaming de eventos empresariales
- **`message_queuing/`** - Cola de mensajes distribuida
- **`data_synchronization/`** - Sincronización de datos en tiempo real

---

## 📱 Intelligent UI (Interfaz Inteligente)
*Equipos: 2 Frontend Engineers + 1 UX/UI Designer*

### Experiencia de Usuario Inteligente:

#### `intelligent_ui/adaptive_interfaces/`
- **`role_based_customization/`** - Personalización basada en roles
- **`ai_assisted_navigation/`** - Navegación asistida por IA
- **`contextual_help/`** - Ayuda contextual inteligente

#### `intelligent_ui/visualization_engine/`
- **`dynamic_charts/`** - Gráficos dinámicos e interactivos
- **`3d_warehouse_visualization/`** - Visualización 3D de almacenes
- **`route_mapping/`** - Mapas interactivos de rutas

#### `intelligent_ui/voice_and_chat/`
- **`natural_language_interface/`** - Interfaz de lenguaje natural
- **`voice_commands/`** - Comandos de voz para operaciones
- **`intelligent_chatbot/`** - Chatbot empresarial inteligente

---

## 🛡️ Security & Governance (Seguridad y Gobernanza)
*Equipos: 1 Security Engineer + 0.5 Compliance Specialist*

### Seguridad Empresarial:

#### `security_governance/ai_security/`
- **`model_security/`** - Seguridad de modelos de IA
- **`data_privacy/`** - Protección de privacidad de datos
- **`bias_monitoring/`** - Monitoreo de sesgos algorítmicos

#### `security_governance/enterprise_security/`
- **`zero_trust_architecture/`** - Arquitectura de confianza cero
- **`audit_trails/`** - Trillos de auditoría completos
- **`compliance_management/`** - Gestión de cumplimiento regulatorio

---

## 📡 Real-Time Data Stream (Procesamiento en Tiempo Real)
*Equipos: 1 Data Engineer especializaodo en streaming*

### Procesamiento de Datos Masivos:

#### `real_time_data_stream/stream_processing/`
- **`kafka_ecosystem/`** - Ecosistema Apache Kafka
- **`real_time_analytics/`** - Análisis en tiempo real
- **`data_lake_management/`** - Gestión de data lake empresarial

#### `real_time_data_stream/event_processing/`
- **`complex_event_processing/`** - Procesamiento de eventos complejos
- **`stream_ml_inference/`** - Inferencia ML en streams
- **`data_quality_monitoring/`** - Monitoreo de calidad de datos

---

## 🧪 Experimentation Lab (Laboratorio de Experimentación)
*Equipos: 1 Research Engineer + 0.5 Innovation Lead*

### Innovación Continua:

#### `experimentation_lab/ai_research/`
- **`emerging_algorithms/`** - Investigación de algoritmos emergentes
- **`industry_specific_models/`** - Modelos específicos por industria
- **`explainable_ai/`** - IA explicable y transparente

#### `experimentation_lab/prototype_development/`
- **`proof_of_concepts/`** - Pruebas de concepto rápidas
- **`a_b_testing_framework/`** - Framework de testing A/B
- **`innovation_pipeline/`** - Pipeline de innovación estructurada

---

## 🎯 Módulos de Negocio Existentes (Actualizados)

### `modules/hr/` - Recursos Humanos Inteligentes
- **`workforce_analytics/`** - Análisis predictivo de fuerza laboral
- **`skills_optimization/`** - Optimización de habilidades y asignaciones
- **`performance_intelligence/`** - Inteligencia de desempeño

### `modules/inventory/` - Inventario Tradicional (Integrado)
- Integrado completamente con `logistics_core/smart_inventory/`
- Mantiene APIs de compatibilidad hacia atrás
- Añade capacidades de IA sin interrumpir funcionalidad existente

### `modules/finance/` - Finanzas Inteligentes
- **`predictive_budgeting/`** - Presupuestación predictiva
- **`cash_flow_optimization/`** - Optimización de flujo de efectivo
- **`financial_risk_assessment/`** - Evaluación de riesgos financieros

---

## 🚀 Plan de Implementación por Fases

### **Fase 1 (Meses 1-3): Fundaciones IA**
- Implementar `ai_engine/core/prediction_models/`
- Desarrollar `analytics_platform/real_time_dashboard/`
- Establecer `integration_layer/api_gateway/`

### **Fase 2 (Meses 4-6): Logística Inteligente**
- Lanzar `logistics_core/intelligent_routing/`
- Implementar `logistics_core/smart_inventory/`
- Desarrollar `real_time_data_stream/stream_processing/`

### **Fase 3 (Meses 7-9): Automatización Avanzada**
- Desplegar `automation_hub/robotics_integration/`
- Implementar `automation_hub/iot_ecosystem/`
- Lanzar `intelligent_ui/adaptive_interfaces/`

### **Fase 4 (Meses 10-12): Optimización y Escala**
- Completar `experimentation_lab/ai_research/`
- Optimizar todos los componentes integrados
- Lanzamiento comercial completo

---

## 📈 Métricas de Éxito por Componente

### Logística Inteligente:
- **Reducción de costos de transporte**: 15-25%
- **Mejora en tiempo de entrega**: 20-30%
- **Optimización de rutas**: 90% de rutas optimizadas automáticamente

### Gestión de Inventario:
- **Reducción de stock muerto**: 30-40%
- **Mejora en disponibilidad de productos**: 95%+
- **Predicción de demanda**: 85%+ de precisión

### Automatización:
- **Reducción de errores manuales**: 80%+
- **Aumento en productividad**: 25-35%
- **Tiempo de procesamiento**: 60% más rápido

---

---

## 👥 Distribución Completa del Equipo (Ampliado a 18-20 Desarrolladores)

### **Core Team (13 desarrolladores originales):**
- **AI/ML Team (3)**: Motor de IA y modelos predictivos
- **Backend Logistics (3)**: Núcleo de logística inteligente + automatización
- **Integration & Data (3)**: Integración, streaming de datos, y APIs
- **Frontend & UX (2)**: Interfaz inteligente y experiencia usuario
- **DevOps & Security (1)**: Infraestructura, seguridad y DR
- **Innovation & Research (1)**: Experimentación e innovación

### **Extended Team (5-7 desarrolladores adicionales para completud total):**
- **Business Core Team (2)**: ERP tradicional, finanzas, RRHH
- **Customer & Supplier Team (2)**: CRM, gestión de proveedores, procurement
- **Mobile & Field Operations (1)**: Apps móviles para operaciones de campo
- **Compliance & Documentation (1)**: Cumplimiento regulatorio y gestión documental
- **Configuration & Training (1)**: Personalización y gestión de conocimiento

### **Especialistas de Apoyo (Medio Tiempo o Consultores):**
- **Business Analysts (2)**: Especialistas en logística y procurement
- **Compliance Specialists (1)**: Experto en regulaciones de transporte
- **UX/UI Designer (1)**: Especialista en experiencia de usuario
- **Technical Writers (1)**: Documentación técnica y entrenamiento

---

## 🎯 Versiones de Implementación Sugeridas

### **MVP (Producto Mínimo Viable) - Core Team de 13:**
Enfocarse en componentes diferenciadores:
- `ai_engine/` (completo)
- `logistics_core/` (completo)  
- `automation_hub/` (básico)
- `analytics_platform/` (básico)
- `integration_layer/` (básico)
- `intelligent_ui/` (básico)
- Módulos tradicionales existentes (mejorados con IA)

### **Enterprise Edition - Equipo Completo de 18-20:**
Incluir todos los componentes para una solución empresarial completa:
- Todos los componentes MVP +
- `business_core/` (completo)
- `customer_engagement/` (completo)
- `supplier_network/` (completo)
- `mobile_field_ops/` (completo)
- `compliance_regulatory/` (completo)
- Todos los componentes de soporte

### **Industry-Specific Versions:**
- **Manufacturing Focus**: Énfasis en `automation_hub/` y `supplier_network/`
- **Retail Focus**: Énfasis en `customer_engagement/` y `analytics_platform/`
- **3PL Focus**: Énfasis en `logistics_core/` y `mobile_field_ops/`