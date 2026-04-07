---
name: 📚 Content Request
description: Request new subjects, topics, or content packs
title: "[Content]: "
labels: ["content"]
body:
  - type: markdown
    attributes:
      value: |
        Want a new subject added to kslearn? Tell us what you need!

  - type: input
    id: subject
    attributes:
      label: Subject / Category
      description: What subject should we add?
      placeholder: "e.g., Organic Chemistry, World History, Guitar Theory"
    validations:
      required: true

  - type: dropdown
    id: level
    attributes:
      label: Difficulty Level
      options:
        - Beginner
        - Intermediate
        - Advanced
        - Mixed (all levels)
    validations:
      required: true

  - type: textarea
    id: topics
    attributes:
      label: Specific Topics
      description: List the topics you'd like covered.
      value: |
        - Topic 1
        - Topic 2
        - Topic 3

  - type: checkboxes
    id: content-types
    attributes:
      label: Content Types Needed
      options:
        - label: Study Notes
        - label: Quiz Questions
        - label: Flashcards
        - label: Tutorials
        - label: All of the above

  - type: textarea
    id: details
    attributes:
      label: Details
      description: Any specific syllabus, curriculum, or references?

  - type: input
    id: source
    attributes:
      label: Source / Reference
      description: Link to syllabus, textbook, or curriculum if available.
