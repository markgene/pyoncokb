"""Test GenomicChangeAnnotator class with EGFR E746_A750del."""

import unittest

from pyoncokb.annotations.genomicchangeannotator import GenomicChangeAnnotator
from pyoncokb.models.indicatorqueryresp import IndicatorQueryResp
from pyoncokb.models.indicatorquerytreatment import IndicatorQueryTreatment
from pyoncokb.oncokbapi import OncokbApi
from tests.testconfig import TestConfig


class GenomicChangeAnnotatorEgfrE746a750delTestCase(unittest.TestCase):
    """Test GenomicChangeAnnotator class with EGFR E746_A750del."""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        config = TestConfig()
        oncokb_auth = config.get_oncokb_authorization()
        oncokb_api = OncokbApi(auth=oncokb_auth)
        annotator = GenomicChangeAnnotator(
            oncokb_api=oncokb_api,
            genomic_change="7,55242464,55242479,AGGAATTAAGAGAAGC,A",
            ref_genome="GRCh37",
        )
        cls.indicator_query_response = annotator.query()

    def test_allele_exist(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertFalse(self.indicator_query_response.allele_exist)

    def test_query_alteration(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(
                self.indicator_query_response.query.alteration, "E746_A750del"
            )

    def test_query_entrez_gene_id(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(self.indicator_query_response.query.entrez_gene_id, 1956)

    def test_gene_exist(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertTrue(self.indicator_query_response.gene_exist)

    def test_query_hugo_symbol(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(self.indicator_query_response.query.hugo_symbol, "EGFR")

    def test_highest_diagnostic_implication_level(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNone(
                self.indicator_query_response.highest_diagnostic_implication_level
            )

    def test_highest_fda_level(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(
                self.indicator_query_response.highest_fda_level, "LEVEL_Fda2"
            )

    def test_highest_prognostic_implication_level(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNone(
                self.indicator_query_response.highest_prognostic_implication_level
            )

    def test_highest_resistance_level(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNone(self.indicator_query_response.highest_resistance_level)

    def test_highest_sensitive_level(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(
                self.indicator_query_response.highest_sensitive_level, "LEVEL_1"
            )

    def test_hotspot(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertTrue(self.indicator_query_response.hotspot)

    def test_mutation_effect_known_effect(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(
                self.indicator_query_response.mutation_effect.known_effect,
                "Gain-of-function",
            )

    def test_oncogenic(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(self.indicator_query_response.oncogenic, "Oncogenic")

    def test_query_tumor_type(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNone(self.indicator_query_response.query.tumor_type)

    def test_tumor_type_summary(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertEqual(self.indicator_query_response.tumor_type_summary, "")

    def test_variant_exist(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertTrue(self.indicator_query_response.variant_exist)

    def test_vus(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertFalse(self.indicator_query_response.vus)

    def test_treatments(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNotNone(self.indicator_query_response.treatments)
            for treatment in self.indicator_query_response.treatments:
                self.assertTrue(isinstance(treatment, IndicatorQueryTreatment))

    def test_summarize_treatments_of_level_1(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNotNone(self.indicator_query_response.treatments)
            treatments_level_1 = (
                self.indicator_query_response.summarize_treatments_of_level_1()
            )
            self.assertGreaterEqual(len(treatments_level_1), 6)

    def test_summarize_treatments_of_level_1_have_fields(self):
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNotNone(self.indicator_query_response.treatments)
            treatments_level_1 = (
                self.indicator_query_response.summarize_treatments_of_level_1()
            )
            for treatment in treatments_level_1:
                self.check_treatment(treatment)

    def test_summarize_treatments_of_level_2(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNotNone(self.indicator_query_response.treatments)
            treatments_level_2 = (
                self.indicator_query_response.summarize_treatments_of_level_2()
            )
            self.assertGreaterEqual(len(treatments_level_2), 0)

    def test_summarize_treatments_of_level_r1(self):
        self.assertTrue(isinstance(self.indicator_query_response, IndicatorQueryResp))
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNotNone(self.indicator_query_response.treatments)
            treatments_level_r1 = (
                self.indicator_query_response.summarize_treatments_of_level_r1()
            )
            self.assertEqual(len(treatments_level_r1), 0)

    def check_treatment(self, treatment: dict):
        self.assertTrue("alterations" in treatment)
        self.assertTrue("approved_indications" in treatment)
        self.assertTrue("description" in treatment)
        self.assertTrue("drug_names" in treatment)
        self.assertTrue("pmids" in treatment)
        self.assertTrue("level" in treatment)
        self.assertTrue("level_associated_cancer_type_name" in treatment)

    def test_treatments_level_1_has_a_specific_treatment(self):
        flag = False
        if isinstance(self.indicator_query_response, IndicatorQueryResp):
            self.assertIsNotNone(self.indicator_query_response.treatments)
            treatments_level_1 = (
                self.indicator_query_response.summarize_treatments_of_level_1()
            )
            for treatment in treatments_level_1:
                if (
                    treatment["level_associated_cancer_type_name"]
                    == 'Non-Small Cell Lung Cancer'
                    and treatment["approved_indications"]
                    == 'Erlotinib is FDA-approved for (1) First-line treatment of metastatic non-small cell lung cancer with EGFR exon 19 deletions or exon 21 (L858R) substitution mutations as detected by an FDA-approved test, (2) maintenance treatment of non small cell lung cancer (NSCLC) that has stabilized after platinum-based chemotherapy, (3) locally advanced or metastatic NSCLC after failure of chemotherapy.'
                ):
                    flag = True
                    break
        self.assertTrue(flag)
