---
name: 🐛 Bug Report
description: Report a bug or unexpected behavior
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to report a bug! Please fill out the details below.

  - type: dropdown
    id: platform
    attributes:
      label: Platform
      description: Where are you running kslearn?
      options:
        - Termux (Android)
        - Linux
        - macOS
        - Windows
    validations:
      required: true

  - type: input
    id: python-version
    attributes:
      label: Python Version
      description: Run `python --version` to check
      placeholder: "e.g., 3.11.5"
    validations:
      required: true

  - type: input
    id: kslearn-version
    attributes:
      label: kslearn Version
      description: Run `kslearn --version` to check
      placeholder: "e.g., 1.0.0"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: What happened?
      description: A clear and concise description of the bug.
      placeholder: "When I press 2 for quiz, the app crashes..."
    validations:
      required: true

  - type: textarea
    id: reproduce
    attributes:
      label: Steps to Reproduce
      description: How can we reproduce this?
      value: |
        1. Go to '...'
        2. Select '...'
        3. See error
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
      description: What did you expect to happen?
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Error Output
      description: Paste any error messages or tracebacks.
      render: shell

  - type: textarea
    id: additional
    attributes:
      label: Additional Context
      description: Screenshots, config files, or any other info.
