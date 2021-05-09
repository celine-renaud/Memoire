from syntaxgym import compute_surprisals, evaluate
from lm_zoo import get_registry


model=get_registry()["tinylstm"]

suite=compute_surprisals(model,"ORC_CMP.json")

results=evaluate(suite)

print(results.to_csv(sep="\t"))