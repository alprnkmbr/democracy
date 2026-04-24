#!/usr/bin/env python3
"""
Clean raw data files: remove all commentary, evaluative labels, and interpretive notes.
Keep only: numbers, booleans, verifiable institutional descriptors, and methodological clarifications.
Move removed content to analysis files.
"""
import json
import os
import copy

DATA_DIR = "/Users/claudius/clawd/democracy-pulse/data/raw"
ANALYSIS_DIR = "/Users/claudius/clawd/democracy-pulse/analysis"

# Evaluative adjectives/phrases that signal commentary, not data
EVALUATIVE_TERMS = {
    "strong", "weak", "very strong", "very weak", "high", "low", "moderate",
    "minimal", "comprehensive", "generous", "robust", "severe", "nominal",
    "declining", "polarized", "fragmented", "mixed", "thin", "growing",
    "limited", "extensive", "significant", "critical", "among highest",
    "among lowest", "effectively none", "present but fragile"
}

# Fields that are structural/factual descriptors — keep if verifiable
# These describe institutional mechanisms, not quality judgments
STRUCTURAL_FIELDS = {
    "government_type", "head_of_state_selection", "sovereignty_origin",
    "head_of_state_formal_powers"
}

# Fields that must be null/number/boolean — never free text
MUST_BE_QUANTITATIVE = {
    "community_organization", "volunteering_rate", "family_stability",
    "domestic_violence_severity", "score", "mobility_note",
    "social_safety_net", "refugee_policy", "healthcare_access",
    "housing_security", "food_security", "education_access",
    "judicial_independence", "due_process", "political_imprisonment",
    "bodily_autonomy", "government_transparency", "scientific_integrity",
    "censorship", "labor_protections", "mutual_aid_networks", "community_support",
    "broadcast_licensing_process", "media_regulator_independence",
    "digital_surveillance_legislation", "data_retention_laws",
    "foreign_ownership_restrictions", "net_neutrality_legislation",
    "constitutional_right_to_internet", "digital_id_system_scope",
    "biometric_data_legislation", "right_to_be_forgotten_legislation",
    "defamation_prison_sentences_exists", "media_subsidies_exist",
    "inheritance_estate_tax_exists", "participatory_budgeting_exists",
    "assembly_law_restrictions", "legal_right_to_protest",
    "protest_permit_required", "encrypted_messaging_restrictions",
    "platform_bans_or_restrictions", "independent_news_sites_blocked",
    "swf_note", "tax_to_gdp_note", "social_protection_note",
    "infrastructure_note", "equal_access_note", "sami_rights_note"
}

# Fields that are purely commentary/note fields — remove entirely
COMMENTARY_FIELDS = {
    "source_notes", "gst_specific_observations", "gst_assessment",
    "atomization_level", "capture_level", "mutual_aid", "regional_disparity",
    "mass_incarceration"
}


def is_evaluative(value):
    """Check if a string value contains evaluative judgment."""
    if not isinstance(value, str):
        return False
    lower = value.lower().strip()
    # Check for evaluative adjective at start
    first_word = lower.split()[0] if lower.split() else ""
    if first_word.rstrip("—").rstrip(",") in EVALUATIVE_TERMS:
        return True
    # Check for evaluative patterns
    patterns = ["among highest", "among lowest", "effectively none", "not universal",
                 "crisis", "major compassion", "critical gst"]
    for p in patterns:
        if p in lower:
            return True
    return False


def is_methodological_note(note_text):
    """Check if a note is purely methodological (allowed) vs interpretive (not allowed)."""
    if not isinstance(note_text, str):
        return False
    lower = note_text.lower()
    # Methodological: explains methodology differences, source coverage
    methodological_phrases = [
        "uses different methodology", "both included for comparability",
        "methodology differs", "not in standard", "does not report to"
    ]
    for phrase in methodological_phrases:
        if phrase in lower:
            return True
    return False


def clean_field(key, value, path, removed):
    """Clean a single field value. Returns (cleaned_value, removed_content)."""
    if value is None:
        return None, None

    # Commentary fields — remove entirely
    if key in COMMENTARY_FIELDS:
        if value and value != {"note": "GST analysis to be performed separately from data collection"}:
            removed.append((path, key, value))
        if key == "gst_specific_observations":
            return None, None  # Remove entire key
        return None, None

    # Confidence-flagged objects
    if isinstance(value, dict) and ("confidence" in value or "value" in value):
        new_obj = {}
        for k, v in value.items():
            if k == "note":
                if is_methodological_note(v):
                    new_obj[k] = v  # Keep methodological notes
                else:
                    removed.append((path, f"{key}.note", v))
                    # Don't keep interpretive notes
            else:
                new_obj[k] = v
        return new_obj if new_obj else None, None

    # Free-text evaluative fields
    if key in MUST_BE_QUANTITATIVE:
        if isinstance(value, str):
            # Some structural descriptors are factual
            if key in {"broadcast_licensing_process", "media_regulator_independence",
                       "digital_id_system_scope", "digital_surveillance_legislation",
                       "data_retention_laws", "foreign_ownership_restrictions",
                       "net_neutrality_legislation", "constitutional_right_to_internet",
                       "biometric_data_legislation", "right_to_be_forgotten_legislation",
                       "assembly_law_restrictions", "legal_right_to_protest",
                       "encrypted_messaging_restrictions", "platform_bans_or_restrictions",
                       "independent_news_sites_blocked"}:
                # These can be factual descriptors — check if evaluative
                if is_evaluative(value):
                    # Strip evaluative prefix, keep factual part if possible
                    # e.g. "low — RTÜK members appointed by AKP-controlled parliament"
                    # → "RTÜK members appointed by parliament" (factual)
                    parts = value.split("—")
                    if len(parts) > 1:
                        factual = parts[1].strip()
                        removed.append((path, key, f"EVALUATIVE STRIPPED: '{parts[0].strip()}'"))
                        return factual, None
                    else:
                        removed.append((path, key, value))
                        return None, None
                else:
                    return value, None  # Keep factual descriptors
            
            # Notes that are evaluative
            if key.endswith("_note"):
                removed.append((path, key, value))
                return None, None
            
            # Rights/quality fields that should be numeric/coded
            rights_fields = {
                "political_imprisonment", "bodily_autonomy", "social_safety_net",
                "refugee_policy", "healthcare_access", "housing_security",
                "food_security", "education_access", "judicial_independence",
                "due_process", "government_transparency", "scientific_integrity",
                "censorship", "labor_protections", "mutual_aid_networks",
                "community_support", "family_stability", "domestic_violence_severity",
                "community_organization", "volunteering_rate", "score", "mobility_note"
            }
            if key in rights_fields:
                removed.append((path, key, value))
                return None, None
            
            # Generic strings that are evaluative
            if is_evaluative(value):
                removed.append((path, key, value))
                return None, None
            
            removed.append((path, key, value))
            return None, None
        # Booleans and numbers are fine
        return value, None
    
    # Structural descriptors in government_type
    if key in STRUCTURAL_FIELDS:
        if isinstance(value, str):
            # Check if evaluative prefix
            if is_evaluative(value):
                parts = value.split("—")
                if len(parts) > 1:
                    factual = parts[1].strip()
                    removed.append((path, key, f"EVALUATIVE STRIPPED: '{parts[0].strip()}'"))
                    return factual, None
                else:
                    removed.append((path, key, value))
                    return None, None
            return value, None
        return value, None
    
    # Numbers, booleans — always keep
    if isinstance(value, (int, float, bool)):
        return value, None
    
    # Null — keep
    if value is None:
        return None, None
    
    # Nested objects — recurse
    if isinstance(value, dict):
        return None, None  # Will be handled by the recursive pass
    
    return value, None


def clean_country_data(data, country_name):
    """Recursively clean all fields in a country data object."""
    removed = []
    
    def recurse(obj, path=""):
        if not isinstance(obj, dict):
            return obj
        
        keys_to_delete = []
        new_obj = {}
        
        for key, value in obj.items():
            current_path = f"{path}.{key}" if path else key
            
            # Skip metadata fields
            if key in ("country", "country_code", "collection_date", "data_version",
                       "last_updated", "confidence_system", "source"):
                new_obj[key] = value
                continue
            
            # Commentary fields — mark for deletion
            if key in COMMENTARY_FIELDS:
                if value and value != "GST analysis to be performed separately from data collection":
                    removed.append((current_path, key, value))
                keys_to_delete.append(key)
                continue
            
            # Nested dict — recurse
            if isinstance(value, dict) and not ("confidence" in value or "value" in value):
                cleaned_sub = recurse(value, current_path)
                if cleaned_sub:  # Keep if non-empty
                    new_obj[key] = cleaned_sub
                continue
            
            # Confidence-flagged objects
            if isinstance(value, dict) and ("confidence" in value or "value" in value):
                cleaned = {}
                for k, v in value.items():
                    if k == "note":
                        if is_methodological_note(v):
                            cleaned[k] = v
                        else:
                            removed.append((current_path, f"{key}.note", v))
                            # Don't include interpretive notes
                    else:
                        cleaned[k] = v
                if cleaned:
                    new_obj[key] = cleaned
                continue
            
            # Free-text fields
            if isinstance(value, str):
                # Structural descriptors
                if key in STRUCTURAL_FIELDS:
                    if is_evaluative(value):
                        parts = value.split("—")
                        if len(parts) > 1:
                            factual = parts[1].strip()
                            removed.append((current_path, key, f"EVALUATIVE STRIPPED: '{parts[0].strip()}'"))
                            new_obj[key] = factual
                        else:
                            removed.append((current_path, key, value))
                    else:
                        new_obj[key] = value
                    continue
                
                # Institutional mechanism descriptors
                institutional_fields = {
                    "broadcast_licensing_process", "media_regulator_independence",
                    "digital_id_system_scope", "digital_surveillance_legislation",
                    "data_retention_laws", "foreign_ownership_restrictions",
                    "net_neutrality_legislation", "constitutional_right_to_internet",
                    "biometric_data_legislation", "right_to_be_forgotten_legislation",
                    "assembly_law_restrictions", "legal_right_to_protest",
                    "encrypted_messaging_restrictions", "platform_bans_or_restrictions",
                    "independent_news_sites_blocked", "sovereignty_origin",
                    "head_of_state_formal_powers"
                }
                if key in institutional_fields:
                    if is_evaluative(value):
                        parts = value.split("—")
                        if len(parts) > 1:
                            factual = parts[1].strip()
                            removed.append((current_path, key, f"EVALUATIVE STRIPPED: '{parts[0].strip()}'"))
                            new_obj[key] = factual
                        else:
                            removed.append((current_path, key, value))
                    else:
                        new_obj[key] = value
                    continue
                
                # Note fields — remove interpretive
                if key.endswith("_note"):
                    removed.append((current_path, key, value))
                    continue
                
                # Rights/quality fields that should not be free text
                evaluative_string_fields = {
                    "political_imprisonment", "bodily_autonomy", "social_safety_net",
                    "refugee_policy", "healthcare_access", "housing_security",
                    "food_security", "education_access", "judicial_independence",
                    "due_process", "government_transparency", "scientific_integrity",
                    "censorship", "labor_protections", "mutual_aid_networks",
                    "community_support", "family_stability", "domestic_violence_severity",
                    "community_organization", "volunteering_rate", "score",
                    "mobility_note", "swf_note", "tax_to_gdp_note",
                    "social_protection_note", "infrastructure_note",
                    "equal_access_note", "sami_rights_note", "volunteering_rate",
                    "mutual_aid", "regional_disparity", "mass_incarceration"
                }
                if key in evaluative_string_fields:
                    removed.append((current_path, key, value))
                    continue
                
                # Other strings — check if evaluative
                if is_evaluative(value):
                    removed.append((current_path, key, value))
                    continue
                
                # Keep factual strings
                new_obj[key] = value
                continue
            
            # Booleans — always keep
            if isinstance(value, bool):
                new_obj[key] = value
                continue
            
            # Numbers — always keep
            if isinstance(value, (int, float)):
                new_obj[key] = value
                continue
            
            # Null — keep
            if value is None:
                new_obj[key] = value
                continue
        
        return new_obj
    
    cleaned = recurse(data)
    return cleaned, removed


def main():
    os.makedirs(ANALYSIS_DIR, exist_ok=True)
    
    for fname in ["norway_pilot_v0.2.json", "turkey_pilot_v0.2.json", "usa_pilot_v0.2.json"]:
        filepath = os.path.join(DATA_DIR, fname)
        with open(filepath) as f:
            data = json.load(f)
        
        country = data["country"]
        print(f"\n{'='*60}")
        print(f"Cleaning: {country} ({fname})")
        print(f"{'='*60}")
        
        cleaned, removed = clean_country_data(data, country)
        
        # Write cleaned data
        with open(filepath, 'w') as f:
            json.dump(cleaned, f, indent=2, ensure_ascii=False)
        print(f"  Written cleaned data to {filepath}")
        
        # Write removed content to analysis
        analysis_path = os.path.join(ANALYSIS_DIR, f"{country.lower()}_removed_commentary.json")
        analysis_data = {
            "country": country,
            "cleaned_date": "2026-04-24",
            "note": "Commentary and evaluative labels removed from raw data. This content is interpretive and belongs in analysis, not in raw data inputs.",
            "removed_items": [
                {"path": r[0], "field": r[1], "original_value": r[2]} 
                for r in removed
            ]
        }
        with open(analysis_path, 'w') as f:
            json.dump(analysis_data, f, indent=2, ensure_ascii=False)
        print(f"  Moved {len(removed)} items to {analysis_path}")


if __name__ == "__main__":
    main()