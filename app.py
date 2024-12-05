from flask import Flask, render_template, jsonify
import random
import numpy as np

app = Flask(__name__)

# Genomic data and SNP functions generation
def generate_snp_functions():
    traits = ["growth_rate", "hazard_resistance", "resource_efficiency"]
    snp_functions = {trait: {} for trait in traits}
    for trait in traits:
        num_snps = random.randint(1, 10)  # Randomly assign 1-10 SNPs to each trait
        for _ in range(num_snps):
            snp_index = random.randint(0, 9)  # SNP index (0-9)
            if snp_index in snp_functions[trait]:
                continue  # Avoid duplicates
            effects = {allele: round(random.uniform(-1, 2), 2) for allele in [0, 1, 2]}
            snp_functions[trait][snp_index] = effects
    return snp_functions

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/initialize")
def initialize():
    # Generate genomic data for 3 plants
    genomic_data = np.random.randint(0, 3, (3, 10)).tolist()  # 3 plants, 10 SNPs
    snp_functions = generate_snp_functions()
    return jsonify({"genomic_data": genomic_data, "snp_functions": snp_functions})

if __name__ == "__main__":
    app.run(debug=True)
