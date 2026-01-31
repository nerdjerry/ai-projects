"""
Data Quality Copilot
====================
An AI assistant that analyzes CSV data and identifies quality issues.
Helps you understand and improve your data quality.

Key Features:
- Automatic quality checks
- AI-powered insights
- Detailed reporting
- Actionable suggestions
"""

import os
import csv
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_csv_file(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        file_path: Path to the CSV file
    
    Returns:
        pandas DataFrame or None if error
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def analyze_completeness(df):
    """
    Check for missing values and completeness.
    
    Args:
        df: pandas DataFrame
    
    Returns:
        Dictionary with completeness metrics
    """
    total_cells = df.size
    missing_cells = df.isnull().sum().sum()
    missing_percentage = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
    
    column_missing = {}
    for col in df.columns:
        missing = df[col].isnull().sum()
        if missing > 0:
            missing_pct = (missing / len(df)) * 100 if len(df) > 0 else 0
            column_missing[col] = {
                'count': missing,
                'percentage': round(missing_pct, 2)
            }
    
    return {
        'total_missing': missing_cells,
        'missing_percentage': round(missing_percentage, 2),
        'columns_with_missing': column_missing
    }


def analyze_duplicates(df):
    """
    Check for duplicate records.
    
    Args:
        df: pandas DataFrame
    
    Returns:
        Dictionary with duplicate information
    """
    duplicates = df.duplicated()
    num_duplicates = duplicates.sum()
    duplicate_percentage = (num_duplicates / len(df)) * 100 if len(df) > 0 else 0
    
    return {
        'count': num_duplicates,
        'percentage': round(duplicate_percentage, 2)
    }


def analyze_data_types(df):
    """
    Analyze data types and detect inconsistencies.
    
    Args:
        df: pandas DataFrame
    
    Returns:
        Dictionary with data type information
    """
    type_info = {}
    
    for col in df.columns:
        col_type = str(df[col].dtype)
        unique_count = df[col].nunique()
        
        type_info[col] = {
            'type': col_type,
            'unique_values': unique_count,
            'sample_values': df[col].dropna().head(3).tolist()
        }
    
    return type_info


def analyze_outliers(df):
    """
    Detect outliers in numerical columns.
    
    Args:
        df: pandas DataFrame
    
    Returns:
        Dictionary with outlier information
    """
    outliers = {}
    
    # Get numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    for col in numeric_cols:
        # Use IQR method to detect outliers
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outlier_mask = (df[col] < lower_bound) | (df[col] > upper_bound)
        num_outliers = outlier_mask.sum()
        
        if num_outliers > 0:
            outliers[col] = {
                'count': num_outliers,
                'percentage': round((num_outliers / len(df)) * 100, 2),
                'range': f"{lower_bound:.2f} to {upper_bound:.2f}"
            }
    
    return outliers


def create_quality_report(file_name, df, completeness, duplicates, types, outliers):
    """
    Create a text summary of data quality findings.
    
    Args:
        file_name: Name of the file
        df: DataFrame
        completeness: Completeness analysis results
        duplicates: Duplicate analysis results
        types: Data type analysis results
        outliers: Outlier analysis results
    
    Returns:
        Formatted report string
    """
    report = f"""
DATA QUALITY REPORT
{'='*60}

File: {file_name}
Rows: {len(df)}
Columns: {len(df.columns)}
Total Data Points: {df.size}

COMPLETENESS ANALYSIS
{'-'*60}
Missing Data: {completeness['total_missing']} cells ({completeness['missing_percentage']}%)
"""
    
    if completeness['columns_with_missing']:
        report += "\nColumns with Missing Values:\n"
        for col, info in completeness['columns_with_missing'].items():
            report += f"  • {col}: {info['count']} missing ({info['percentage']}%)\n"
    else:
        report += "✅ No missing values detected\n"
    
    report += f"""
DUPLICATE ANALYSIS
{'-'*60}
Duplicate Rows: {duplicates['count']} ({duplicates['percentage']}%)
"""
    
    if duplicates['count'] > 0:
        report += "⚠️  Consider removing duplicates\n"
    else:
        report += "✅ No duplicates found\n"
    
    report += f"""
DATA TYPE SUMMARY
{'-'*60}
"""
    for col, info in types.items():
        report += f"{col}:\n"
        report += f"  Type: {info['type']}\n"
        report += f"  Unique values: {info['unique_values']}\n"
    
    if outliers:
        report += f"""
OUTLIER DETECTION
{'-'*60}
"""
        for col, info in outliers.items():
            report += f"{col}:\n"
            report += f"  Outliers: {info['count']} ({info['percentage']}%)\n"
            report += f"  Expected range: {info['range']}\n"
    else:
        report += f"""
OUTLIER DETECTION
{'-'*60}
✅ No significant outliers detected in numeric columns
"""
    
    return report


def get_ai_recommendations(report):
    """
    Get AI-powered recommendations based on the quality report.
    
    Args:
        report: Text quality report
    
    Returns:
        AI-generated recommendations
    """
    prompt = f"""Analyze this data quality report and provide actionable recommendations:

{report}

Please provide:
1. Top 3 priority issues to fix
2. Specific suggestions for each issue
3. Beginner-friendly explanations
4. Best practices for data quality

Keep recommendations clear and practical."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data quality expert helping beginners improve their data. Provide clear, actionable advice."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=600
    )
    
    return response.choices[0].message.content


def save_report(report, recommendations, file_name):
    """
    Save the quality report to a file.
    
    Args:
        report: Quality report text
        recommendations: AI recommendations
        file_name: Original file name
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"quality_report_{timestamp}.txt"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
        f.write("\n\n")
        f.write("="*60)
        f.write("\nAI RECOMMENDATIONS\n")
        f.write("="*60)
        f.write("\n")
        f.write(recommendations)
    
    print(f"\n📄 Full report saved to: {output_file}")


def main():
    """
    Main function to run the data quality copilot.
    """
    print("=" * 60)
    print("Data Quality Copilot")
    print("=" * 60)
    print()
    print("AI-powered data quality analysis for your CSV files")
    print()
    
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Find CSV files
    csv_files = list(data_dir.glob("*.csv"))
    
    if not csv_files:
        print("No CSV files found in the 'data' folder.")
        print("Please add CSV files to analyze.")
        return
    
    print(f"Found {len(csv_files)} CSV file(s):\n")
    for i, file_path in enumerate(csv_files, 1):
        print(f"{i}. {file_path.name}")
    
    print()
    choice = input("Enter the number of the file to analyze (or 'quit'): ").strip()
    
    if choice.lower() in ['quit', 'exit', 'q']:
        return
    
    try:
        file_index = int(choice) - 1
        selected_file = csv_files[file_index]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    
    print(f"\n🔍 Analyzing {selected_file.name}...\n")
    
    # Load the data
    df = load_csv_file(selected_file)
    
    if df is None:
        return
    
    # Perform analyses
    print("Running quality checks...")
    completeness = analyze_completeness(df)
    duplicates = analyze_duplicates(df)
    types = analyze_data_types(df)
    outliers = analyze_outliers(df)
    
    # Create report
    report = create_quality_report(
        selected_file.name,
        df,
        completeness,
        duplicates,
        types,
        outliers
    )
    
    # Display report
    print(report)
    
    # Get AI recommendations
    print("\n💭 Getting AI recommendations...")
    recommendations = get_ai_recommendations(report)
    
    print("\n" + "="*60)
    print("AI RECOMMENDATIONS")
    print("="*60)
    print(recommendations)
    
    # Save report
    save_report(report, recommendations, selected_file.name)


if __name__ == "__main__":
    main()
