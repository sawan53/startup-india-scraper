"""
Data enrichment utilities for lead generation
Adds additional information to scraped startup data
"""

import re
import requests
from typing import Dict, Optional
import pandas as pd


class DataEnricher:
    """Enrich startup data with additional information"""
    
    @staticmethod
    def clean_company_name(name: str) -> str:
        """Clean and standardize company names"""
        if not name:
            return ""
        
        # Remove common suffixes
        suffixes = [
            'PRIVATE LIMITED', 'PVT LTD', 'PVT. LTD.', 'PRIVATE LTD',
            'LLP', 'LIMITED', 'LTD', 'INC', 'CORP', 'CORPORATION',
            '(OPC)', 'OPC'
        ]
        
        cleaned = name.upper()
        for suffix in suffixes:
            cleaned = cleaned.replace(suffix, '')
        
        return cleaned.strip()
    
    @staticmethod
    def extract_domain_from_email(email: str) -> Optional[str]:
        """Extract domain from email address"""
        if not email or '@' not in email:
            return None
        
        try:
            domain = email.split('@')[1]
            return domain
        except:
            return None
    
    @staticmethod
    def categorize_stage(stage: str) -> Dict[str, any]:
        """Categorize startup stage with additional insights"""
        stage_info = {
            'stage': stage,
            'maturity_level': 0,
            'investment_readiness': '',
            'risk_level': ''
        }
        
        if not stage:
            return stage_info
        
        stage_lower = stage.lower()
        
        if 'ideation' in stage_lower:
            stage_info['maturity_level'] = 1
            stage_info['investment_readiness'] = 'Seed/Angel'
            stage_info['risk_level'] = 'Very High'
        elif 'validation' in stage_lower:
            stage_info['maturity_level'] = 2
            stage_info['investment_readiness'] = 'Pre-Seed/Seed'
            stage_info['risk_level'] = 'High'
        elif 'early traction' in stage_lower:
            stage_info['maturity_level'] = 3
            stage_info['investment_readiness'] = 'Series A'
            stage_info['risk_level'] = 'Medium'
        elif 'scaling' in stage_lower:
            stage_info['maturity_level'] = 4
            stage_info['investment_readiness'] = 'Series B+'
            stage_info['risk_level'] = 'Low'
        
        return stage_info
    
    @staticmethod
    def categorize_sector(sector: str) -> Dict[str, str]:
        """Categorize sector with broader categories"""
        sector_mapping = {
            'AI': 'Technology',
            'Machine Learning': 'Technology',
            'IT Services': 'Technology',
            'SaaS': 'Technology',
            'FinTech': 'Financial Services',
            'Finance': 'Financial Services',
            'Healthcare': 'Healthcare & Lifesciences',
            'Lifesciences': 'Healthcare & Lifesciences',
            'MedTech': 'Healthcare & Lifesciences',
            'Education': 'Education & Training',
            'EdTech': 'Education & Training',
            'E-commerce': 'Retail & Commerce',
            'Retail': 'Retail & Commerce',
            'Food': 'Food & Beverages',
            'Agriculture': 'Agriculture & Agritech',
            'Renewable Energy': 'Energy & Environment',
            'CleanTech': 'Energy & Environment'
        }
        
        category = 'Other'
        for key, value in sector_mapping.items():
            if sector and key.lower() in sector.lower():
                category = value
                break
        
        return {
            'sector': sector,
            'broad_category': category
        }
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        if not email:
            return False
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number"""
        if not phone:
            return False
        
        # Remove common separators
        cleaned = re.sub(r'[\s\-\(\)\+]', '', phone)
        
        # Check if it's a valid number (10-15 digits)
        return cleaned.isdigit() and 10 <= len(cleaned) <= 15
    
    @staticmethod
    def enrich_location(city: str, state: str) -> Dict[str, any]:
        """Enrich location data with tier classification"""
        tier_1_cities = [
            'Mumbai', 'Delhi', 'Bengaluru', 'Bangalore', 'Hyderabad',
            'Chennai', 'Kolkata', 'Pune', 'Ahmedabad'
        ]
        
        tier_2_cities = [
            'Jaipur', 'Lucknow', 'Kochi', 'Chandigarh', 'Bhopal',
            'Indore', 'Coimbatore', 'Visakhapatnam', 'Nagpur', 'Vadodara'
        ]
        
        tier = 'Tier 3+'
        if city:
            if any(t1.lower() in city.lower() for t1 in tier_1_cities):
                tier = 'Tier 1'
            elif any(t2.lower() in city.lower() for t2 in tier_2_cities):
                tier = 'Tier 2'
        
        return {
            'city': city,
            'state': state,
            'tier': tier,
            'is_metro': tier == 'Tier 1'
        }
    
    @classmethod
    def enrich_dataframe(cls, df: pd.DataFrame) -> pd.DataFrame:
        """Enrich entire dataframe with additional columns"""
        enriched_df = df.copy()
        
        # Clean company names
        if 'company_name' in enriched_df.columns:
            enriched_df['company_name_cleaned'] = enriched_df['company_name'].apply(
                cls.clean_company_name
            )
        
        # Enrich stage information
        if 'stage' in enriched_df.columns:
            stage_info = enriched_df['stage'].apply(cls.categorize_stage)
            enriched_df['maturity_level'] = stage_info.apply(lambda x: x['maturity_level'])
            enriched_df['investment_readiness'] = stage_info.apply(lambda x: x['investment_readiness'])
            enriched_df['risk_level'] = stage_info.apply(lambda x: x['risk_level'])
        
        # Enrich sector information
        if 'sector' in enriched_df.columns:
            sector_info = enriched_df['sector'].apply(cls.categorize_sector)
            enriched_df['broad_category'] = sector_info.apply(lambda x: x['broad_category'])
        
        # Enrich location information
        if 'city' in enriched_df.columns and 'state' in enriched_df.columns:
            location_info = enriched_df.apply(
                lambda row: cls.enrich_location(row.get('city', ''), row.get('state', '')),
                axis=1
            )
            enriched_df['city_tier'] = location_info.apply(lambda x: x['tier'])
            enriched_df['is_metro'] = location_info.apply(lambda x: x['is_metro'])
        
        # Validate contact information
        if 'email' in enriched_df.columns:
            enriched_df['email_valid'] = enriched_df['email'].apply(cls.validate_email)
        
        if 'phone' in enriched_df.columns:
            enriched_df['phone_valid'] = enriched_df['phone'].apply(cls.validate_phone)
        
        return enriched_df


def enrich_leads_file(input_file: str, output_file: str = None):
    """
    Enrich a leads file with additional information
    
    Args:
        input_file: Path to input CSV/Excel file
        output_file: Path to output file (optional)
    """
    # Read file
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")
    
    print(f"Loaded {len(df)} records from {input_file}")
    
    # Enrich data
    enriched_df = DataEnricher.enrich_dataframe(df)
    
    print(f"Enriched data with {len(enriched_df.columns) - len(df.columns)} new columns")
    
    # Save enriched data
    if output_file is None:
        output_file = input_file.replace('.csv', '_enriched.csv').replace('.xlsx', '_enriched.xlsx')
    
    if output_file.endswith('.csv'):
        enriched_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    else:
        enriched_df.to_excel(output_file, index=False, engine='openpyxl')
    
    print(f"Enriched data saved to {output_file}")
    
    return enriched_df


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        enrich_leads_file(input_file, output_file)
    else:
        print("Usage: python data_enrichment.py <input_file> [output_file]")
        print("Example: python data_enrichment.py startup_leads.csv startup_leads_enriched.csv")
