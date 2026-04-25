---
title: Parent-Child Structure — User Manual Implementation Plan
date: 2026-04-23
owner: Kseniia (BA, test assignment for AXIOM.tech)
po: Maya Pivovarova (@mayya_pi)
feature: Parent-Child Structure (menu item variants in Gen1POS)
context: HoReCa / restaurant POS
status: executed through drafting and validation; final git-packaging cleanup in progress
---

# Parent-Child Structure — User Manual Implementation Plan

## 0. TL;DR

Descriptive feature-level user manual для Parent-Child Structure в Gen1POS, собранный из video + normalized transcript + screenshot archive (`34` cropped frames: `32` original + `2` replacement frames) под условиями **test assignment** (high self-reliance, no admin-panel access, no follow-up calls, minimal PO demands).

Методологический стек подобран прагматично под характеристики фичи (single feature, stable, UI-visible, single-SME): **Diátaxis + Microsoft Writing Style Guide + Minimalism + ISO/IEC/IEEE 26514 + BABOK v3 Elicitation + RTM**. Из черновика `plan.md` сознательно убраны DITA, Information Mapping, JTBD и persona-driven как отдельная дорожка — overhead без выгоды для single-feature MD-мануала.

План был реализован как **17 атомарных шагов в 6 фазах** (Framing & Elicitation → Evidence → Scope & IA → Drafting → Validation → Publishing). На текущий момент пакет собран; в работе остались только consistency-pass и git-packaging.

---

## 1. Контекст и констрейнты

### 1.1 Характеристики задачи (под них и подбирался стек)

| # | Характеристика | Следствие |
|---|---|---|
| C1 | Одна фича, не полный продукт | Не нужен DITA/XML pipeline, reuse infrastructure |
| C2 | Фича stable, уже в проде | Descriptive, не prescriptive |
| C3 | Single-SME (Maya), knowledge transfer через скринкаст | Elicitation-техники, не requirements workshop |
| C4 | UI-visible поведение | Screenshot-driven |
| C5 | HoReCa-admin аудитория (гипотеза H1) | Task-oriented с бизнес-контекстом меню ресторана |
| C6 | Один канал публикации (гипотеза) | Markdown single-source |
| C7 | Deadline не задан | Есть время на правильный процесс |

### 1.2 Констрейнты test assignment

- **High self-reliance**: всё, что можно вывести из video/transcript собственным ресёрчем, выводим сами.
- **No admin-panel access**: не запрашиваем учётку в коммерческой системе. Edge-cases, не видимые в скринкасте, → `08-known-limitations.md`.
- **No follow-up calls**: interaction с PO — минимальный Telegram-батч (4 вопроса), не созвоны.
- **Graceful "not documented in v1"**: явная маркировка gap'ов вместо ложной полноты. Опора на ISO 26514 §8 и safe-scope publication principle.

---

## 2. Методологический фундамент (pragmatic stack)

### 2.1 Что берём

| Инструмент | Роль | Почему именно он |
|---|---|---|
| **Diátaxis** (Procida, 2017) | Структурный скелет мануала | 4 явных слота (tutorial / how-to / reference / explanation); tutorial опускаем (фича маленькая, onboarding-путь не нужен). Убирает микс инструкции + теории + FAQ в кашу. |
| **Microsoft Writing Style Guide** | Style & procedure writing | Индустриальная конвенция для UI end-user docs. Imperative mood, UI capitalization, screenshot captions. Google Dev Style — для API/кода, нам не подходит. |
| **Minimalism** (Carroll, 1990) | Принципы внутри how-to | Task-first, не feature-first. Минимум теории перед действием, fast path. Работает внутри Diátaxis how-to-слота. |
| **ISO/IEC/IEEE 26514** | Meta-framework и DoD checklist | Референс качества (completeness, accuracy, accessibility, usability). Не drafting-framework, а QA-чеклист. |
| **BABOK v3 — Elicitation Techniques** (Ch.10) | Sub-process для Phase 1 | Structured SME Q&A. Берём только elicitation-главу, не весь BABOK. |
| **Requirements Traceability Matrix (RTM)** | QA mechanism | Каждое утверждение → источник (timestamp / screen / SME-ответ). Защита от drift'а. |

### 2.2 Что отбрасываем из `docs/plan.md` и почему

| Выкинуто | Причина |
|---|---|
| **DITA** | XML-пайплайн, topic specialisation, CMS. Для single-MD-мануала — overhead. Diátaxis решает IA-задачу проще. |
| **Information Mapping (R. Horn)** | Проприетарная методика с закрытой лицензией; перекрывается с MS Style Guide и Diátaxis reference-слотом. |
| **JTBD** | Discovery-фреймворк; для descriptive docs stable-фичи не добавляет сверх Diátaxis how-to. Неподходящий этап. |
| **Persona-driven как отдельная дорожка** | Сворачиваю в один шаг Audience Card. Одной персоны в v1 достаточно. |

**Итого**: было 7, стало 6, и из них 2 «лёгкие» (RTM, 26514 — только как чеклист). Вес стека ≈ в 2 раза меньше.

---

## 3. Target State — образ итогового результата

### 3.1 Что лежит в финальном пакете

```
docs/manual/
├── 00-index.md                  # Overview + карта документов
├── 01-explanation.md            # Что такое Parent-Child, зачем, когда (концепт)
├── 02-howto-create-variant.md   # Добавить новый вариант
├── 03-howto-attach-existing.md  # Привязать существующий айтем
├── 04-howto-reorder-variants.md # Переупорядочить + pre-chosen
├── 05-howto-remove-variant.md   # Удалить вариант (+ логика возврата/исчезновения)
├── 06-reference-rules.md        # Правила: Product Class inheritance, Short Name,
│                                #   POS/Kitchen/Report display, deletion logic
├── 07-reference-glossary.md     # Термины (normalized)
├── 08-known-limitations.md      # Not documented in v1 / out-of-scope
└── _assets/                     # Published screenshots used by the manual
```

### 3.2 Гарантии качества (DoD для всего пакета)

- **Traceability**: 100% утверждений → строка в RTM (timestamp / shot # / SME-answer).
- **Reproducibility**: любой читатель с admin-доступом может повторить каждый how-to шаг-в-шаг.
- **Accuracy**: 0 противоречий; все gap'ы явно маркированы «Not documented in v1».
- **Consistency**: единая терминология, единая структура, единый визуальный стиль.
- **Accessibility (ISO 26514 §8.2)**: alt-тексты скриншотов, H1–H3 без пропусков, plain language.
- **Safe-scope publication**: в body только confirmed behaviour; inferred / unknown — в `08-known-limitations.md`.

### 3.3 Формат публикации (resolved for v1)

V1 публикуется как Markdown-пакет в `docs/manual/` внутри GitHub-репо. Отдельный PDF-export для v1 не требуется.

---

## 4. Repository state before handover

### 4.1 Что уже есть ✅

| Артефакт | Где | Состояние |
|---|---|---|
| Raw video | `docs/video.mp4` | OK |
| Transcript (normalized RU) | `docs/Meeting Recording Transcription.md` | OK |
| Transcript (SRT) | `docs/transcription.srt` | OK |
| Storyboard — film | `docs/narrative_film_storyboard-2026-04-24.md` | 32 shots, RU/EN mix |
| Storyboard — commercial | `docs/product_commercial_storyboard-2026-04-24.md` | 20 shots, EN |
| Cropped screens archive | `docs/screens_cropped/*.png` | 34 frames (`32` original + `2` replacements: `shot_33`, `shot_34`) |
| Final manual | `docs/manual/00-index.md` … `08-known-limitations.md` | Drafted and validated |
| Published screenshot set | `docs/manual/_assets/shot_*.png` | 17 published annotated shots |
| BA traceability pack | `docs/ba-artifacts/*.md` | Filled and cross-linked |

### 4.2 Что осталось до handover ⚙️

| ID | Остаток | Критичность | Как закрывается |
|---|---|:-:|---|
| H1 | Final consistency pass across `manual`, `ba-artifacts`, and spec | 🔴 | Final repo review before commit |
| H2 | Final validation of markdown links, screenshot references, and shot numbering | 🔴 | Automated checks + spot review |
| H3 | Git packaging / handover note | 🟡 | Prepare final commit-ready package |

Phase 1–5 уже выполнены. Остаток — это не исследовательские пробелы, а финальная упаковка и контроль согласованности перед handover.

**Блокеры handover**: H1, H2. Остальное — упаковка.

---

## 5. Step-by-step план (17 шагов, 6 фаз)

### Legenda

- **№** — порядковый
- **Шаг** — что делаем
- **Вход** — что нужно, чтобы начать
- **Артефакт** — что появляется на выходе (файлы с префиксами `01-`…`13-` — это **working artifacts** в `docs/ba-artifacts/`, внутренняя traceability, НЕ финальный мануал; финальный пакет `docs/manual/` описан в §3.1)
- **Метрика / DoD** — как понять, что шаг закрыт

### Phase 1 — Framing & Elicitation (2 шага)

| № | Шаг | Вход | Артефакт | Метрика / DoD |
|:-:|---|---|---|---|
| 1 | **PO Telegram batch + Task Contract** | 4 вопроса из §6 | `docs/ba-artifacts/01-task-contract.md` | Все 5 полей заполнены (audience / format / deadline / scope / non-goals); ответы PO получены или разумные defaults задокументированы |
| 2 | **Glossary v1 + Audience Card** | Transcript, SRT, UI; ответ PO на Q-1 | `docs/ba-artifacts/02-glossary.md`, `docs/ba-artifacts/03-audience.md` | Glossary: ≥15 терминов с definition / source / RU-EN; 0 синонимов без пометок. Audience: primary + secondary persona, prior knowledge, top-3 jobs |

### Phase 2 — Evidence extraction (3 шага)

| № | Шаг | Вход | Артефакт | Метрика / DoD |
|:-:|---|---|---|---|
| 3 | **Observation Log** (frame-by-frame) | Video + storyboards + SRT | `docs/ba-artifacts/04-observation-log.md` | Для каждого user action: timestamp / UI element / visual change / confidence (Fact / Inference / Unknown) |
| 4 | **Feature Capability Map** | Observation Log | `docs/ba-artifacts/05-capability-map.md` | ≥8 capabilities, каждая с trigger / steps / result / preconditions |
| 5 | **Source Reliability Matrix** | Observation Log | `docs/ba-artifacts/06-source-matrix.md` | Каждое утверждение: direct / narrated / inferred; ≥70% direct в confirmed scope |

### Phase 3 — Scope lock & IA (5 шагов)

| № | Шаг | Вход | Артефакт | Метрика / DoD |
|:-:|---|---|---|---|
| 6 | **Scope & Confidence Register** | Capability Map + Source Matrix + ответ PO на Q-3 | `docs/ba-artifacts/07-scope.md` | 3 bucket: in-scope-v1 / conditional / out-of-scope; каждая capability назначена |
| 7 | **Scenario Catalogue** | Scope + Audience | `docs/ba-artifacts/08-scenarios.md` | 5 сценариев (create / attach / reorder / pre-chosen / remove) с trigger + expected result |
| 8 | **Information Architecture (Diátaxis TOC)** | Scenarios + Capability Map | `docs/ba-artifacts/08-ia.md` | TOC для `docs/manual/`; каждый файл назначен в Diátaxis-слот |
| 9 | **Screenshot Shot-list** | Storyboards + IA + screens_cropped | `docs/ba-artifacts/09-shotlist.md` | Для каждого how-to — shot_XX.png + caption; 0 «осиротевших» скринов |
| 10 | **RTM skeleton** | IA + Source Matrix | `docs/ba-artifacts/10-rtm.md` | Строка для каждого TOC-пункта: claim / source / confidence |

### Phase 4 — Drafting (4 шага)

| № | Шаг | Вход | Артефакт | Метрика / DoD |
|:-:|---|---|---|---|
| 11 | **Explanation draft** | IA + Audience + Glossary | `docs/manual/01-explanation.md` | ≤1 страница; 0 step-by-step (только концепт); ≥1 схема |
| 12 | **How-to drafts (×5)** | Scenarios + Shot-list + MS Style | `docs/manual/02-…05-*.md` | Каждый: Goal / Prereqs / Steps (imperative, numbered) / Expected Result; ≤10 шагов; ≥1 скрин |
| 13 | **Reference draft** | Capability Map + self-derived rules | `docs/manual/06-reference-rules.md`, `docs/manual/07-reference-glossary.md` | Таблицы: Short Name, Product Class inheritance, POS/Kitchen/Report display, deletion logic. Glossary — консолидированная версия из `02-glossary.md`. |
| 14 | **Known Limitations draft** | Scope register (out-of-scope bucket) + unresolved gaps | `docs/manual/08-known-limitations.md` | Явный список gap'ов, не покрытых v1 (включая G1, G3, G5, G6, G8 из `plan.md`) |

### Phase 5 — Validation (2 шага)

| № | Шаг | Вход | Артефакт | Метрика / DoD |
|:-:|---|---|---|---|
| 15 | **Internal QA** (ISO 26514 checklist + RTM fill-up) | Draft v1 | `docs/ba-artifacts/11-qa-checklist.md` + filled `docs/ba-artifacts/10-rtm.md` | 100% RTM заполнен; 0 FAIL в 26514; 0 TODO |
| 16 | **Self cognitive walkthrough + consistency pass** | Draft v1 | `docs/ba-artifacts/12-review-log.md` | Сама прохожу 2 сценария по мануалу «как новичок»; фиксирую блоки; все fixes применены |

### Phase 6 — Publishing (1 шаг, условный по Q-2)

| № | Шаг | Вход | Артефакт | Метрика / DoD |
|:-:|---|---|---|---|
| 17 | **Publish & Handover** | Final pack + ответ PO на Q-2 | GitHub репо + ссылка PO (или PDF export) + краткое сопроводительное письмо | Ссылка/файл отправлены; pack содержит все 9 финальных документов |

**Итого**: 17 шагов. Средний вес — полдня. Самая плотная фаза — Drafting (11–14, ≈2 дня).

---

## 6. Четыре вопроса к PO (Maya) — final Telegram-ready version

Отправляется одним сообщением в Telegram (@mayya_pi). Язык — RU (подтверждено пользователем).

```
Привет, Майя! До того, как я начну — 4 коротких вопроса, чтобы мануал попал точно туда, куда тебе нужно:

1. Кто первичный читатель — админ ресторана, настраивающий меню, внутренний support или кто-то ещё? Что он(а) уже знает о Gen1POS к моменту открытия мануала?

2. В каком формате финал — репозиторий на GitHub (пришлю ссылку) или PDF? Есть ли шаблон/стиль других мануалов Gen1POS, которому нужно следовать?

3. Scope v1 — только happy path (create / attach / reorder / pre-chosen / remove), или покрываем и edge-cases (каскадное удаление, многоуровневая вложенность, миграция, скидки на parent vs variant, permissions)? Есть ли дедлайн?

4. Язык мануала — EN, RU или оба?

Спасибо!
```

### Обоснование каждого вопроса (для внутреннего использования, в Telegram не идёт)

| # | Зачем спрашиваем | Что ломается без ответа |
|---|---|---|
| Q-1 | Tone, depth of explanation, выбор примеров | Делаем support-reference вместо admin-how-to или наоборот |
| Q-2 | Структурные ограничения формата + consistency с существующими мануалами | MD-структура может не влезть в целевой шаблон; tone-inconsistency с остальной документацией |
| Q-3 | Scope v1: +50–70% работы на edge-cases или нет; deadline определяет процесс vs shortcut | Scope расплывётся или пропустим то, что для Maya в приоритете |
| Q-4 | Glossary, references, объём работы | EN-only vs RU-only — разные мануалы; bilingual — двойная работа |

---

## 7. Что происходит дальше

1. Завершаем final consistency-pass по `manual`, `ba-artifacts`, и spec.
2. Прогоняем финальную проверку ссылок, шотов и формулировок safe-scope publication.
3. Формируем commit-ready пакет и готовим handover в git.

---

## 8. Логика пересмотра (living document)

Spec ревизуется в следующих случаях:

- PO ответ меняет scope → обновляем §5 Phase 3 + §6.
- Обнаружены новые gap'ы в Phase 2 → §4.2 и §5 Phase 3.
- Изменение методологического стека → §2 с явным обоснованием.

Каждая ревизия — отдельный коммит с описанием «что и почему».
