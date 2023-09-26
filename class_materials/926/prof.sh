# Save profiling summary to text file
python -m cProfile example.py > profile.txt

# Save to a log file and make a dot graph
python -m cProfile -o output.pstats example.py
gprof2dot -f pstats output.pstats | dot -Tpng -o output.png

