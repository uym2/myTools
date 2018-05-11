import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i","--input",required=True,help="Input trees")
parser.add_argument("-d","--outdir",required=False,help="Output directory. Default: inferred from the input trees")
parser.add_argument("-t","--tempdir",required=False,help="Directory to keep temporary files. If specified, the temp files will be kept")
parser.add_argument("-o","--output",required=False,help="The name of the output trees. Default: inferred from the input trees")
parser.add_argument("-c","--centroid",required=False,action='store_true',help="Do centroid reroot in preprocessing. Highly recommended for large trees. Default: NO")
parser.add_argument("-k","--k",required=False,help="The maximum number of leaves that can be removed. Default: auto-select based on the data")
parser.add_argument("-q","--quantiles",required=False,help="The quantile(s) to set threshold. Default is 0.05")
parser.add_argument("-m","--mode",required=False,help="Filtering mode: 'per-species', 'per-gene', 'all-genes','auto'. Default: auto")

args = vars(parser.parse_args())
