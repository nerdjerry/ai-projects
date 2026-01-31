# Project 5: Data Quality Copilot

## What is This?
An AI assistant that helps you check and improve the quality of your data. It analyzes CSV files, identifies issues, and suggests improvements - perfect for learning about data quality and AI together.

## What You'll Learn
- Data quality assessment
- Working with CSV files
- AI-powered data analysis
- Data cleaning techniques

## Prerequisites
- Python 3.8 or higher
- Basic Python knowledge
- OpenAI API key (get one at https://platform.openai.com)

## Step-by-Step Guide

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Your API Key
Create a `.env` file in this directory:
```
OPENAI_API_KEY=your-api-key-here
```

### Step 3: Add Your Data
Place CSV files in the `data/` folder that you want to analyze.

### Step 4: Run the Copilot
```bash
python data_copilot.py
```

### Step 5: Review Results
The copilot will analyze your data and provide:
- Data quality report
- Identified issues
- Improvement suggestions
- Summary statistics

## How It Works
1. **Load Data**: Reads CSV files from data folder
2. **Analyze**: Checks for common data quality issues
3. **AI Review**: Uses AI to provide insights
4. **Report**: Generates detailed quality report
5. **Suggestions**: Offers actionable improvements

## Files
- `data_copilot.py`: Main application code
- `requirements.txt`: Python dependencies
- `data/`: Place your CSV files here
- `sample_data.csv`: Example dataset
- `.env`: Your API key (create this yourself)

## Data Quality Checks

### Completeness
- Missing values
- Null percentages
- Empty strings

### Consistency
- Data type issues
- Format inconsistencies
- Duplicate records

### Validity
- Out-of-range values
- Invalid formats
- Constraint violations

### Accuracy
- Outliers
- Suspicious patterns
- Statistical anomalies

## Features
- **Automatic Detection**: Finds issues automatically
- **AI Insights**: Explains what issues mean
- **Prioritization**: Ranks issues by severity
- **Suggestions**: Provides fix recommendations
- **Export**: Saves report to file

## Example Issues Detected
- "Column 'age' has 15% missing values"
- "Duplicate records found (23 duplicates)"
- "Email column contains invalid formats"
- "Outliers detected in 'salary' column"
- "Date format inconsistent"

## Tips for Beginners
- Start with small CSV files
- Use the sample data to learn
- Review all suggestions carefully
- Understand each issue before fixing
- Keep original data backed up

## Sample Data Included
The project includes `sample_data.csv` with intentional issues:
- Missing values
- Duplicates
- Formatting problems
- Outliers

Use this to learn how the copilot works!

## Output
The copilot generates:
1. Console report (on-screen)
2. Text report file
3. Issue summary
4. Recommendations

## Common Use Cases
- Cleaning survey data
- Validating customer data
- Checking import files
- Preparing data for analysis
- Learning data quality

## Safety Features
- **Read-only**: Never modifies your original data
- **Backup reminder**: Suggests backing up files
- **Clear reporting**: Explains all findings
- **No automatic fixes**: You control changes

## Understanding Reports

### Severity Levels
- 🔴 **Critical**: Major data quality issues
- 🟡 **Warning**: Potential problems
- 🟢 **Info**: General observations

### Common Metrics
- **Completeness %**: How much data is filled in
- **Duplicate Rate**: Percentage of duplicate rows
- **Validity Score**: How many values are valid

## Next Steps
- Add data visualization
- Implement auto-fix suggestions
- Create data profiling
- Add custom validation rules
- Build data quality dashboard
