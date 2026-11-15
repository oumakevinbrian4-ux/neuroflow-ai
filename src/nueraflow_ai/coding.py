"""Safe coding-agent boundary. Execution is intentionally not implemented in v0.1."""

from dataclasses import dataclass


@dataclass(frozen=True)
class CodeProposal:
    language: str
    code: str
    explanation: str
    tests_to_run: tuple[str, ...] = ()


class CodingAgent:
    """Stores proposed code; a future runner must use an isolated sandbox."""

    def review_boundary(self, proposal: CodeProposal) -> str:
        if not proposal.code.strip():
            raise ValueError("A code proposal cannot be empty")
        return (
            f"Proposal received ({proposal.language}). "
            "Review it before use; execution is disabled until a sandbox is configured."
        )
