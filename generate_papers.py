#!/usr/bin/env python3
"""
Generate Hugo markdown files from Zotero BibTeX export.
"""

import re
import os
from pathlib import Path


def parse_bibtex_entry(entry_text):
    """Parse a single BibTeX entry into a dictionary."""
    data = {}

    # Extract entry type and key
    match = re.match(r'@(\w+)\{([^,]+),', entry_text)
    if match:
        data['entry_type'] = match.group(1)
        data['entry_key'] = match.group(2)

    # Extract fields with proper brace matching
    pos = 0
    while pos < len(entry_text):
        # Find field name
        match = re.search(r'(\w+)\s*=\s*\{', entry_text[pos:])
        if not match:
            break

        field_name = match.group(1)
        start = pos + match.end()

        # Find matching closing brace
        brace_count = 1
        end = start
        while end < len(entry_text) and brace_count > 0:
            if entry_text[end] == '{':
                brace_count += 1
            elif entry_text[end] == '}':
                brace_count -= 1
            end += 1

        if brace_count == 0:
            field_value = entry_text[start:end-1].strip()
            data[field_name] = field_value
            pos = end
        else:
            break

    # Also try pattern for quoted strings
    field_pattern_quoted = r'(\w+)\s*=\s*"([^"]*)\"'
    for match in re.finditer(field_pattern_quoted, entry_text):
        field_name = match.group(1)
        if field_name not in data:  # Don't override brace version
            field_value = match.group(2)
            if field_value:
                data[field_name] = field_value.strip()

    # Also get bare number fields (like year = 2023, month = jan)
    bare_pattern = r'(\w+)\s*=\s*(\w+)(?=\s*[,\n])'
    for match in re.finditer(bare_pattern, entry_text):
        field_name = match.group(1)
        if field_name not in data:
            data[field_name] = match.group(2)

    return data


def clean_latex(text):
    """Remove LaTeX commands and clean text."""
    if not text:
        return ""

    # Remove \textbackslash
    text = text.replace('\\textbackslash', '')

    # Handle math symbols
    text = text.replace('\\%', '%')
    text = re.sub(r'\$<\$', '<', text)
    text = re.sub(r'\$>\$', '>', text)
    text = re.sub(r'\$\\leq\$', '≤', text)
    text = re.sub(r'\$\\geq\$', '≥', text)

    # Handle {{Title Case}} -> Title Case
    text = re.sub(r'\{\{([^}]+)\}\}', r'\1', text)

    # Handle {\"u} -> ü, etc.
    text = re.sub(r'\{\\"u\}', 'ü', text)
    text = re.sub(r'\{\\"o\}', 'ö', text)
    text = re.sub(r'\{\\"a\}', 'ä', text)

    # Handle {\'e} -> é, etc.
    text = re.sub(r'\{\\\'e\}', 'é', text)
    text = re.sub(r'\{\\\'a\}', 'á', text)
    text = re.sub(r'\{\\\'i\}', 'í', text)
    text = re.sub(r'\{\\\'o\}', 'ó', text)
    text = re.sub(r'\{\\\'c\}', 'ć', text)

    # Handle {ø} -> ø
    text = re.sub(r'\{\\o\}', 'ø', text)

    # Remove remaining braces
    text = text.replace('{', '').replace('}', '')

    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def extract_authors(author_string):
    """Extract and format author list."""
    if not author_string:
        return []

    # Split by ' and '
    authors = [a.strip() for a in author_string.split(' and ')]

    # Clean up LaTeX formatting
    authors = [clean_latex(a) for a in authors]

    # Format as "Last, First" if not already
    formatted = []
    for author in authors:
        if ',' in author:
            formatted.append(author)
        else:
            # Try to split first/last name
            parts = author.split()
            if len(parts) >= 2:
                formatted.append(f"{parts[-1]}, {' '.join(parts[:-1])}")
            else:
                formatted.append(author)

    return formatted


def get_paper_url(entry):
    """Extract the paper URL from various possible fields."""
    # Priority: doi > arxiv > howpublished > file

    if 'doi' in entry and entry['doi']:
        return f"https://doi.org/{entry['doi']}"

    if 'eprint' in entry and entry['eprint']:
        return f"https://arxiv.org/abs/{entry['eprint']}"

    if 'howpublished' in entry:
        url = entry['howpublished']
        if url.startswith('http'):
            return url

    # Try to extract from file field (HTML files)
    if 'file' in entry:
        files = entry['file'].split(';')
        for f in files:
            if '.html' in f:
                # This is a local file, we'll skip it
                pass

    return ""


def create_slug(entry):
    """Create a URL-friendly slug for the paper."""
    # Use entry key as base
    slug = entry.get('entry_key', 'unknown')

    # Clean up
    slug = slug.lower()
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')

    return slug


def generate_markdown(entry):
    """Generate Hugo markdown frontmatter and content for a paper."""

    title = clean_latex(entry.get('title', 'Untitled'))
    authors = extract_authors(entry.get('author', ''))
    year = entry.get('year', '2024')  # Default to 2024 if missing

    # Publication info
    publication = entry.get('journal', entry.get('publisher', entry.get('institution', 'Preprint')))
    publication = clean_latex(publication)

    # URLs
    paper_url = get_paper_url(entry)
    arxiv = entry.get('eprint', '')
    doi = entry.get('doi', '')

    # Summary/abstract
    abstract = entry.get('abstract', '')
    if abstract:
        # Truncate to first few sentences for summary (used on listing page)
        sentences = abstract.split('. ')
        summary = '. '.join(sentences[:2]) + '.' if len(sentences) > 1 else abstract
        summary = clean_latex(summary)
        # Clean the full abstract too
        full_abstract = clean_latex(abstract)
    else:
        summary = ""
        full_abstract = ""

    # Create frontmatter and content
    frontmatter = f"""---
title: "{title}"
date: {year}-01-01
draft: false

# Paper metadata
authors: [{', '.join(f'"{a}"' for a in authors)}]
publication: "{publication}"
publication_year: {year}
doi: "{doi}"
arxiv: "{arxiv}"
paper_url: "{paper_url}"

# Taxonomies
deception_types: []
research_areas: []
system_types: []
tags: []

# Summary
summary: "{summary}"
---

## Abstract

{full_abstract if full_abstract else "[Abstract not available]"}

## Summary

[Summary to be written]

## Key Findings

[Key findings to be written]

## Philosophical & CogSci Commentary

[Commentary to be written]
"""

    return frontmatter


def main():
    """Main function to process BibTeX and generate markdown files."""

    bibtex_file = Path(__file__).parent / 'Deception.bib'
    output_dir = Path(__file__).parent / 'content' / 'papers'

    # Read BibTeX file
    with open(bibtex_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into individual entries
    entries = re.split(r'\n(?=@)', content)
    entries = [e.strip() for e in entries if e.strip() and e.strip().startswith('@')]

    print(f"Found {len(entries)} entries in BibTeX file")

    # Parse each entry and generate markdown
    for entry_text in entries:
        entry = parse_bibtex_entry(entry_text)

        if not entry:
            continue

        slug = create_slug(entry)
        markdown = generate_markdown(entry)

        # Write to file
        output_file = output_dir / f"{slug}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        title = clean_latex(entry.get('title', 'Untitled'))
        print(f"Created: {output_file.name} - {title}")

    print(f"\nGenerated {len(entries)} markdown files in {output_dir}")


if __name__ == '__main__':
    main()
