def execute_query(chain, df, question):
    response = chain.invoke(
        {
            "columns": list(df.columns),
            "sample_data": df.head(5).to_string(),
            "question": question
        }
    )
    return response.content