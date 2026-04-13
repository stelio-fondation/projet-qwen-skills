# 🎬 Video To Guide — Compétence Qwen Code

> Transformez du contenu vidéo en guides web interactifs et professionnels. Cette compétence automatise l'analyse de vidéos, leur structuration en étapes logiques, et la génération d'une application React complète avec tutoriels, diagrammes et extraits de code copiables.

---

## 🔄 Core Workflow (Processus en 5 phases)

### Phase 1 : Analyse du Contenu
Extraction et structuration du contenu depuis votre source vidéo (YouTube, Vimeo, fichiers locaux, ou documentation existante). Le système identifie les sujets clés, les étapes et leurs relations.

### Phase 2 : Sélection du Design
Choisissez un pattern de design (glassmorphic, minimal, bold, playful) et personnalisez couleurs et typographie. Le design s'applique uniformément sur toutes les pages.

### Phase 3 : Génération du Projet
Création automatique d'un projet React avec page d'accueil, tutoriels étape par étape, et composants interactifs. Toutes les pages sont pré-connectées avec une navigation fonctionnelle.

### Phase 4 : Peuplement du Contenu
Ajout de types de contenu spécifiques (commandes, prompts, configurations, études de cas) à chaque étape. Le système génère les composants UI appropriés pour chaque type.

### Phase 5 : Polissage & Déploiement
Correction des erreurs, tests de navigation, et préparation pour la publication. La compétence inclut des patterns de débogage pour les problèmes courants.

---

## 📥 Sources d'Entrée

La compétence accepte plusieurs formats d'entrée :

| Type | Description | Outil Qwen Code |
|------|-------------|-----------------|
| **Vidéo** | URLs YouTube/Vimeo ou fichiers vidéo locaux | `qwen-analyze-video` pour extraire transcripts et points clés |
| **Documentation** | Fichiers Markdown, docs API, notes structurées | `qwen-parse-docs` pour parser le contenu textuel |
| **Hybride** | Combinaison vidéo + documentation complémentaire | Fusion intelligente via `qwen-merge-context` |

---

## 🧩 Types de Contenu Supportés

Contenu structuré mappé vers des composants React pré-construits :

```yaml
Commands:
  format: "commande + description"
  features: [copie-clipboard, syntax-highlighting, explication]
  exemple: |
    npx ctx7@latest setup
    → Installe et initialise Context7

Prompts:
  catégories: [Restriction, Search, Chaining, Generation]
  format: "contexte + prompt + usage attendu"
  exemple: |
    Category: Restriction Bash
    Prompt: "Restrict to bash commands only, no Python"

Configurations:
  formats: [JSON, YAML, TOML]
  features: [syntax-highlighting, before/after diff, validation]
  exemple: |
    {
      "version": "1.0.0",
      "skillsPath": "~/.ctx7/skills"
    }

Case Studies:
  structure: [user story, étapes, résultat, métriques]
  exemple: |
    Scenario: Migration from MCP
    Before: 37k tokens used at startup
    After: 0 tokens at startup, loaded on-demand
    Result: 163k tokens available for context

Troubleshooting:
  format: "erreur + cause racine + commande de fix"
  exemple: |
    Error: "Module not found: 'ctx7'"
    Cause: Package not installed in current environment
    Fix: npm install -g ctx7@latest
```

---

## 🎨 Patterns de Design

| Pattern | Caractéristiques | Cas d'usage recommandé |
|---------|-----------------|----------------------|
| **Glassmorphic** *(défaut)* | Cartes semi-transparentes, blur, fond sombre, accents indigo/violet | Docs techniques, guides développeurs |
| **Minimal** | Typographie épurée, whitespace, couleur d'accent unique | Contenu éducatif, onboarding |
| **Bold** | Fort contraste, couleurs vibrantes, grosse typographie | Marketing, annonces, landing pages |
| **Playful** | Coins arrondis, gradients, animations subtiles | Tutoriels créatifs, outils internes |
| **Custom** | Palette, fonts, spacing définis via tokens Tailwind | Besoins spécifiques de marque |

> 💡 **Personnalisation** : Utilisez les tokens Tailwind CSS (`--qwen-primary`, `--qwen-radius`, etc.) pour définir votre propre système de design.

---

## ⚙️ Flexibilité & Personnalisation

```yaml
Step Count:
  auto-detect: true
  min_steps: 2
  max_steps: 20+
  override: "manual step definition via JSON"

Navigation:
  breadcrumbs: auto-generated
  next_prev_buttons: true
  back_to_home: true
  keyboard_shortcuts: ["←", "→", "h"]

Content Density:
  per_step_components:
    - overview
    - tutorial
    - code_examples
    - real_world_scenarios
    - troubleshooting
    - related_resources

Component Reuse:
  library:
    - CopyableCommand
    - DiagramComparison
    - PromptCard
    - ImplementationSteps
    - ConfigViewer
    - ErrorTroubleshooter
  props_documentation: "available in component-api.md"
```

---

## 🌳 Arbre de Décision du Workflow

```
START: Avez-vous du contenu vidéo à analyser ?
│
├─ OUI → Fournissez URL YouTube/Vimeo ou fichier local
│        → qwen-analyze-video extrait transcript + points clés
│        → Passage à la sélection du design
│
├─ NON → Fournissez documentation Markdown ou notes structurées
│        → qwen-parse-docs parse et structure le contenu
│        → Passage à la sélection du design
│
NEXT: Choisissez un pattern de design
      [glassmorphic | minimal | bold | playful | custom]
│
THEN: Spécifiez le nombre d'étapes OU laissez l'auto-détection
│
FINALLY: Ajoutez les types de contenu pour chaque étape
         [commands | prompts | configs | case_studies | troubleshooting]
```

---

## 📋 Étapes Détaillées

### Étape 1 : Analyse du Contenu
```bash
# Input exemple
URL: https://www.youtube.com/watch?v=example
Durée: 15 minutes
Sujets: MCP, CLI, Skills, Context optimization

# Traitement Qwen Code
qwen-analyze-video \
  --source "URL_or_path" \
  --extract transcript,keypoints,code_snippets \
  --output structured_json
```

**Output JSON structuré :**
```json
{
  "title": "MCP to CLI + Skills",
  "description": "Optimize AI context by replacing MCP with CLI + Skills",
  "metadata": {
    "duration": "15:00",
    "language": "en",
    "difficulty": "intermediate"
  },
  "steps": [
    {
      "name": "Configuration",
      "description": "Set up Context7",
      "keyPoints": ["Install Context7", "Configure paths", "Test installation"],
      "codeSnippets": ["npx ctx7@latest setup"],
      "estimatedTime": "3 min"
    }
  ]
}
```

### Étape 2 : Sélection du Design
```yaml
# Configuration design (qwen-design-config.yaml)
pattern: glassmorphic
theme:
  mode: dark
  colors:
    primary: "#6366f1"    # indigo-500
    secondary: "#8b5cf6"  # violet-500
    background: "#0f172a" # slate-900
    surface: "rgba(30,41,59,0.7)"
  typography:
    heading: "Inter, sans-serif"
    body: "JetBrains Mono, monospace"
  effects:
    blur: "backdrop-blur-md"
    border: "border-white/10"
    shadow: "shadow-xl shadow-indigo-500/10"
```

### Étape 3 : Génération du Projet
```bash
qwen-generate-project \
  --input structured_content.json \
  --design qwen-design-config.yaml \
  --output ./my-video-guide \
  --framework react+tailwind
```

**Structure générée :**
```
my-video-guide/
├── src/
│   ├── pages/
│   │   ├── Home.tsx          # Hero, problem/solution, overview
│   │   ├── Step1_Config.tsx  # Page étape 1
│   │   ├── Step2_CLI.tsx     # Page étape 2
│   │   └── ...
│   ├── components/
│   │   ├── CopyableCommand.tsx
│   │   ├── DiagramComparison.tsx
│   │   ├── PromptCard.tsx
│   │   └── ImplementationSteps.tsx
│   ├── lib/
│   │   ├── navigation.ts     # Breadcrumbs, routing helpers
│   │   └── utils.ts          # Clipboard, formatting helpers
│   └── styles/
│       └── globals.css       # Tailwind + design tokens
├── public/
│   ├── diagrams/             # SVG générés automatiquement
│   └── assets/               # Images, icônes
├── qwen.config.ts            # Configuration projet Qwen Code
└── package.json
```

### Étape 4 : Peuplement du Contenu
Pour chaque étape, enrichissez avec des composants spécifiques :

```tsx
// Exemple d'intégration dans Step1_Config.tsx
<StepLayout title="Configuration" stepNumber={1}>
  <Overview>
    Configurez Context7 pour optimiser votre contexte AI.
  </Overview>
  
  <CopyableCommand 
    command="npx ctx7@latest setup"
    description="Installe et initialise Context7 dans votre projet"
  />
  
  <ConfigViewer 
    before={{ tokens: 37000, loading: "startup" }}
    after={{ tokens: 0, loading: "on-demand" }}
    improvement="+163k tokens disponibles"
  />
  
  <Troubleshooting 
    items={[
      {
        error: "Permission denied",
        cause: "npm global prefix requires sudo",
        fix: "npm config set prefix '~/.npm-global'"
      }
    ]}
  />
</StepLayout>
```

### Étape 5 : Polissage & Déploiement
```bash
# Validation automatique
qwen-validate-project ./my-video-guide

# Tests de navigation
qwen-test-nav ./my-video-guide --check-links --check-components

# Build pour production
qwen-build ./my-video-guide --optimize --output dist/

# Options de déploiement
qwen-deploy ./dist \
  --target [vercel | netlify | github-pages | custom] \
  --domain yourguide.com  # optionnel
```

**Problèmes courants & correctifs :**
| Erreur | Cause | Solution Qwen Code |
|--------|-------|-------------------|
| `Nested <a> tags` | Link enveloppe un `<a>` natif | Utiliser `className` sur `Link`, supprimer `<a>` interne |
| `Import missing` | Composant non importé | Exécuter `qwen-fix-imports --auto` |
| `Token mismatch` | Variables Tailwind non définies | Vérifier `qwen-design-config.yaml` et `globals.css` |
| `Route not found` | `href` incohérent avec `App.tsx` | Utiliser `qwen-sync-routes` pour harmoniser |

---

## 📚 Ressources Qwen Code

```
scripts/
├── analyze_video_content.py    # Wrapper pour qwen-analyze-video
├── generate_step_pages.py      # Création pages React par étape
├── generate_home_page.py       # Génération page d'accueil
├── create_diagram_svg.py       # Diagrammes comparatifs SVG
└── validate_project.py         # Validation pré-déploiement

references/
├── workflow.md                 # Workflow complet + points de décision
├── content-types.md            # Formats commandes, prompts, configs
├── design-patterns.md          # Specs visuelles par pattern
├── video-sources.md            # Sources vidéo supportées + méthodes
├── component-api.md            # Props & usage des composants
└── qwen-integration.md         # Intégration avec l'écosystème Qwen

templates/
├── project-structure.template  # Layout de projet React de base
├── step-page.template.tsx      # Template page étape
├── home-page.template.tsx      # Template page d'accueil
├── component-library.template.tsx  # Bibliothèque de composants
└── qwen.config.template.ts     # Configuration projet Qwen Code
```

---

## 🚀 Commandes Rapides Qwen Code

```bash
# Démarrage rapide avec vidéo YouTube
qwen video-to-guide \
  --url "https://youtube.com/watch?v=xxx" \
  --design glassmorphic \
  --output ./my-guide

# Démarrage avec documentation Markdown
qwen video-to-guide \
  --docs ./content/*.md \
  --design minimal \
  --steps 5 \
  --output ./edu-guide

# Mode interactif (assistant pas-à-pas)
qwen video-to-guide --interactive

# Prévisualisation locale
cd ./my-guide && qwen dev --port 3000

# Export pour partage
qwen export ./my-guide --format [zip | docker | static]
```

---

## 🎯 Bonnes Pratiques Qwen Code

✅ **Avant l'analyse** :
- Vérifiez que la vidéo a un transcript (activez les sous-titres YouTube si besoin)
- Préparez un résumé textuel si la vidéo est très technique

✅ **Pendant la génération** :
- Utilisez `--dry-run` pour valider la structure avant génération complète
- Personnalisez les tokens de design tôt pour éviter des refontes CSS

✅ **Après génération** :
- Testez la navigation sur mobile et desktop
- Validez que tous les snippets de code sont exécutables
- Ajoutez des métadonnées SEO dans `qwen.config.ts`

---

> 💡 **Astuce Pro** : Combinez cette compétence avec `qwen-summarize` pour générer automatiquement des résumés exécutifs en haut de chaque guide, et avec `qwen-translate` pour publier vos guides en plusieurs langues.

*Cette compétence est native à l'écosystème Qwen Code et tire parti de l'analyse sémantique avancée, de la génération de code contextuelle, et de l'intégration Tailwind/React optimisée.* 🤖✨