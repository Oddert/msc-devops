# Plan

- Introduction
- DevOps Strategy
- Pipeline Implementation
- Appraisal & Reflection

## DevOps Lifecycle

- Discover
- Plan
  - Define Requirements
  - Set Objectives
  - Backlog create & prioritise
- Develop
  - Deployment
  - Version Control
  - Automatic reviews & static testing
- Build
  - Automated builds
  - Automated tests
  - Continuos Feedback
- Test
  - Integration & System Testing
  - E2E testing
  - Shift-left security (vulnerability scans)
- Delivery
  - Package & Versioning
  - Deploy to staging
  - Manual approvals
- Deploy
  - Production deployment
  - Auto-rollback
  - Feature Flags
- Operate / Observe
  - Monitor performance & Availability
  - Log Analysis
  - Alerting
- Continuos Feedback
  - User & system feedback
  - Post-mortem analysis
  - Iterate & improve

## Notes

- something else under "automate"?
  - automated commit checks
- can do something with log analysis
- what about feedback? Auto-triage?
- Specific deploy feedback from Spinnaker, ArgoCD?

## Napkin

- Intro
- DevOps Strategy
  - Combined tool, process, architecture defence + describing stages
    - Feedback driven development
      - SDD, TDD
      - Communication etc
    - Continuos integration
    - Verification (testing)
    - IAC
    - Deployment (versioning)
- Pipeline details
- Appraise

## Dev Ops Principles

- Collaboration
- Communication
- Automation
- Continuous Improvement
- Continuous Delivery
- Continuous feedback
- Customer centric action / customer centric decision making
- Create with the end in mind
- Data based decision making
- Learn from mistakes
- Shared goals & responsibility / Responsibility through the cycle
- Infrastructure as code
- Monitoring & Logging
- Agile principles
- Security Integration DevSecOps
- Version control
- Testing

## Dev Ops Principle Map

- Collaboration
  - Monorepo for combined issues
  - Spec driven development
  - Standards enforcement (ruff, spectral)
- Communication
  - Docs in code
- Automation
  - Scheduled cleanup
- Continuous Integration
  - tests after merge to development
  - feature flags
- Continuous Delivery
  - Hands-off deployment
- Continuous feedback
- Customer centric action / customer centric decision making
- Create with the end in mind
- Data based decision making
- Learn from mistakes
- Shared goals & responsibility / Responsibility through the cycle
- IAC: Infrastructure as code
  - Terraform
  - Containers
  - Abelic to include DB in code
- Monitoring & Logging
  - AWS cloudwatch
- Agile principles
- Security Integration DevSecOps
  - OPA gate
- Version control
  - Build IDs
  - Container version numbers
  - Code signing
- Testing
  - Unit, Integration, Regression

### Simplified

- Collaboration
  - Agile methodology
  - Contribution standards
    - Code lint
    - Commit lint
    - Shared environment settings
  - Docs in code
  - Monorepo for contract alignment
- Communication & feedback
  - User centrality
    - Feedback loops
    - Immediate visibility
  - Data driven development
  - Shared responsibility
- CI
  - Frequent merges, immediate deploy to dev
  - Testing after integration
  - Stale branch detection
  - Feature flags
    - Branch by abstraction
- CD
  - Automation
    - Github Actions
  - Canary releases, Auto rollback
  - terraform dry-run
  - ? Version Control
    - Build IDs
    - Container version numbers
- Observability
  - Learn from mistakes
  - Monitoring
  - Logging
  - Alerts
- Security / DevSecOps
  - OPA gate
    - Git ops
  - Code signing
  - Dep check & other static tests
- Testing
  - Unit, Integration, Regression
  - Contract testing Spectral & Dredd
  - Static (continually run)
- IAC
  - Terraform
  - Containerisation
  - DB migrations

- E2E Responsibility

## Possible Repetitions

- is point adequately made about 'security throughout' in assessment?
- between Containerisation and Automatic Deployments
- version control within CICD section
- time to action a report
- effect of 'pat on the back' on developers
- LLM PR review effectiveness
- quality of logging

## Can Get A Source

- Noisy notifications
- Documentation quality
- Usefulness of linters
- Database schema stability
- versioning static assets

## Unverified Claims

- Full stack mindset
- CI daily merge
- l1 support
- DORA, TMMi
- team effectiveness re DORA and CI
