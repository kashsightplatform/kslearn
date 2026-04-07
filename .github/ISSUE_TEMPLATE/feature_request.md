---
name: 💡 Feature Request
description: Suggest a new feature or improvement
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Got an idea to make kslearn better? Share it below!

  - type: textarea
    id: problem
    attributes:
      label: Is your feature request related to a problem?
      description: Describe the problem you're trying to solve.
      placeholder: "I'm always frustrated when..."

  - type: textarea
    id: solution
    attributes:
      label: Describe the solution you'd like
      description: What do you want to happen?
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Describe alternatives you've considered
      description: Any other solutions or workarounds?

  - type: dropdown
    id: type
    attributes:
      label: Feature Type
      options:
        - New learning mode
        - UI improvement
        - New content type
        - Settings/Config
        - AI/Chat
        - Performance
        - Other
    validations:
      required: true

  - type: textarea
    id: additional
    attributes:
      label: Additional Context
      description: Mockups, examples, or references.
