"""
docs2llm - Extract documentation from GitHub repositories for use with LLMs.

This package provides functionality to extract documentation from GitHub repositories
and format it for use as context with large language models.
"""

from docs2llm.main import (
    extract_documentation,
    setup_logging,
    is_documentation_file,
    markdown_to_text,
    clone_repository,
    find_documentation_files,
    process_documentation_files
)

__version__ = "0.1.0"
