"""Annotate mutation by protein changse POST method.

API point: /annotate/mutations/byProteinChange
"""

from pyoncokb.oncokbapi import OncokbApi
from .batchannotator import BatchAnnotator


class ProteinChangesAnnotator(BatchAnnotator):
    """Batch annotator for protein changes."""
    def __init__(self, oncokb_api: OncokbApi, protein_changes: list):
        service_url = "/annotate/mutations/byProteinChange"
        super().__init__(
            oncokb_api=oncokb_api, service_url=service_url, variants=protein_changes
        )
        self.check_variants_format()

    def check_variants_format(self):
        """Check variants of protein changes is in the good format."""
        protein_changes = self.variants
        assert isinstance(protein_changes, list)
        for elm in protein_changes:
            assert isinstance(elm, dict)
            assert "referenceGenome" in elm
            assert "alteration" in elm
            assert "gene" in elm
            assert isinstance(elm["gene"], dict)
            assert "hugoSymbol" in elm["gene"]
