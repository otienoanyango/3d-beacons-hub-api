# generated by datamodel-codegen:
#   filename:  3dbeacons.yaml
#   timestamp: 2022-05-13T10:29:41+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class UniprotEntry(BaseModel):
    ac: str = Field(..., description="UniProt accession", example="P00520")
    id: Optional[str] = Field(
        None, description="UniProt identifier", example="ABL1_MOUSE"
    )
    uniprot_checksum: Optional[str] = Field(
        None,
        description="CRC64 checksum of the UniProt sequence",
        example="5F9BA1D4C7DE6925",
    )
    sequence_length: Optional[int] = Field(
        None, description="Length of the UniProt sequence", example=76
    )
    segment_start: Optional[int] = Field(
        None,
        description="1-indexed first residue of the UniProt sequence segment",
        example=1,
    )
    segment_end: Optional[int] = Field(
        None,
        description="1-indexed last residue of the UniProt sequence segment",
        example=86,
    )
    description: Optional[str] = Field(
        None,
        description="Description of the UniProt entry",
        example="Proto-oncogene tyrosine-protein kinase ABL1",
    )


class PdbEntry(BaseModel):
    entry_id: str = Field(..., description="PDB entry identifier", example="3bow")
    chain_id: str = Field(..., description="PDB chain identifier", example="A")
    mapped_uniprot: Optional[str] = Field(
        None, description="UniProt accession mapped to the PDB entry", example="P12345"
    )
    uniprot_start: int = Field(
        ..., description="1-indexed first residue in the mapped UniProt", example=1
    )
    uniprot_end: int = Field(
        ..., description="1-indexed last residue in the mapped UniProt", example=100
    )


class ModelCategory(Enum):
    EXPERIMENTALLY_DETERMINED = "EXPERIMENTALLY DETERMINED"
    TEMPLATE_BASED = "TEMPLATE-BASED"
    AB_INITIO = "AB-INITIO"
    CONFORMATIONAL_ENSEMBLE = "CONFORMATIONAL ENSEMBLE"


class ModelFormat(Enum):
    PDB = "PDB"
    MMCIF = "MMCIF"
    BCIF = "BCIF"


class ModelType(Enum):
    ATOMIC = "ATOMIC"
    DUMMY = "DUMMY"
    MIX = "MIX"


class EnsembleSampleFormat(Enum):
    PDB = "PDB"
    MMCIF = "MMCIF"
    BCIF = "BCIF"


class ExperimentalMethod(Enum):
    ELECTRON_CRYSTALLOGRAPHY = "ELECTRON CRYSTALLOGRAPHY"
    ELECTRON_MICROSCOPY = "ELECTRON MICROSCOPY"
    EPR = "EPR"
    FIBER_DIFFRACTION = "FIBER DIFFRACTION"
    FLUORESCENCE_TRANSFER = "FLUORESCENCE TRANSFER"
    INFRARED_SPECTROSCOPY = "INFRARED SPECTROSCOPY"
    NEUTRON_DIFFRACTION = "NEUTRON DIFFRACTION"
    X_RAY_POWDER_DIFFRACTION = "X-RAY POWDER DIFFRACTION"
    SOLID_STATE_NMR = "SOLID-STATE NMR"
    SOLUTION_NMR = "SOLUTION NMR"
    X_RAY_SOLUTION_SCATTERING = "X-RAY SOLUTION SCATTERING"
    THEORETICAL_MODEL = "THEORETICAL MODEL"
    X_RAY_DIFFRACTION = "X-RAY DIFFRACTION"
    HYBRID = "HYBRID"


class ConfidenceType(Enum):
    pLDDT = "pLDDT"
    QMEANDisCo = "QMEANDisCo"
    ipTMPlusPTM = "ipTM+pTM"


class OligomericState(Enum):
    MONOMER = "MONOMER"
    HOMODIMER = "HOMODIMER"
    HETERODIMER = "HETERODIMER"
    HOMO_OLIGOMER = "HOMO-OLIGOMER"
    HETERO_OLIGOMER = "HETERO-OLIGOMER"


class EntityType(Enum):
    BRANCHED = "BRANCHED"
    MACROLIDE = "MACROLIDE"
    NON_POLYMER = "NON-POLYMER"
    POLYMER = "POLYMER"
    WATER = "WATER"


class EntityPolyType(Enum):
    CYCLIC_PSEUDO_PEPTIDE = "CYCLIC-PSEUDO-PEPTIDE"
    PEPTIDE_NUCLEIC_ACID = "PEPTIDE NUCLEIC ACID"
    POLYDEOXYRIBONUCLEOTIDE = "POLYDEOXYRIBONUCLEOTIDE"
    POLYDEOXYRIBONUCLEOTIDE_POLYRIBONUCLEOTIDE_HYBRID = (
        "POLYDEOXYRIBONUCLEOTIDE/POLYRIBONUCLEOTIDE HYBRID"
    )
    POLYPEPTIDE_D_ = "POLYPEPTIDE(D)"
    POLYPEPTIDE_L_ = "POLYPEPTIDE(L)"
    POLYRIBONUCLEOTIDE = "POLYRIBONUCLEOTIDE"
    OTHER = "OTHER"


class IdentifierCategory(Enum):
    UNIPROT = "UNIPROT"
    RFAM = "RFAM"
    CCD = "CCD"
    SMILES = "SMILES"
    INCHI = "INCHI"
    INCHIKEY = "INCHIKEY"


class Entity(BaseModel):
    entity_type: EntityType = Field(
        ...,
        description="The type of the molecular entity; similar to _entity.type in"
        " mmCIF",
        example="POLYMER",
    )
    entity_poly_type: Optional[EntityPolyType] = Field(
        None,
        description="The type of the molecular entity; similar to _entity_poly.type"
        " in mmCIF",
        example="PEPTIDE NUCLEIC ACID",
    )
    identifier: Optional[str] = Field(
        None, description="Identifier of the molecule", example="Q13033"
    )
    identifier_category: Optional[IdentifierCategory] = Field(
        None, description="Category of the identifier", example="UNIPROT"
    )
    description: str = Field(
        ..., description="A textual label of the molecule", example="Striatin-3"
    )
    chain_ids: List[str] = Field(
        ...,
        description="A list of label_asym identifiers "
        "( chain_id in the case of PDB format) of the molecule",
        example=["A", "B"],
    )


class SummaryItems(BaseModel):
    model_identifier: str = Field(
        ..., description="Identifier of the model, such as PDB id", example="8kfa"
    )
    model_category: ModelCategory = Field(
        ..., description="Category of the model", example="TEMPLATE-BASED"
    )
    model_url: str = Field(
        ...,
        description="URL of the model coordinates",
        example="https://www.ebi.ac.uk/pdbe/static/entry/1t29_updated.cif",
    )
    model_format: ModelFormat = Field(
        ..., description="File format of the coordinates", example="MMCIF"
    )
    model_type: Optional[ModelType] = Field(
        None,
        description="Defines if the coordinates are atomic-level or contains "
        "dummy atoms (e.g. SAXS models), or a mix of both (e.g. hybrid models)\n",
        example="ATOMIC",
    )
    model_page_url: Optional[str] = Field(
        None,
        description="URL of a web page of the data provider that show the model",
        example="https://alphafold.ebi.ac.uk/entry/Q5VSL9",
    )
    provider: str = Field(
        ..., description="Name of the model provider", example="SWISS-MODEL"
    )
    number_of_conformers: Optional[float] = Field(
        None,
        description="The number of conformers in a conformational ensemble",
        example=42,
    )
    ensemble_sample_url: Optional[str] = Field(
        None,
        description="URL of a sample of conformations from a conformational "
        "ensemble",
        example="https://proteinensemble.org/api/ensemble_sample/PED00001e001",
    )
    ensemble_sample_format: Optional[EnsembleSampleFormat] = Field(
        None,
        description="File format of the sample coordinates, e.g. PDB",
        example="PDB",
    )
    created: str = Field(
        ...,
        description="Date of release of model generation in the format of YYYY-MM-DD",
        example="2021-12-21",
    )
    sequence_identity: float = Field(
        ...,
        description="Sequence identity in the range of [0,1] of the model to the "
        "UniProt sequence\n",
        example=0.97,
    )
    uniprot_start: int = Field(
        ...,
        description="1-indexed first residue of the model according to UniProt "
        "sequence numbering\n",
        example=1,
    )
    uniprot_end: int = Field(
        ...,
        description="1-indexed last residue of the model according to UniProt "
        "sequence numbering\n",
        example=142,
    )
    coverage: float = Field(
        ...,
        description="Fraction in range of [0, 1] of the UniProt sequence covered by "
        "the model.  This is calculated as (uniprot_end - uniprot_start + 1) / "
        "uniprot_sequence_length\n",
        example=0.4,
    )
    experimental_method: Optional[ExperimentalMethod] = Field(
        None,
        description="Experimental method used to determine the structure, if "
        "applicable",
    )
    resolution: Optional[float] = Field(
        None,
        description="The resolution of the model in Angstrom, if applicable",
        example=1.4,
    )
    confidence_type: Optional[ConfidenceType] = Field(
        None,
        description="Type of the confidence measure. This is required for  "
        "theoretical models.\n",
        example="QMEANDisCo",
    )
    confidence_version: Optional[str] = Field(
        None,
        description="Version of confidence measure software used to calculate quality. "
        "This is required for theoretical models.\n",
        example="v1.0.2",
    )
    confidence_avg_local_score: Optional[float] = Field(
        None,
        description="Average of the confidence measures in the range of [0,1] for "
        "QMEANDisCo  and [0,100] for pLDDT. Please contact 3D-Beacons developers "
        "if other  estimates are to be added. This is required for theoretical "
        "models.\n",
        example=0.95,
    )
    oligomeric_state: Optional[OligomericState] = Field(
        None, description="Oligomeric state of the model", example="MONOMER"
    )
    oligomeric_state_confidence: Optional[float] = Field(
        None,
        description="Numerical value that describes the confidence in the oligomeric "
        "state of the predicted complex",
        example=0.4603,
    )
    preferred_assembly_id: Optional[str] = Field(
        None,
        description="Identifier of the preferred assembly in the model",
        example="1A",
    )
    entities: List[Entity] = Field(
        ..., description="A list of molecular entities in the model"
    )


class ExperimentalMethod1(Enum):
    ELECTRON_CRYSTALLOGRAPHY = "ELECTRON CRYSTALLOGRAPHY"
    ELECTRON_MICROSCOPY = "ELECTRON MICROSCOPY"
    EPR = "EPR"
    FIBER_DIFFRACTION = "FIBER DIFFRACTION"
    FLUORESCENCE_TRANSFER = "FLUORESCENCE TRANSFER"
    INFRARED_SPECTROSCOPY = "INFRARED SPECTROSCOPY"
    NEUTRON_DIFFRACTION = "NEUTRON DIFFRACTION"
    POWDER_DIFFRACTION = "POWDER DIFFRACTION"
    SOLID_STATE_NMR = "SOLID-STATE NMR"
    SOLUTION_NMR = "SOLUTION NMR"
    SOLUTION_SCATTERING = "SOLUTION SCATTERING"
    THEORETICAL_MODEL = "THEORETICAL MODEL"
    X_RAY_DIFFRACTION = "X-RAY DIFFRACTION"
    HYBRID = "HYBRID"


class Template(BaseModel):
    template_id: str = Field(
        ..., description="Identifier of the template", example="2aqa"
    )
    chain_id: str = Field(
        ...,
        description="Identifier of the chain of the template; this is label_asym_id in "
        "mmCIF",
        example="C",
    )
    template_sequence_identity: float = Field(
        ...,
        description="Sequence identity of the template with the  UniProt accession, "
        "in the range of [0,1]\n",
        example=0.97,
    )
    last_updated: str = Field(
        ...,
        description="Date of release of the last update in  the format of YYYY-MM-DD\n",
        example="2021-08-06",
    )
    provider: str = Field(..., description="Provider of the template", example="PDB")
    experimental_method: ExperimentalMethod1 = Field(
        ...,
        description="Experimental method used to determine the template",
        example="HYBRID",
    )
    resolution: float = Field(
        ..., description="Resolution of the template, in Angstrom", example=2.1
    )
    preferred_assembly_id: Optional[str] = Field(
        None,
        description="Identifier of the preferred assembly of the template",
        example="1",
    )


class Seqres(BaseModel):
    aligned_sequence: str = Field(
        ..., description="Sequence of the model", example="AAGTGHLKKKYT..."
    )
    from_: int = Field(
        ..., alias="from", description="1-indexed first residue", example=32
    )
    to: int = Field(..., description="1-indexed last residue", example=976)


class Uniprot(BaseModel):
    aligned_sequence: str = Field(
        ...,
        description="Sequence of the UniProt accession",
        example="AAGTGHLKKKYTAAGTGHLKKKYT...",
    )
    from_: int = Field(
        ..., alias="from", description="1-indexed first residue", example=23
    )
    to: int = Field(..., description="1-indexed last residue", example=868)


class Residue(BaseModel):
    confidence: Optional[float] = Field(
        None, description="Confidence score in the range of [0,1]", example=0.99
    )
    model_residue_label: int = Field(..., description="Model residue index", example=1)
    uniprot_residue_number: int = Field(
        ..., description="UniProt residue index", example=1
    )


class Segment(BaseModel):
    templates: Optional[List[Template]] = Field(
        None, description="Information on the template(s) used for the model"
    )
    seqres: Seqres = Field(..., description="Information on the sequence of the model")
    uniprot: Uniprot
    residues: List[Residue]


class Chain(BaseModel):
    chain_id: str
    segments: Optional[List[Segment]] = None


class Chains(BaseModel):
    __root__: List[Chain]


class LigandItem(BaseModel):
    id: str = Field(..., description="Three-letter code of the ligand", example="IHP")
    name: str = Field(
        ..., description="Name of the small ligand", example="INOSITOL HEXAKISPHOSPHATE"
    )
    formula: str = Field(
        ...,
        description="Chemical composition formula of the ligand",
        example="C6 H18 O24 P6",
    )
    inchikey: str = Field(
        ..., description="InChIKey of the ligand", example="IMQLKJBTEOYOSI-GPIVLXJGSA-N"
    )


class Type(Enum):
    HELIX = "HELIX"
    SHEET = "SHEET"
    COIL = "COIL"


class RegionItem(BaseModel):
    start: int = Field(
        ..., description="The first position of the annotation", example=23
    )
    end: int = Field(..., description="The last position of the annotation", example=42)


class SecondaryStructureItem(BaseModel):
    type: Type = Field(
        ..., description="Type of the secondary structure element", example="HELIX"
    )
    region: Optional[List[RegionItem]] = None


class Type1(Enum):
    CARBOHYD = "CARBOHYD"
    DOMAIN = "DOMAIN"
    CA_BIND = "CA_BIND"
    DNA_BIND = "DNA_BIND"
    NP_BIND = "NP_BIND"
    ACT_SITE = "ACT_SITE"
    METAL = "METAL"
    BINDING = "BINDING"
    NON_STD = "NON_STD"
    MOD_RES = "MOD_RES"
    DISULFID = "DISULFID"
    MUTAGEN = "MUTAGEN"


class Region(BaseModel):
    start: int = Field(
        ..., description="The first position of the annotation", example=23
    )
    end: int = Field(..., description="The last position of the annotation", example=42)


class FeatureItem(BaseModel):
    type: Type1 = Field(..., description="Type of the annotation", example="ACT_SITE")
    description: str = Field(
        ...,
        description="Description/Label of the annotation",
        example="Pfam N1221 (PF07923)",
    )
    residues: Optional[List[int]] = Field(
        None, description="An array of residue indices"
    )
    regions: Optional[List[Region]] = None


class Annotations(BaseModel):
    accession: str = Field(..., description="A UniProt accession", example="P00734")
    id: Optional[str] = Field(
        None, description="A UniProt identifier", example="FGFR2_HUMAN"
    )
    sequence: str = Field(
        ..., description="The sequence of the protein", example="AFFGVAATRKL"
    )
    ligand: Optional[List[LigandItem]] = Field(
        None, description="Contains ligand annotations"
    )
    secondary_structure: Optional[List[SecondaryStructureItem]] = None
    feature: Optional[List[FeatureItem]] = None


class MappingAccessionType(Enum):
    uniprot = "uniprot"
    pfam = "pfam"


class ModelCategory1(Enum):
    EXPERIMENTALLY_DETERMINED = "EXPERIMENTALLY DETERMINED"
    TEMPLATE_BASED = "TEMPLATE-BASED"
    AB_INITIO = "AB-INITIO"
    CONFORMATIONAL_ENSEMBLE = "CONFORMATIONAL ENSEMBLE"
    DEEP_LEARNING = "DEEP-LEARNING"


class ModelType1(Enum):
    single = "single"
    complex = "complex"


class Metadata(BaseModel):
    mappingAccession: str = Field(
        ...,
        description="Accession/identifier of the entity the model is mapped to",
        example="P38398",
    )
    mappingAccessionType: MappingAccessionType = Field(
        ...,
        description="The name of the data provider the model is mapped to",
        example="uniprot",
    )
    start: int = Field(
        ...,
        description="The index of the first residue of the model according to the "
        "mapping",
        example=1,
    )
    end: int = Field(
        ...,
        description="The index of the last residue of the model according to the "
        "mapping",
        example=103,
    )
    modelCategory: ModelCategory1 = Field(
        ..., description="Category of the model", example="TEMPLATE-BASED"
    )
    modelType: ModelType1 = Field(
        ..., description="Monomeric or complex strutures", example="single"
    )


class Detailed(BaseModel):
    summary: SummaryItems
    chains: Chains


class Overview(BaseModel):
    summary: SummaryItems


class UniprotSummary(BaseModel):
    uniprot_entry: Optional[UniprotEntry] = None
    structures: Optional[List[Overview]] = None


class UniprotDetails(BaseModel):
    uniprot_entry: Optional[UniprotEntry] = None
    structures: Optional[List[Detailed]] = None


class PdbSummary(BaseModel):
    uniprot_entry: Optional[PdbEntry] = None
    structures: Optional[List[Overview]] = None


class AccessionListRequest(BaseModel):
    accessions: List[str] = Field(
        ..., description="A list of UniProt accessions", example=["P00734", "P38398"]
    )
    provider: str = Field(
        None, description="Name of the model provider", example="swissmodel"
    )
    exclude_provider: Optional[str] = Field(
        None, description="Provider to exclude.", example="pdbe"
    )
