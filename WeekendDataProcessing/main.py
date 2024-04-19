import pandas as pd

ACTIVE_METRIC_MESSAGE = \
    "The metric is active - aggregation is a summed value for whole period. Date is marked as latest entry"
NOT_ACTIVE_METRIC_MESSAGE = \
    "The metric is not active - we provide latest available data. Date is marked as latest entry"

df1 = pd.read_csv('data_2023-02-11.csv', sep=';')
df2 = pd.read_csv('data_2023-02-12.csv', sep=';')

values = []
explanation = []
for i in range(len(df1.metric_id)):
    if df1['metric_desc'][i].split()[0] == "active":
        values.append(df1['metric_value'][i] + df2['metric_value'][i])
        explanation.append(ACTIVE_METRIC_MESSAGE)
    else:
        values.append(df2['metric_value'][i])
        explanation.append(NOT_ACTIVE_METRIC_MESSAGE)

df = df2
df['metric_value'] = values
df['explanation'] = explanation

df.to_csv('output.csv', sep=';', encoding='utf-8')
